const fs = require('fs');
const path = require('path');

console.log('🚨 REMOVING AFFILIATE LINKS FOR ADSENSE COMPLIANCE 🚨\n');

// Function to remove all affiliate content from HTML
const removeAffiliateContent = (html) => {
    let cleaned = html;
    
    // Remove all Amazon affiliate links (amzn.to and amazon.com with tags)
    cleaned = cleaned.replace(/https?:\/\/amzn\.to\/[A-Za-z0-9]+/g, '#');
    cleaned = cleaned.replace(/https?:\/\/(?:www\.)?amazon\.com\/[^"'\s>]*(?:tag=|linkCode=|ref=)[^"'\s>]*/g, '#');
    
    // Remove affiliate disclosure text
    cleaned = cleaned.replace(/As an Amazon Associate[^.]*\./g, '');
    cleaned = cleaned.replace(/\*As an Amazon Associate[^*]*\*/g, '');
    cleaned = cleaned.replace(/We earn from qualifying purchases[^.]*\./g, '');
    cleaned = cleaned.replace(/\*We earn from qualifying purchases[^*]*\*/g, '');
    
    // Remove entire affiliate product sections
    cleaned = cleaned.replace(/<div[^>]*class="[^"]*affiliate[^"]*"[^>]*>[\s\S]*?<\/div>/gi, '');
    
    // Remove "Essential Gear" sections that contain affiliate links
    cleaned = cleaned.replace(/<section[^>]*>[^<]*<h[2-6][^>]*>[^<]*Essential Gear[^<]*<\/h[2-6]>[\s\S]*?<\/section>/gi, '');
    
    // Remove product recommendation sections
    cleaned = cleaned.replace(/<div[^>]*class="[^"]*product[^"]*"[^>]*>[\s\S]*?<\/div>/gi, '');
    
    // Remove "Donor Essentials" sections
    cleaned = cleaned.replace(/<section[^>]*>[^<]*<h[2-6][^>]*>[^<]*Donor Essentials[^<]*<\/h[2-6]>[\s\S]*?<\/section>/gi, '');
    
    // Remove any remaining affiliate-related content
    cleaned = cleaned.replace(/affiliate|sponsored|paid partnership/gi, '');
    
    // Clean up empty sections and divs
    cleaned = cleaned.replace(/<div[^>]*>\s*<\/div>/g, '');
    cleaned = cleaned.replace(/<section[^>]*>\s*<\/section>/g, '');
    
    return cleaned;
};

// Function to process all HTML files
const processFiles = (dir) => {
    const items = fs.readdirSync(dir);
    let processedCount = 0;
    
    for (const item of items) {
        const fullPath = path.join(dir, item);
        const stat = fs.statSync(fullPath);
        
        if (stat.isDirectory() && !item.startsWith('.') && item !== 'node_modules') {
            processedCount += processFiles(fullPath);
        } else if (item.endsWith('.html')) {
            try {
                const content = fs.readFileSync(fullPath, 'utf8');
                const cleanedContent = removeAffiliateContent(content);
                
                // Only write if content actually changed
                if (content !== cleanedContent) {
                    fs.writeFileSync(fullPath, cleanedContent, 'utf8');
                    console.log(`✅ REMOVED AFFILIATE LINKS: ${fullPath}`);
                    processedCount++;
                } else {
                    console.log(`✓ CLEAN (no affiliates): ${fullPath}`);
                }
            } catch (error) {
                console.error(`❌ ERROR processing ${fullPath}:`, error.message);
            }
        }
    }
    
    return processedCount;
};

// Start processing from current directory
console.log(`📁 Processing all HTML files in: ${__dirname}\n`);

const totalProcessed = processFiles(__dirname);

console.log(`\n🎯 AFFILIATE REMOVAL COMPLETE!`);
console.log(`📊 Files processed: ${totalProcessed}`);
console.log(`✅ Site is now AFFILIATE-FREE for AdSense compliance!`);
console.log(`🚀 Ready for AdSense application!`);