/**
 * Exit Intent Popup Component
 * Triggers on mouse exit or 75% scroll depth
 * Uses sessionStorage to show only once per session
 */
(function() {
    'use strict';

    var STORAGE_KEY = 'exitPopupShown';
    var SCROLL_THRESHOLD = 0.75;

    // Check if popup has already been shown this session
    function hasBeenShown() {
        return sessionStorage.getItem(STORAGE_KEY) === 'true';
    }

    // Mark popup as shown
    function markAsShown() {
        sessionStorage.setItem(STORAGE_KEY, 'true');
    }

    // Create popup elements using DOM methods (safe from XSS)
    function createPopup() {
        // Create overlay
        var overlay = document.createElement('div');
        overlay.id = 'exitPopupOverlay';
        overlay.className = 'exit-popup-overlay';

        // Create modal
        var modal = document.createElement('div');
        modal.className = 'exit-popup-modal';

        // Close button
        var closeBtn = document.createElement('button');
        closeBtn.className = 'exit-popup-close';
        closeBtn.setAttribute('aria-label', 'Close popup');
        closeBtn.textContent = '\u00D7';

        // Content container
        var content = document.createElement('div');
        content.className = 'exit-popup-content';

        // Icon
        var iconDiv = document.createElement('div');
        iconDiv.className = 'exit-popup-icon';
        var iconSvg = document.createElementNS('http://www.w3.org/2000/svg', 'svg');
        iconSvg.setAttribute('width', '48');
        iconSvg.setAttribute('height', '48');
        iconSvg.setAttribute('viewBox', '0 0 24 24');
        iconSvg.setAttribute('fill', 'none');
        iconSvg.setAttribute('stroke', 'currentColor');
        iconSvg.setAttribute('stroke-width', '2');
        iconSvg.setAttribute('stroke-linecap', 'round');
        iconSvg.setAttribute('stroke-linejoin', 'round');

        var path1 = document.createElementNS('http://www.w3.org/2000/svg', 'path');
        path1.setAttribute('d', 'M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z');
        var polyline1 = document.createElementNS('http://www.w3.org/2000/svg', 'polyline');
        polyline1.setAttribute('points', '14 2 14 8 20 8');
        var line1 = document.createElementNS('http://www.w3.org/2000/svg', 'line');
        line1.setAttribute('x1', '16');
        line1.setAttribute('y1', '13');
        line1.setAttribute('x2', '8');
        line1.setAttribute('y2', '13');
        var line2 = document.createElementNS('http://www.w3.org/2000/svg', 'line');
        line2.setAttribute('x1', '16');
        line2.setAttribute('y1', '17');
        line2.setAttribute('x2', '8');
        line2.setAttribute('y2', '17');
        var polyline2 = document.createElementNS('http://www.w3.org/2000/svg', 'polyline');
        polyline2.setAttribute('points', '10 9 9 9 8 9');

        iconSvg.appendChild(path1);
        iconSvg.appendChild(polyline1);
        iconSvg.appendChild(line1);
        iconSvg.appendChild(line2);
        iconSvg.appendChild(polyline2);
        iconDiv.appendChild(iconSvg);

        // Title
        var title = document.createElement('h2');
        title.className = 'exit-popup-title';
        title.textContent = 'Before you go!';

        // Subtitle
        var subtitle = document.createElement('p');
        subtitle.className = 'exit-popup-subtitle';
        subtitle.textContent = 'Get our FREE Plasma Donation Earning Guide';

        // Description
        var description = document.createElement('p');
        description.className = 'exit-popup-description';
        description.textContent = 'Learn insider tips to maximize your plasma donation earnings. Discover which centers pay the most and how to qualify for bonus programs.';

        // Form
        var form = document.createElement('form');
        form.className = 'exit-popup-form';
        form.id = 'exitPopupForm';

        var inputWrapper = document.createElement('div');
        inputWrapper.className = 'exit-popup-input-wrapper';

        var input = document.createElement('input');
        input.type = 'email';
        input.className = 'exit-popup-input';
        input.placeholder = 'Enter your email address';
        input.required = true;
        input.setAttribute('aria-label', 'Email address');

        var submitBtn = document.createElement('button');
        submitBtn.type = 'submit';
        submitBtn.className = 'exit-popup-submit';
        submitBtn.textContent = 'Get Free Guide';

        inputWrapper.appendChild(input);
        inputWrapper.appendChild(submitBtn);
        form.appendChild(inputWrapper);

        // Dismiss button
        var dismissBtn = document.createElement('button');
        dismissBtn.className = 'exit-popup-dismiss';
        dismissBtn.id = 'exitPopupDismiss';
        dismissBtn.type = 'button';
        dismissBtn.textContent = 'No thanks, I\'ll figure it out myself';

        // Privacy text
        var privacy = document.createElement('p');
        privacy.className = 'exit-popup-privacy';
        privacy.textContent = 'We respect your privacy. Unsubscribe anytime.';

        // Assemble content
        content.appendChild(iconDiv);
        content.appendChild(title);
        content.appendChild(subtitle);
        content.appendChild(description);
        content.appendChild(form);
        content.appendChild(dismissBtn);
        content.appendChild(privacy);

        // Assemble modal
        modal.appendChild(closeBtn);
        modal.appendChild(content);

        // Assemble overlay
        overlay.appendChild(modal);

        return overlay;
    }

    // Create success message using DOM methods
    function createSuccessMessage() {
        var successDiv = document.createElement('div');
        successDiv.className = 'exit-popup-success';

        var successSvg = document.createElementNS('http://www.w3.org/2000/svg', 'svg');
        successSvg.setAttribute('width', '32');
        successSvg.setAttribute('height', '32');
        successSvg.setAttribute('viewBox', '0 0 24 24');
        successSvg.setAttribute('fill', 'none');
        successSvg.setAttribute('stroke', 'currentColor');
        successSvg.setAttribute('stroke-width', '2');
        successSvg.setAttribute('stroke-linecap', 'round');
        successSvg.setAttribute('stroke-linejoin', 'round');

        var successPath = document.createElementNS('http://www.w3.org/2000/svg', 'path');
        successPath.setAttribute('d', 'M22 11.08V12a10 10 0 1 1-5.93-9.14');
        var successPolyline = document.createElementNS('http://www.w3.org/2000/svg', 'polyline');
        successPolyline.setAttribute('points', '22 4 12 14.01 9 11.01');

        successSvg.appendChild(successPath);
        successSvg.appendChild(successPolyline);

        var successText = document.createElement('p');
        successText.textContent = 'Check your inbox for your free guide!';

        successDiv.appendChild(successSvg);
        successDiv.appendChild(successText);

        return successDiv;
    }

    // Show the popup
    function showPopup() {
        if (hasBeenShown()) return;

        var overlay = document.getElementById('exitPopupOverlay');
        if (overlay) {
            overlay.classList.add('active');
            markAsShown();
            document.body.style.overflow = 'hidden';
        }
    }

    // Hide the popup
    function hidePopup() {
        var overlay = document.getElementById('exitPopupOverlay');
        if (overlay) {
            overlay.classList.remove('active');
            document.body.style.overflow = '';
        }
    }

    // Initialize the popup
    function init() {
        // Don't initialize if already shown this session
        if (hasBeenShown()) return;

        // Create and inject popup into the page
        var popup = createPopup();
        document.body.appendChild(popup);

        // Get references to elements
        var overlay = document.getElementById('exitPopupOverlay');
        var closeBtn = overlay.querySelector('.exit-popup-close');
        var dismissBtn = document.getElementById('exitPopupDismiss');
        var form = document.getElementById('exitPopupForm');

        // Close button click
        closeBtn.addEventListener('click', hidePopup);

        // Dismiss button click
        dismissBtn.addEventListener('click', hidePopup);

        // Click outside to close
        overlay.addEventListener('click', function(e) {
            if (e.target === overlay) {
                hidePopup();
            }
        });

        // Escape key to close
        document.addEventListener('keydown', function(e) {
            if (e.key === 'Escape') {
                hidePopup();
            }
        });

        // Form submission (visual only - no backend)
        form.addEventListener('submit', function(e) {
            e.preventDefault();
            var submitBtn = form.querySelector('.exit-popup-submit');

            // Show success state
            submitBtn.textContent = 'Sending...';
            submitBtn.disabled = true;

            // Simulate form submission
            setTimeout(function() {
                // Clear form and show success
                while (form.firstChild) {
                    form.removeChild(form.firstChild);
                }
                form.appendChild(createSuccessMessage());

                // Auto-close after success
                setTimeout(hidePopup, 3000);
            }, 1000);
        });

        // Exit intent detection (mouse leaves viewport from top)
        var exitIntentTriggered = false;
        document.addEventListener('mouseout', function(e) {
            if (exitIntentTriggered) return;

            // Check if mouse left from the top of the page
            if (e.clientY <= 0) {
                exitIntentTriggered = true;
                showPopup();
            }
        });

        // Scroll depth trigger (75%)
        var scrollTriggered = false;
        window.addEventListener('scroll', function() {
            if (scrollTriggered || hasBeenShown()) return;

            var scrollTop = window.pageYOffset || document.documentElement.scrollTop;
            var scrollHeight = document.documentElement.scrollHeight - document.documentElement.clientHeight;
            var scrollPercent = scrollTop / scrollHeight;

            if (scrollPercent >= SCROLL_THRESHOLD) {
                scrollTriggered = true;
                showPopup();
            }
        });
    }

    // Initialize when DOM is ready
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }
})();
