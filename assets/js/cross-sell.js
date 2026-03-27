(function(){
  'use strict';
  var p=window.location.pathname;
  if(p==='/'||p==='/index.html'||p==='/contact.html'||p==='/about.html'||p==='/privacy.html'||p==='/terms.html'||p==='/disclaimer.html')return;
  if(document.getElementById('cross-sell-section'))return;
  function init(){
    var f=document.querySelector('footer')||document.querySelector('[class*="footer"]');
    if(!f)return;
    var section=document.createElement('div');
    section.id='cross-sell-section';
    section.style.cssText='margin:2.5rem auto 0;padding:0 1rem';
    var container=document.createElement('a');
    container.href='https://buy.stripe.com/28E7sMbbE8LN6LNcKI2cg0h';
    container.target='_blank';
    container.rel='noopener';
    container.style.cssText='display:block;max-width:640px;margin:0 auto;padding:2rem;background:linear-gradient(135deg,#064e3b,#065f46);border-radius:16px;text-decoration:none;text-align:center';
    var label=document.createElement('p');
    label.style.cssText='font-size:0.7rem;font-weight:700;text-transform:uppercase;letter-spacing:0.15em;color:#6ee7b7;margin:0 0 0.75rem';
    label.textContent='EARNING FROM DONATIONS? EARN EVEN MORE.';
    var headline=document.createElement('p');
    headline.style.cssText='font-size:1.4rem;font-weight:700;color:#ffffff;margin:0 0 0.75rem;line-height:1.3';
    headline.textContent='The Side Hustle Launch Kit \u2014 Start a Second Income Stream';
    var body=document.createElement('p');
    body.style.cssText='font-size:0.9rem;color:#d1d5db;margin:0 auto 1.25rem;max-width:520px;line-height:1.5';
    body.textContent='3 auto-calculating spreadsheets + 7 expert guides. Track income, find your hustle, and save on taxes. Used by 5,000+ hustlers.';
    var cta=document.createElement('span');
    cta.style.cssText='display:inline-block;padding:0.75rem 1.75rem;background:#ffffff;color:#064e3b;font-size:0.95rem;font-weight:700;border-radius:8px';
    cta.textContent='Get the Launch Kit \u2014 $19 \u2192';
    var trust=document.createElement('p');
    trust.style.cssText='font-size:0.7rem;color:#9ca3af;margin:0.75rem 0 0';
    trust.textContent='Instant download \u00b7 Excel + PDF guides';
    container.appendChild(label);
    container.appendChild(headline);
    container.appendChild(body);
    container.appendChild(cta);
    container.appendChild(trust);
    section.appendChild(container);
    f.parentNode.insertBefore(section,f);
  }
  if(document.readyState==='loading'){document.addEventListener('DOMContentLoaded',init)}else{init()}
})();
