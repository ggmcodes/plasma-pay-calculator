# Plasma Pay Calculator

A comprehensive website for calculating plasma donation income with center directory and educational blog.

## Live Site
- **Primary Domain**: https://plasmapaycalculator.com
- **Redirect Domains**: 
  - plasmadonorcalculator.com
  - plasmapaycalc.com

## Features

### 🧮 Income Calculator
- Calculate weekly and monthly plasma donation earnings
- Support for new vs returning donor rates
- Weight-based payment multipliers
- Gas cost calculations using IRS mileage rates
- Tax estimation (20% withholding suggestion)
- Support for major plasma center chains:
  - CSL Plasma
  - BioLife Plasma Services
  - Octapharma Plasma
  - Grifols Biomat USA
  - KedPlasma
  - ImmunoTek Bio Centers
  - GCAM Plasma

### 🏥 Centers Directory
Comprehensive directory organized by state with:
- Center names and addresses
- Phone numbers
- No external links (keeps visitors on site)
- Quick state navigation
- AdSense ad placement between sections

### ❓ Eligibility Quiz
Interactive 5-question quiz covering:
- Age requirements (18+)
- Weight requirements (110+ lbs)
- Recent tattoos/piercings
- Required documentation
- Health status

### 📚 Blog Structure
Educational content including:
- Maximizing earnings guides
- Requirements and eligibility
- Center comparisons
- Health and safety information
- Tax implications
- Newsletter signup

## Technical Details

### Built With
- HTML5
- CSS3 (Flexbox & Grid)
- Vanilla JavaScript
- Responsive design
- SEO optimized

### Files Structure
```
/
├── index.html          # Main calculator page
├── centers.html        # Plasma centers directory
├── style.css          # Main stylesheet
├── calculator.js      # Calculator functionality
├── blog/
│   └── index.html     # Blog homepage
└── README.md          # This file
```

### Payment Rate Data
Calculator includes current 2025 rates for:
- New donor promotional rates (4-week programs)
- Returning donor standard rates
- Weight-based multipliers:
  - Under 150 lbs: 1.0x
  - 150-174 lbs: 1.1x
  - 175+ lbs: 1.2x

### AdSense Integration
Placeholder divs ready for AdSense:
- After calculator results
- Between every 3 states in directory
- In blog content areas

## Domain Setup

### Primary Domain
- **plasmapaycalculator.com** - Main domain

### Redirect Domains
Configure these domains to redirect to primary:
- **plasmadonorcalculator.com** → plasmapaycalculator.com
- **plasmapaycalc.com** → plasmapaycalculator.com

### DNS Configuration
```
Type: CNAME
Name: www
Value: plasmapaycalculator.com

Type: A
Name: @
Value: [Your hosting IP]
```

## SEO Features
- Semantic HTML structure
- Meta descriptions and titles
- Canonical URLs
- Internal linking strategy
- Mobile-responsive design
- Fast loading times
- Structured data ready

## Deployment
1. Upload files to web hosting
2. Configure domain redirects
3. Set up SSL certificates
4. Add Google AdSense code
5. Set up Google Analytics
6. Submit sitemap to search engines

## Future Enhancements
- Location-based center finder
- Email newsletter integration
- User accounts for tracking earnings
- Mobile app version
- Multi-language support

## License
All rights reserved - Commercial website

## Contact
For technical issues or updates, contact the site administrator.