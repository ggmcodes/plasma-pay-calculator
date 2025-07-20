#!/usr/bin/env python3
"""
Implement mobile UX enhancements for calculators
"""

import os
import re
from glob import glob

def add_mobile_viewport_enhancements():
    """Enhance mobile viewport and touch optimization"""
    
    # Find all calculator pages
    calculator_files = glob("/Users/glengomezmeade/Projects/plasma-pay-calculator/calculators/**/index.html", recursive=True)
    
    enhanced_count = 0
    
    for file_path in calculator_files[:5]:  # Test on first 5 files
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original_content = content
            
            # Check if already has touch enhancements
            if 'touch-action' in content:
                continue
            
            # Add mobile-specific CSS enhancements
            mobile_css = '''
    <!-- Mobile UX Enhancements -->
    <style>
        /* Mobile Touch Optimization */
        @media (max-width: 768px) {
            /* Larger touch targets */
            button, .btn, a.btn {
                min-height: 48px;
                min-width: 48px;
                padding: 12px 24px;
            }
            
            /* Better input fields for mobile */
            input, select, textarea {
                font-size: 16px !important; /* Prevents zoom on iOS */
                padding: 16px;
                border-radius: 8px;
                touch-action: manipulation;
            }
            
            /* Improved calculator layout */
            .calculator-container {
                padding: 20px 16px;
            }
            
            /* Better spacing for mobile */
            .space-y-6 > * + * {
                margin-top: 24px;
            }
            
            /* Sticky calculate button */
            .calculate-button-container {
                position: sticky;
                bottom: 20px;
                z-index: 10;
                background: white;
                padding: 16px;
                border-radius: 16px;
                box-shadow: 0 -4px 20px rgba(0,0,0,0.1);
            }
            
            /* Smooth scrolling */
            html {
                scroll-behavior: smooth;
                -webkit-overflow-scrolling: touch;
            }
            
            /* Prevent horizontal scroll */
            body {
                overflow-x: hidden;
            }
            
            /* Better card layout */
            .grid {
                gap: 16px !important;
            }
            
            /* Improved readability */
            p, .text-sm {
                font-size: 16px;
                line-height: 1.6;
            }
            
            /* Touch feedback */
            button:active, a:active {
                transform: scale(0.98);
                opacity: 0.9;
            }
        }
        
        /* Accessibility improvements */
        :focus-visible {
            outline: 3px solid #27ae60;
            outline-offset: 2px;
        }
        
        /* Smooth transitions */
        * {
            -webkit-tap-highlight-color: transparent;
        }
    </style>'''
            
            # Insert mobile CSS before closing </head>
            content = content.replace('</head>', mobile_css + '\n</head>')
            
            # Add touch-friendly attributes to buttons
            content = re.sub(
                r'<button([^>]*?)onclick="calculateEarnings\(\)"([^>]*?)>',
                r'<button\1onclick="calculateEarnings()"\2 class="touch-action-manipulation">',
                content
            )
            
            # Enhance select dropdowns for mobile
            content = re.sub(
                r'<select([^>]*?)>',
                r'<select\1 class="touch-action-manipulation">',
                content
            )
            
            if content != original_content:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                
                enhanced_count += 1
                rel_path = os.path.relpath(file_path, "/Users/glengomezmeade/Projects/plasma-pay-calculator")
                print(f"✅ Enhanced mobile UX for {rel_path}")
            
        except Exception as e:
            print(f"❌ Error enhancing {file_path}: {str(e)}")
    
    return enhanced_count

def add_mobile_navigation_improvements():
    """Improve mobile navigation experience"""
    
    nav_improvements = '''
<script>
// Mobile Navigation Improvements
document.addEventListener('DOMContentLoaded', function() {
    // Smooth scroll for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });
    
    // Add loading states to buttons
    document.querySelectorAll('button').forEach(button => {
        button.addEventListener('click', function() {
            if (this.onclick && this.onclick.toString().includes('calculate')) {
                this.innerHTML = '<span class="spinner">⏳</span> Calculating...';
                setTimeout(() => {
                    this.innerHTML = this.getAttribute('data-original-text') || 'Calculate';
                }, 500);
            }
        });
        button.setAttribute('data-original-text', button.innerHTML);
    });
    
    // Improve select dropdown UX on mobile
    if (/iPhone|iPad|iPod|Android/i.test(navigator.userAgent)) {
        document.querySelectorAll('select').forEach(select => {
            select.style.fontSize = '16px';
            select.style.padding = '16px';
        });
    }
    
    // Add haptic feedback for supported devices
    if (window.navigator && window.navigator.vibrate) {
        document.querySelectorAll('button, a.btn').forEach(element => {
            element.addEventListener('click', () => {
                window.navigator.vibrate(10);
            });
        });
    }
});
</script>'''
    
    # Add to main calculator page
    index_path = "/Users/glengomezmeade/Projects/plasma-pay-calculator/index.html"
    
    try:
        with open(index_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if 'Mobile Navigation Improvements' not in content:
            content = content.replace('</body>', nav_improvements + '\n</body>')
            
            with open(index_path, 'w', encoding='utf-8') as f:
                f.write(content)
            
            print("✅ Added mobile navigation improvements to main calculator")
            return True
    except Exception as e:
        print(f"❌ Error adding mobile navigation: {str(e)}")
        return False

def create_progressive_web_app_manifest():
    """Create PWA manifest for better mobile experience"""
    
    manifest_content = {
        "name": "Plasma Pay Calculator",
        "short_name": "Plasma Calc",
        "description": "Calculate your plasma donation earnings across all 50 states",
        "start_url": "/",
        "display": "standalone",
        "background_color": "#f8fffe",
        "theme_color": "#27ae60",
        "orientation": "portrait-primary",
        "icons": [
            {
                "src": "/android-chrome-192x192.png",
                "sizes": "192x192",
                "type": "image/png"
            },
            {
                "src": "/android-chrome-512x512.png",
                "sizes": "512x512",
                "type": "image/png"
            }
        ],
        "categories": ["finance", "medical", "utilities"],
        "lang": "en-US"
    }
    
    import json
    
    manifest_path = "/Users/glengomezmeade/Projects/plasma-pay-calculator/manifest.json"
    
    # Check if manifest already exists
    if os.path.exists(manifest_path):
        print("ℹ️ PWA manifest already exists")
        return False
    
    try:
        with open(manifest_path, 'w', encoding='utf-8') as f:
            json.dump(manifest_content, f, indent=2)
        
        print("✅ Created PWA manifest for mobile app experience")
        
        # Add manifest link to index.html
        index_path = "/Users/glengomezmeade/Projects/plasma-pay-calculator/index.html"
        with open(index_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if 'manifest.json' not in content:
            manifest_link = '    <link rel="manifest" href="/manifest.json">\n'
            content = content.replace('</head>', manifest_link + '</head>')
            
            with open(index_path, 'w', encoding='utf-8') as f:
                f.write(content)
            
            print("✅ Added manifest link to index.html")
        
        return True
        
    except Exception as e:
        print(f"❌ Error creating PWA manifest: {str(e)}")
        return False

def add_touch_gestures():
    """Add touch gesture support for better mobile UX"""
    
    touch_script = '''
<script>
// Touch Gesture Support
(function() {
    let touchStartX = 0;
    let touchStartY = 0;
    let touchEndX = 0;
    let touchEndY = 0;
    
    const calculatorForm = document.querySelector('.calculator-container, .bg-gradient-to-br');
    
    if (calculatorForm) {
        calculatorForm.addEventListener('touchstart', function(e) {
            touchStartX = e.changedTouches[0].screenX;
            touchStartY = e.changedTouches[0].screenY;
        });
        
        calculatorForm.addEventListener('touchend', function(e) {
            touchEndX = e.changedTouches[0].screenX;
            touchEndY = e.changedTouches[0].screenY;
            handleGesture();
        });
    }
    
    function handleGesture() {
        // Swipe up to calculate
        if (touchEndY < touchStartY - 50) {
            const calculateBtn = document.querySelector('button[onclick*="calculate"]');
            if (calculateBtn) {
                calculateBtn.click();
            }
        }
    }
    
    // Pull to refresh on results
    let pulling = false;
    let pullDistance = 0;
    
    document.addEventListener('touchstart', function(e) {
        if (window.scrollY === 0) {
            pulling = true;
            pullDistance = 0;
        }
    });
    
    document.addEventListener('touchmove', function(e) {
        if (pulling) {
            pullDistance = e.touches[0].clientY;
            if (pullDistance > 100) {
                document.body.style.transform = `translateY(${Math.min(pullDistance - 100, 50)}px)`;
            }
        }
    });
    
    document.addEventListener('touchend', function() {
        if (pulling && pullDistance > 150) {
            location.reload();
        }
        pulling = false;
        document.body.style.transform = '';
    });
})();
</script>'''
    
    # Add to a few key pages
    pages = [
        "/Users/glengomezmeade/Projects/plasma-pay-calculator/index.html",
        "/Users/glengomezmeade/Projects/plasma-pay-calculator/calculators/texas/index.html"
    ]
    
    added_count = 0
    
    for page_path in pages:
        if os.path.exists(page_path):
            try:
                with open(page_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                if 'Touch Gesture Support' not in content:
                    content = content.replace('</body>', touch_script + '\n</body>')
                    
                    with open(page_path, 'w', encoding='utf-8') as f:
                        f.write(content)
                    
                    added_count += 1
                    print(f"✅ Added touch gestures to {os.path.basename(page_path)}")
                    
            except Exception as e:
                print(f"❌ Error adding touch gestures: {str(e)}")
    
    return added_count

def main():
    """Main function to implement mobile UX enhancements"""
    print("📱 Implementing mobile UX enhancements for calculators...")
    
    total_enhancements = 0
    
    # Add mobile viewport enhancements
    print("\n📐 Adding mobile viewport enhancements...")
    viewport_count = add_mobile_viewport_enhancements()
    total_enhancements += viewport_count
    print(f"✅ Enhanced {viewport_count} calculator pages")
    
    # Add mobile navigation improvements
    print("\n🧭 Adding mobile navigation improvements...")
    if add_mobile_navigation_improvements():
        total_enhancements += 1
    
    # Create PWA manifest
    print("\n📱 Creating Progressive Web App manifest...")
    if create_progressive_web_app_manifest():
        total_enhancements += 1
    
    # Add touch gestures
    print("\n👆 Adding touch gesture support...")
    touch_count = add_touch_gestures()
    total_enhancements += touch_count
    
    print(f"\n🎉 Mobile UX enhancement complete!")
    print(f"📊 Total enhancements: {total_enhancements}")
    print(f"✨ Improved: Touch targets, input fields, navigation, gestures")
    print(f"📱 Added: PWA support, haptic feedback, smooth scrolling")

if __name__ == "__main__":
    main()