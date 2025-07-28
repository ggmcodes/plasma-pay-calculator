// Submit directly to Bing IndexNow endpoint
const https = require('https');

const API_KEY = '216b734625ce462a9ae6f78c0f846310';
const HOST = 'plasmapaycalculator.com';
const KEY_LOCATION = `https://${HOST}/${API_KEY}.txt`;

function submitToBing(urls) {
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

    console.log('Submitting to Bing IndexNow...');
    console.log('Key location:', KEY_LOCATION);
    console.log('URLs:', urls);

    const req = https.request(options, (res) => {
        console.log(`Bing response: ${res.statusCode}`);
        
        let responseData = '';
        res.on('data', (chunk) => {
            responseData += chunk;
        });
        
        res.on('end', () => {
            if (responseData) {
                console.log('Response:', responseData);
            }
        });
    });

    req.on('error', (error) => {
        console.error('Error:', error);
    });

    req.write(data);
    req.end();
}

// Test with homepage
submitToBing(['https://plasmapaycalculator.com/']);