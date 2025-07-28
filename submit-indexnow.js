// IndexNow URL submission script
// Usage: node submit-indexnow.js [url1] [url2] [url3]...

const https = require('https');

const API_KEY = '216b734625ce462a9ae6f78c0f846310';
const HOST = 'plasmapaycalculator.com';
const KEY_LOCATION = `https://${HOST}/${API_KEY}.txt`;

function submitToIndexNow(urls) {
    const data = JSON.stringify({
        host: HOST,
        key: API_KEY,
        keyLocation: KEY_LOCATION,
        urlList: urls
    });

    const options = {
        hostname: 'www.bing.com',
        port: 443,
        path: '/indexnow',
        method: 'POST',
        headers: {
            'Content-Type': 'application/json; charset=utf-8',
            'Content-Length': data.length
        }
    };

    const req = https.request(options, (res) => {
        console.log(`IndexNow response: ${res.statusCode}`);
        console.log(`URLs submitted: ${urls.length}`);
        
        res.on('data', (d) => {
            if (d.toString().trim()) {
                console.log('Response:', d.toString());
            }
        });
    });

    req.on('error', (error) => {
        console.error('Error submitting to IndexNow:', error);
    });

    req.write(data);
    req.end();
}

// Get URLs from command line arguments or use defaults
const urls = process.argv.slice(2);

if (urls.length === 0) {
    // Submit main pages by default
    const defaultUrls = [
        `https://${HOST}/`,
        `https://${HOST}/centers/`,
        `https://${HOST}/blog/`,
    ];
    console.log('No URLs provided, submitting main pages...');
    submitToIndexNow(defaultUrls);
} else {
    // Make sure URLs are full URLs
    const fullUrls = urls.map(url => {
        if (url.startsWith('http')) {
            return url;
        } else {
            return `https://${HOST}${url.startsWith('/') ? url : '/' + url}`;
        }
    });
    
    console.log('Submitting URLs to IndexNow...');
    submitToIndexNow(fullUrls);
}