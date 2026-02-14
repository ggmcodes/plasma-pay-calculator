// Universal AdSense Auto Ads Loader
// Include this on any page: <script src="/js/adsense-loader.js"></script>
// It will automatically inject Google AdSense if not already present.
(function() {
  var PUB_ID = 'ca-pub-3180649272238451';
  if (document.querySelector('script[src*="' + PUB_ID + '"]')) return;
  var s = document.createElement('script');
  s.async = true;
  s.crossOrigin = 'anonymous';
  s.src = 'https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=' + PUB_ID;
  document.head.appendChild(s);
})();
