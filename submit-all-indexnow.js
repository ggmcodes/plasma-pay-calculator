// Submit all URLs from sitemap to IndexNow
const fs = require('fs');
const https = require('https');
const { DOMParser } = require('xmldom');

const API_KEY = '216b734625ce462a9ae6f78c0f846310';

function extractUrlsFromSitemap(sitemapPath) {
    try {
        const sitemapContent = fs.readFileSync(sitemapPath, 'utf-8');
        const parser = new DOMParser();
        const xmlDoc = parser.parseFromString(sitemapContent, 'text/xml');
        
        const urlElements = xmlDoc.getElementsByTagName('loc');
        const urls = [];
        
        for (let i = 0; i < urlElements.length; i++) {
            const url = urlElements[i].textContent.trim();
            if (url) {
                urls.push(url);
            }
        }
        
        return urls;
    } catch (error) {
        console.error('Error reading sitemap:', error.message);
        return [];
    }
}

function submitBatch(urls, batchNumber) {
    return new Promise((resolve, reject) => {
        const data = JSON.stringify({
            host: 'plasmapaycalculator.com',
            key: API_KEY,
            keyLocation: `https://plasmapaycalculator.com/${API_KEY}.txt`,
            urlList: urls
        });

        const options = {
            hostname: 'yandex.com',
            port: 443,
            path: '/indexnow',
            method: 'POST',
            headers: {
                'Content-Type': 'application/json; charset=utf-8',
                'Content-Length': data.length
            }
        };

        const req = https.request(options, (res) => {
            let responseData = '';
            res.on('data', (chunk) => responseData += chunk);
            res.on('end', () => {
                console.log(`Batch ${batchNumber}: ${res.statusCode} - ${urls.length} URLs`);
                if (responseData.trim()) {
                    console.log(`Response: ${responseData}`);
                }
                resolve({ batchNumber, status: res.statusCode, response: responseData, urlCount: urls.length });
            });
        });

        req.on('error', (error) => {
            console.error(`Batch ${batchNumber} error:`, error.message);
            reject(error);
        });

        req.write(data);
        req.end();
    });
}

async function submitAllUrls() {
    console.log('Extracting URLs from sitemap...');
    const allUrls = extractUrlsFromSitemap('sitemap.xml');
    
    if (allUrls.length === 0) {
        console.log('No URLs found in sitemap!');
        return;
    }
    
    console.log(`Found ${allUrls.length} URLs in sitemap`);
    console.log('Submitting to IndexNow in batches of 100...\n');
    
    // Split into batches of 100 (IndexNow limit is typically 10,000 but smaller batches are more reliable)
    const batchSize = 100;
    const batches = [];
    
    for (let i = 0; i < allUrls.length; i += batchSize) {
        batches.push(allUrls.slice(i, i + batchSize));
    }
    
    console.log(`Created ${batches.length} batches of up to ${batchSize} URLs each\n`);
    
    let successCount = 0;
    let totalSubmitted = 0;
    
    for (let i = 0; i < batches.length; i++) {
        try {
            const result = await submitBatch(batches[i], i + 1);
            totalSubmitted += result.urlCount;
            
            if (result.status === 200 || (result.response && result.response.includes('success'))) {
                successCount++;
            }
            
            // Small delay between batches to avoid rate limiting
            if (i < batches.length - 1) {
                await new Promise(resolve => setTimeout(resolve, 2000));
            }
            
        } catch (error) {
            console.error(`Failed to submit batch ${i + 1}:`, error.message);
        }
    }
    
    console.log('\n=== IndexNow Submission Complete ===');
    console.log(`Total URLs processed: ${totalSubmitted}`);
    console.log(`Successful batches: ${successCount}/${batches.length}`);
    console.log(`Success rate: ${((successCount / batches.length) * 100).toFixed(1)}%`);
}

// Check if xmldom is available, if not, provide instructions
try {
    require('xmldom');
    submitAllUrls();
} catch (error) {
    console.log('xmldom package not found. Installing...');
    
    const { exec } = require('child_process');
    exec('npm install xmldom', (error, stdout, stderr) => {
        if (error) {
            console.error('Failed to install xmldom. Please run: npm install xmldom');
            process.exit(1);
        } else {
            console.log('xmldom installed successfully. Running submission...');
            // Restart the script
            delete require.cache[require.resolve('xmldom')];
            submitAllUrls();
        }
    });
}