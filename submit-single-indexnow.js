// Submit individual URLs to IndexNow using GET method
const https = require('https');

const API_KEY = '216b734625ce462a9ae6f78c0f846310';
const BASE_URL = 'https://plasmapaycalculator.com';

const newPages = [
    '/comprehensive-plasma-tax-guide-2025.html',
    '/weight-requirements-maximum-pay-guide.html', 
    '/csl-biolife-octapharma-comparison-guide.html',
    '/calculators/california/',
    '/plasma-centers-near-me-open-now.html',
    '/plasma-donation-pay-chart-by-state.html'
];

function submitUrl(url) {
    return new Promise((resolve, reject) => {
        const fullUrl = `${BASE_URL}${url}`;
        const submitUrl = `https://indexnow.org/indexnow?url=${encodeURIComponent(fullUrl)}&key=${API_KEY}`;
        
        https.get(submitUrl, (res) => {
            let data = '';
            res.on('data', (chunk) => data += chunk);
            res.on('end', () => {
                console.log(`✓ Submitted: ${url} (Status: ${res.statusCode})`);
                if (data.trim()) {
                    console.log(`  Response: ${data}`);
                }
                resolve({ url, status: res.statusCode, response: data });
            });
        }).on('error', (err) => {
            console.log(`✗ Failed: ${url} - ${err.message}`);
            reject(err);
        });
    });
}

async function submitAllUrls() {
    console.log('Submitting new pages to IndexNow...\n');
    
    for (const url of newPages) {
        try {
            await submitUrl(url);
            // Small delay between submissions
            await new Promise(resolve => setTimeout(resolve, 1000));
        } catch (error) {
            console.error(`Error submitting ${url}:`, error.message);
        }
    }
    
    console.log('\nIndexNow submission complete!');
}

submitAllUrls();