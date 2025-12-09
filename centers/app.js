// BestPlasmaCenters Frontend Application
class PlasmaApp {
    constructor() {
        this.centers = [];
        this.filteredCenters = [];
        this.allCenters = []; // Store all loaded centers
        this.currentPage = 0;
        this.pageSize = 4; // Show only 4 centers initially
        this.userLocation = null;
        this.searchRadius = 50;
        this.lastSearchQuery = null; // Track the last search query
        this.isSearchMode = false; // Track if we're in search mode
        this.isPinnedMode = false; // Track if we're showing featured/pinned centers
        this.commonZipCodes = []; // For autocomplete
        this.isDataLoaded = false; // Track if JSON data is loaded
        this.filters = {
            distance: 50,
            centerTypes: [],
            rating: 0
        };
        
        this.init();
    }

    async init() {
        this.setupEventListeners();
        this.setupZipAutocomplete();
        this.setupLazyLoading();
        await this.loadStats();
        await this.loadCenterData(); // Load JSON data first
        await this.loadInitialCenters();
        this.getUserLocation();
        this.updateHeroWithLocation();
        
        // Check if there's a search query in the URL
        this.handleURLSearch();
    }

    setupLazyLoading() {
        if ('IntersectionObserver' in window) {
            this.lazyImageObserver = new IntersectionObserver((entries, observer) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting) {
                        const img = entry.target;
                        if (img.dataset.src) {
                            img.src = img.dataset.src;
                            img.removeAttribute('data-src');
                            observer.unobserve(img);
                        }
                    }
                });
            }, {
                rootMargin: '50px 0px'
            });
        }
    }

    setupEventListeners() {
        // Search functionality
        const searchBtn = document.getElementById('search-btn');
        const searchInput = document.getElementById('location-search');
        const geolocationBtn = document.getElementById('geolocation-btn');
        const clearFiltersBtn = document.getElementById('clear-filters');
        
        
        if (searchBtn) {
            searchBtn.addEventListener('click', (e) => {
                e.preventDefault();
                this.performSearch();
            });
        }
        
        if (searchInput) {
            searchInput.addEventListener('keypress', (e) => {
                if (e.key === 'Enter') {
                    this.performSearch();
                }
            });
        }
        
        // Setup autocomplete and real-time search
        if (searchInput) {
            searchInput.addEventListener('input', (e) => {
                this.handleAutocomplete(e);
                // Real-time search as user types (debounced)
                clearTimeout(this.searchTimeout);
                this.searchTimeout = setTimeout(() => {
                    const value = e.target.value.trim();
                    if (value.length >= 3) { // Start searching after 3 characters
                        // Add visual feedback that search is happening
                        searchInput.style.borderColor = '#3B82F6';
                        this.performSearch();
                        // Reset border after search
                        setTimeout(() => {
                            searchInput.style.borderColor = '';
                        }, 500);
                    }
                }, 300); // 300ms delay for snappy but not too aggressive
            });
            
            searchInput.addEventListener('keydown', (e) => this.handleAutocompleteKeydown(e));
            searchInput.addEventListener('blur', () => this.hideAutocomplete());
        }
        
        // Geolocation functionality
        geolocationBtn?.addEventListener('click', () => this.useGeolocation());
        
        // Clear filters functionality
        clearFiltersBtn?.addEventListener('click', () => this.clearAllFilters());

        // Filters dropdown toggle functionality
        this.setupFiltersDropdown();

        // Filter listeners
        document.querySelectorAll('input[name="distance"]').forEach(radio => {
            radio.addEventListener('change', (e) => {
                this.filters.distance = parseInt(e.target.value);
                this.applyFilters();
            });
        });

        document.querySelectorAll('input[name="rating"]').forEach(radio => {
            radio.addEventListener('change', (e) => {
                this.filters.rating = parseFloat(e.target.value);
                this.applyFilters();
            });
        });

        document.querySelectorAll('.filter-section input[type="checkbox"]').forEach(checkbox => {
            checkbox.addEventListener('change', () => {
                this.updateCenterTypeFilters();
                this.applyFilters();
            });
        });

        // Sort functionality
        const sortSelect = document.getElementById('sort-select');
        sortSelect?.addEventListener('change', (e) => {
            this.sortCenters(e.target.value);
        });

        // Load more functionality
        const loadMoreBtn = document.getElementById('load-more-btn');
        loadMoreBtn?.addEventListener('click', () => this.loadMoreCenters());
    }

    async loadStats() {
        try {
            // Use hardcoded stats instead of API
            const stats = {
                totalCenters: 3012,
                totalStates: 50,
                totalReviews: 47293
            };
            
            const totalCentersEl = document.getElementById('total-centers');
            const statCentersEl = document.getElementById('stat-centers');
            
            if (totalCentersEl) {
                totalCentersEl.textContent = `${stats.totalCenters.toLocaleString()}+`;
            }
            if (statCentersEl) {
                statCentersEl.textContent = stats.totalCenters.toLocaleString();
            }
        } catch (error) {
            console.error('Failed to load stats:', error);
        }
    }

    async loadCenterData() {
        if (this.isDataLoaded) return; // Prevent multiple loads
        
        console.log('📦 Loading center data...');
        
        // Try to load full JSON database first
        try {
            console.log('📦 Fetching /data/centers.json...');
            const response = await fetch('/data/centers.json');
            console.log('📦 Response status:', response.status, response.statusText);
            
            if (response.ok) {
                const data = await response.json();
                console.log('📦 JSON parsed, data:', data);
                console.log('📦 Centers array length:', data.centers?.length);
                
                if (data.centers && data.centers.length > 0) {
                    this.allCenters = data.centers;
                    this.isDataLoaded = true;
                    console.log(`✅ Loaded ${this.allCenters.length} centers from JSON database`);
                    return;
                } else {
                    console.log('⚠️ JSON data invalid or empty centers array');
                }
            } else {
                console.log('⚠️ JSON fetch failed with status:', response.status);
            }
        } catch (error) {
            console.error('⚠️ JSON database failed:', error);
        }
        
        // Fallback to hardcoded data if JSON fails
        console.log('📦 Falling back to hardcoded data...');
        this.allCenters = this.getHardcodedCenters();
        this.isDataLoaded = true;
        console.log(`✅ Loaded ${this.allCenters.length} centers from hardcoded fallback`);
    }

    async loadInitialCenters() {
        // Reset search mode when loading initial centers
        this.isSearchMode = false;
        this.lastSearchQuery = null;
        this.currentPage = 0;
        this.isPinnedMode = true; // Mark as showing featured centers
        
        console.log('📌 Loading featured centers from data...');
        
        // Load featured centers from our data instead of relying on hardcoded HTML
        if (this.allCenters && this.allCenters.length > 0) {
            // Get a good mix of popular centers from different states/brands
            const featuredCenters = this.allCenters
                .filter(center => center.rating >= 4.0) // High rated centers
                .sort((a, b) => (b.rating * b.reviews) - (a.rating * a.reviews)) // Sort by rating * reviews
                .slice(0, 4); // Take top 4 for initial display
            
            this.centers = featuredCenters;
            this.filteredCenters = [...this.centers];
            
            console.log('📌 Loaded', this.centers.length, 'featured centers');
            this.displayCenters();
            this.updateResultsInfo(`Featured Plasma Centers`);
        } else {
            console.log('⚠️ No data loaded yet, keeping HTML featured centers');
            this.hideLoading();
            this.updateResultsInfo(`Featured Plasma Centers`);
        }
        
        console.log(`✅ Featured centers loading complete`);
    }

    async loadLocationBasedCenters(latitude, longitude) {
        console.log('📍 Loading location-based centers...', { latitude, longitude });
        
        try {
            this.showLoading(true);
            
            // Use loaded center data instead of API
            const allCenters = this.allCenters;
            
            // Calculate distances and sort by proximity
            const centersWithDistance = allCenters.map(center => ({
                ...center,
                distance: this.calculateDistance(latitude, longitude, center.latitude, center.longitude)
            })).filter(center => center.distance <= 50) // 50 mile radius
              .sort((a, b) => a.distance - b.distance)
              .slice(0, 30); // Limit to 30 results
            
            console.log('📊 Location-based centers loaded:', centersWithDistance.length);
            
            if (centersWithDistance.length > 0) {
                this.centers = centersWithDistance;
                this.filteredCenters = [...this.centers];
                this.isPinnedMode = false; // Switch from pinned to location mode
                this.isSearchMode = false;
                this.lastSearchQuery = null;
                
                console.log('📍 Loaded', this.centers.length, 'centers near your location');
                this.displayCenters();
                this.updateResultsInfo(`🎯 ${this.centers.length} Plasma Centers Near You`);
                
                // Update hero headline to be more personal
                const heroHeadline = document.getElementById('hero-headline');
                if (heroHeadline) {
                    heroHeadline.textContent = 'Plasma Centers Near You - Earn up to $1,766 This Month';
                }
                
                // Track location-based load for analytics
                if (typeof gtag === 'function') {
                    gtag('event', 'location_centers_loaded', {
                        event_category: 'User Location',
                        event_label: 'Auto Location Detection',
                        value: centersWithDistance.length
                    });
                }
            } else {
                console.log('ℹ️ No centers found near location, keeping featured centers');
            }
            
        } catch (error) {
            console.error('❌ Failed to load location-based centers:', error);
            // Keep the featured centers if location search fails
        } finally {
            this.showLoading(false);
        }
    }

    handleURLSearch() {
        // Check if there's a search parameter in the URL
        const urlParams = new URLSearchParams(window.location.search);
        const searchQuery = urlParams.get('search');
        
        if (searchQuery) {
            console.log('🔎 Found search query in URL:', searchQuery);
            
            // Set the search input value
            const searchInput = document.getElementById('location-search');
            if (searchInput) {
                searchInput.value = searchQuery;
                
                // Scroll to search section
                const searchSection = document.getElementById('search');
                if (searchSection) {
                    searchSection.scrollIntoView({ behavior: 'smooth', block: 'start' });
                }
                
                // Perform the search after a short delay to ensure everything is loaded
                setTimeout(() => {
                    this.performSearch();
                }, 500);
            }
        }
    }

    async performSearch() {
        console.log('🔎 performSearch called');
        
        const searchInput = document.getElementById('location-search');
        if (!searchInput) {
            console.error('❌ Search input not found');
            return;
        }
        
        const location = searchInput.value.trim();
        console.log('🔎 Search input value:', location);
        
        if (!location) {
            console.log('❌ Empty search input');
            this.showSearchError('Please enter a ZIP code');
            return;
        }

        // More flexible validation for better UX
        const isValidZip = /^\d{5}$/.test(location);
        const isValidCity = /^[a-zA-Z\s,.-]+$/.test(location) && location.length >= 2;
        const isPartialInput = location.length >= 2; // Allow shorter inputs for real-time search
        
        console.log('🔎 Validation - isValidZip:', isValidZip, 'isValidCity:', isValidCity, 'length:', location.length);
        
        if (!isValidZip && !isValidCity && !isPartialInput) {
            console.log('❌ Invalid format');
            this.showSearchError('Please enter a city name or ZIP code');
            return;
        }

        this.clearSearchError();
        console.log('✅ Starting search for:', location);
        
        // Track search event for analytics
        if (typeof trackSearch === 'function') {
            trackSearch(location, this.userLocation ? `${this.userLocation.latitude},${this.userLocation.longitude}` : 'unknown');
        }
        
        // Skip loading indicator for snappy real-time search
        const isRealTimeSearch = this.searchTimeout; // If triggered by typing
        if (!isRealTimeSearch) {
            this.showLoading(true);
        }
        
        try {
            console.log('🔎 Calling searchByText...');
            await this.searchByText(location);
            console.log('✅ searchByText completed');
        } catch (error) {
            console.error('❌ Search failed:', error);
            this.showError('Search failed. Please try a different location.');
        } finally {
            if (!isRealTimeSearch) {
                this.showLoading(false);
            }
        }
    }

    useGeolocation() {
        const geolocationBtn = document.getElementById('geolocation-btn');
        
        if (!navigator.geolocation) {
            this.showSearchError('Geolocation is not supported by this browser');
            return;
        }

        geolocationBtn.innerHTML = '⌛';
        geolocationBtn.disabled = true;
        this.clearSearchError();

        navigator.geolocation.getCurrentPosition(
            async (position) => {
                const { latitude, longitude } = position.coords;
                console.log('📍 Manual geolocation requested:', latitude, longitude);
                
                // Store user location
                this.userLocation = { latitude, longitude };
                
                try {
                    // Use the new location-based centers function
                    await this.loadLocationBasedCenters(latitude, longitude);
                    
                    // Update search input to show "Your Location"
                    const searchInput = document.getElementById('location-search');
                    if (searchInput) {
                        searchInput.value = 'Your Location';
                    }
                    
                    // Track manual geolocation use
                    if (typeof gtag === 'function') {
                        gtag('event', 'manual_geolocation', {
                            event_category: 'User Location',
                            event_label: 'Geolocation Button Clicked'
                        });
                    }
                    
                } catch (error) {
                    console.error('Manual geolocation search failed:', error);
                    this.showSearchError('Unable to find centers near your location. Please try entering a ZIP code.');
                }
                
                geolocationBtn.innerHTML = '📍';
                geolocationBtn.disabled = false;
            },
            (error) => {
                console.error('Geolocation error:', error);
                let message = 'Unable to get your location. ';
                if (error.code === error.PERMISSION_DENIED) {
                    message += 'Please allow location access or enter a ZIP code manually.';
                } else if (error.code === error.POSITION_UNAVAILABLE) {
                    message += 'Location information is unavailable.';
                } else {
                    message += 'Location request timed out.';
                }
                this.showSearchError(message);
                
                geolocationBtn.innerHTML = '📍';
                geolocationBtn.disabled = false;
            },
            { timeout: 10000, enableHighAccuracy: true }
        );
    }

    clearAllFilters() {
        // Reset distance filter to default (25 miles)
        const distanceRadios = document.querySelectorAll('input[name="distance"]');
        distanceRadios.forEach(radio => {
            radio.checked = radio.value === '50';
        });

        // Clear center type checkboxes
        const centerTypeCheckboxes = document.querySelectorAll('.filter-section input[type="checkbox"]');
        centerTypeCheckboxes.forEach(checkbox => {
            checkbox.checked = false;
        });

        // Reset rating filter
        const ratingRadios = document.querySelectorAll('input[name="rating"]');
        ratingRadios.forEach(radio => {
            radio.checked = false;
        });

        // Reset filters object
        this.filters = {
            distance: 50,
            centerTypes: [],
            rating: 0
        };

        // Reapply filters
        this.applyFilters();
        
        console.log('🧹 All filters cleared');
    }

    showSearchError(message) {
        const errorDiv = document.getElementById('search-error');
        if (errorDiv) {
            errorDiv.textContent = message;
            errorDiv.style.display = 'block';
        } else {
            console.warn('Search error element not found, using alert:', message);
            // Fallback: show error in console or create temporary error display
        }
    }

    clearSearchError() {
        const errorDiv = document.getElementById('search-error');
        if (errorDiv) {
            errorDiv.style.display = 'none';
        }
        // If element doesn't exist, just ignore - no error to clear
    }

    async geocodeLocation(location) {
        console.log('🗺️ Geocoding location:', location);
        
        // If it's a ZIP code, try a more accurate geocoding approach
        if (/^\d{5}$/.test(location)) {
            console.log('🏛️ ZIP code detected, using enhanced geocoding for:', location);
            
            // First try to find an exact match in our data
            const allCenters = this.allCenters;
            const exactMatch = allCenters.find(center => center.postal_code === location);
            
            if (exactMatch) {
                console.log('✅ Found exact ZIP match for geocoding:', exactMatch.city);
                return {
                    latitude: exactMatch.latitude,
                    longitude: exactMatch.longitude
                };
            }
            
            // Try ZIP code database lookup using a simplified geographical center
            const zipCoords = this.getZipCodeCoordinates(location);
            if (zipCoords) {
                console.log('✅ Found ZIP coordinates from database for', location, ':', zipCoords);
                return zipCoords;
            } else {
                console.log('⚠️ ZIP', location, 'not found in database, trying fallback methods');
            }
            
            // Fallback: try to use coordinates from centers in the same ZIP prefix
            const zipPrefix = location.substring(0, 3);
            const prefixCenters = allCenters.filter(center => 
                center.postal_code && center.postal_code.startsWith(zipPrefix)
            );
            
            if (prefixCenters.length > 0) {
                // Use average coordinates of centers with same prefix
                const avgLat = prefixCenters.reduce((sum, center) => sum + center.latitude, 0) / prefixCenters.length;
                const avgLng = prefixCenters.reduce((sum, center) => sum + center.longitude, 0) / prefixCenters.length;
                console.log('✅ Using average coordinates from ZIP prefix', zipPrefix);
                return {
                    latitude: avgLat,
                    longitude: avgLng
                };
            }
        }
        
        // Try to find a center matching the location
        const allCenters = this.allCenters;
        const matchingCenter = allCenters.find(center => {
            const city = center.city || '';
            const state = center.state || '';
            return city.toLowerCase().includes(location.toLowerCase()) ||
                   state.toLowerCase().includes(location.toLowerCase()) ||
                   center.postal_code === location;
        });
        
        if (matchingCenter) {
            console.log('✅ Found matching center for geocoding:', matchingCenter.city);
            return {
                latitude: matchingCenter.latitude,
                longitude: matchingCenter.longitude
            };
        }
        
        // If no direct match, try state-based search for smaller cities
        // This helps cities like "Denton, TX" find all Texas centers
        const stateSearchTerms = [
            { pattern: /,?\s*(texas|tx)$/i, state: 'Texas' },
            { pattern: /,?\s*(california|ca)$/i, state: 'California' },
            { pattern: /,?\s*(florida|fl)$/i, state: 'Florida' },
            { pattern: /,?\s*(new york|ny)$/i, state: 'New York' },
            { pattern: /,?\s*(illinois|il)$/i, state: 'Illinois' },
            { pattern: /,?\s*(pennsylvania|pa)$/i, state: 'Pennsylvania' },
            { pattern: /,?\s*(ohio|oh)$/i, state: 'Ohio' },
            { pattern: /,?\s*(michigan|mi)$/i, state: 'Michigan' },
            { pattern: /,?\s*(georgia|ga)$/i, state: 'Georgia' },
            { pattern: /,?\s*(north carolina|nc)$/i, state: 'North Carolina' },
            { pattern: /,?\s*(virginia|va)$/i, state: 'Virginia' },
            { pattern: /,?\s*(washington|wa)$/i, state: 'Washington' },
            { pattern: /,?\s*(arizona|az)$/i, state: 'Arizona' },
            { pattern: /,?\s*(massachusetts|ma)$/i, state: 'Massachusetts' },
            { pattern: /,?\s*(tennessee|tn)$/i, state: 'Tennessee' },
            { pattern: /,?\s*(indiana|in)$/i, state: 'Indiana' },
            { pattern: /,?\s*(missouri|mo)$/i, state: 'Missouri' },
            { pattern: /,?\s*(maryland|md)$/i, state: 'Maryland' },
            { pattern: /,?\s*(wisconsin|wi)$/i, state: 'Wisconsin' },
            { pattern: /,?\s*(colorado|co)$/i, state: 'Colorado' },
            { pattern: /,?\s*(minnesota|mn)$/i, state: 'Minnesota' },
            { pattern: /,?\s*(south carolina|sc)$/i, state: 'South Carolina' },
            { pattern: /,?\s*(alabama|al)$/i, state: 'Alabama' },
            { pattern: /,?\s*(louisiana|la)$/i, state: 'Louisiana' },
            { pattern: /,?\s*(kentucky|ky)$/i, state: 'Kentucky' },
            { pattern: /,?\s*(oregon|or)$/i, state: 'Oregon' },
            { pattern: /,?\s*(oklahoma|ok)$/i, state: 'Oklahoma' },
            { pattern: /,?\s*(connecticut|ct)$/i, state: 'Connecticut' },
            { pattern: /,?\s*(utah|ut)$/i, state: 'Utah' },
            { pattern: /,?\s*(iowa|ia)$/i, state: 'Iowa' },
            { pattern: /,?\s*(nevada|nv)$/i, state: 'Nevada' },
            { pattern: /,?\s*(arkansas|ar)$/i, state: 'Arkansas' },
            { pattern: /,?\s*(mississippi|ms)$/i, state: 'Mississippi' },
            { pattern: /,?\s*(kansas|ks)$/i, state: 'Kansas' },
            { pattern: /,?\s*(new mexico|nm)$/i, state: 'New Mexico' },
            { pattern: /,?\s*(nebraska|ne)$/i, state: 'Nebraska' },
            { pattern: /,?\s*(west virginia|wv)$/i, state: 'West Virginia' },
            { pattern: /,?\s*(idaho|id)$/i, state: 'Idaho' },
            { pattern: /,?\s*(hawaii|hi)$/i, state: 'Hawaii' },
            { pattern: /,?\s*(new hampshire|nh)$/i, state: 'New Hampshire' },
            { pattern: /,?\s*(maine|me)$/i, state: 'Maine' },
            { pattern: /,?\s*(montana|mt)$/i, state: 'Montana' },
            { pattern: /,?\s*(rhode island|ri)$/i, state: 'Rhode Island' },
            { pattern: /,?\s*(delaware|de)$/i, state: 'Delaware' },
            { pattern: /,?\s*(south dakota|sd)$/i, state: 'South Dakota' },
            { pattern: /,?\s*(north dakota|nd)$/i, state: 'North Dakota' },
            { pattern: /,?\s*(alaska|ak)$/i, state: 'Alaska' },
            { pattern: /,?\s*(vermont|vt)$/i, state: 'Vermont' },
            { pattern: /,?\s*(wyoming|wy)$/i, state: 'Wyoming' }
        ];
        
        for (const stateInfo of stateSearchTerms) {
            if (stateInfo.pattern.test(location)) {
                console.log('✅ Detected state search for:', stateInfo.state);
                
                // Try to use external geocoding first for accurate city coordinates
                try {
                    const coords = await this.geocodeWithExternalAPI(location);
                    if (coords) {
                        console.log('✅ Using external geocoding for:', location);
                        return coords;
                    }
                } catch (error) {
                    console.log('⚠️ External geocoding failed, trying fallback methods');
                }
                
                // Fallback: Try to find coordinates from known city database
                const cityCoords = this.getCityCoordinates(location, stateInfo.state);
                if (cityCoords) {
                    console.log('✅ Using city coordinates from database for:', location);
                    return cityCoords;
                }
                
                // Last resort: Use state center coordinates
                const stateCenters = allCenters.filter(center => 
                    center.state && center.state.toLowerCase() === stateInfo.state.toLowerCase()
                );
                if (stateCenters.length > 0) {
                    // Use the center closest to the state's geographic center instead of first
                    const stateCenter = this.getStateCenterCoordinates(stateInfo.state);
                    if (stateCenter) {
                        console.log('✅ Using state center coordinates for:', stateInfo.state);
                        return stateCenter;
                    }
                    
                    const firstCenter = stateCenters[0];
                    console.log('✅ Using coordinates from first center:', firstCenter.city, firstCenter.state);
                    return {
                        latitude: firstCenter.latitude,
                        longitude: firstCenter.longitude
                    };
                }
            }
        }
        
        console.log('❌ No coordinates found for:', location);
        return null;
    }

    // External geocoding using a free service (no API key required)
    async geocodeWithExternalAPI(location) {
        try {
            // Using OpenStreetMap Nominatim API (free, no API key required)
            const encodedLocation = encodeURIComponent(location);
            const response = await fetch(`https://nominatim.openstreetmap.org/search?format=json&q=${encodedLocation}&countrycodes=us&limit=1`);
            
            if (!response.ok) {
                throw new Error(`HTTP ${response.status}`);
            }
            
            const data = await response.json();
            
            if (data && data.length > 0) {
                const result = data[0];
                return {
                    latitude: parseFloat(result.lat),
                    longitude: parseFloat(result.lon)
                };
            }
            
            return null;
        } catch (error) {
            console.log('⚠️ External geocoding API error:', error.message);
            return null;
        }
    }

    // Get coordinates from a comprehensive city database
    getCityCoordinates(location, state) {
        const cityName = location.toLowerCase().replace(/,.*$/, '').trim();
        const stateKey = state.toLowerCase();
        
        // Comprehensive city coordinates database
        const cityDatabase = {
            'texas': {
                'richardson': { latitude: 32.9483, longitude: -96.7299 },
                'coppell': { latitude: 32.9544, longitude: -97.0150 },
                'plano': { latitude: 33.0198, longitude: -96.6989 },
                'garland': { latitude: 32.9126, longitude: -96.6389 },
                'irving': { latitude: 32.8140, longitude: -96.9489 },
                'mesquite': { latitude: 32.7668, longitude: -96.5992 },
                'carrollton': { latitude: 32.9537, longitude: -96.8903 },
                'addison': { latitude: 32.9618, longitude: -96.8292 },
                'allen': { latitude: 33.1031, longitude: -96.6705 },
                'frisco': { latitude: 33.1507, longitude: -96.8236 },
                'mckinney': { latitude: 33.1972, longitude: -96.6153 },
                'lewisville': { latitude: 33.0462, longitude: -97.0067 },
                'flower mound': { latitude: 33.0143, longitude: -97.0969 },
                'grapevine': { latitude: 32.9343, longitude: -97.0781 },
                'duncanville': { latitude: 32.6518, longitude: -96.9083 },
                'desoto': { latitude: 32.5896, longitude: -96.8570 },
                'cedar hill': { latitude: 32.5885, longitude: -96.9561 },
                'grand prairie': { latitude: 32.7460, longitude: -96.9978 },
                'arlington': { latitude: 32.7357, longitude: -97.1081 },
                'fort worth': { latitude: 32.7555, longitude: -97.3308 },
                'dallas': { latitude: 32.7767, longitude: -96.7970 },
                'houston': { latitude: 29.7604, longitude: -95.3698 },
                'austin': { latitude: 30.2672, longitude: -97.7431 },
                'san antonio': { latitude: 29.4241, longitude: -98.4936 },
                'el paso': { latitude: 31.7619, longitude: -106.4850 },
                'corpus christi': { latitude: 27.8006, longitude: -97.3964 },
                'lubbock': { latitude: 33.5779, longitude: -101.8552 },
                'amarillo': { latitude: 35.2220, longitude: -101.8313 },
                'beaumont': { latitude: 30.0860, longitude: -94.1019 },
                'brownsville': { latitude: 25.9018, longitude: -97.4975 },
                'killeen': { latitude: 31.1171, longitude: -97.7278 },
                'laredo': { latitude: 27.5306, longitude: -99.4803 },
                'pasadena': { latitude: 29.6911, longitude: -95.2091 },
                'waco': { latitude: 31.5494, longitude: -97.1467 },
                'denton': { latitude: 33.2148, longitude: -97.1331 },
                'tyler': { latitude: 32.3513, longitude: -95.3011 },
                'wichita falls': { latitude: 33.9137, longitude: -98.4934 }
            },
            'california': {
                'los angeles': { latitude: 34.0522, longitude: -118.2437 },
                'san francisco': { latitude: 37.7749, longitude: -122.4194 },
                'san diego': { latitude: 32.7157, longitude: -117.1611 },
                'sacramento': { latitude: 38.5816, longitude: -121.4944 },
                'fresno': { latitude: 36.7378, longitude: -119.7871 },
                'long beach': { latitude: 33.7701, longitude: -118.1937 },
                'oakland': { latitude: 37.8044, longitude: -122.2711 },
                'bakersfield': { latitude: 35.3733, longitude: -119.0187 },
                'anaheim': { latitude: 33.8366, longitude: -117.9143 },
                'santa ana': { latitude: 33.7455, longitude: -117.8677 },
                'riverside': { latitude: 33.9806, longitude: -117.3755 },
                'stockton': { latitude: 37.9577, longitude: -121.2908 },
                'irvine': { latitude: 33.6846, longitude: -117.8265 },
                'chula vista': { latitude: 32.6401, longitude: -117.0842 },
                'fremont': { latitude: 37.5485, longitude: -121.9886 },
                'san bernardino': { latitude: 34.1083, longitude: -117.2898 },
                'modesto': { latitude: 37.6391, longitude: -120.9969 },
                'fontana': { latitude: 34.0922, longitude: -117.4350 },
                'oxnard': { latitude: 34.1975, longitude: -119.1771 },
                'moreno valley': { latitude: 33.9425, longitude: -117.2297 }
            },
            'florida': {
                'miami': { latitude: 25.7617, longitude: -80.1918 },
                'tampa': { latitude: 27.9506, longitude: -82.4572 },
                'orlando': { latitude: 28.5383, longitude: -81.3792 },
                'jacksonville': { latitude: 30.3322, longitude: -81.6557 },
                'st petersburg': { latitude: 27.7676, longitude: -82.6403 },
                'hialeah': { latitude: 25.8576, longitude: -80.2781 },
                'tallahassee': { latitude: 30.4518, longitude: -84.2807 },
                'fort lauderdale': { latitude: 26.1224, longitude: -80.1373 },
                'port st lucie': { latitude: 27.2939, longitude: -80.3501 },
                'cape coral': { latitude: 26.5629, longitude: -81.9495 },
                'hollywood': { latitude: 26.0112, longitude: -80.1495 },
                'gainesville': { latitude: 29.6516, longitude: -82.3248 },
                'miramar': { latitude: 25.9873, longitude: -80.2322 },
                'coral springs': { latitude: 26.2710, longitude: -80.2706 },
                'clearwater': { latitude: 27.9659, longitude: -82.8001 },
                'miami beach': { latitude: 25.7907, longitude: -80.1300 },
                'spring hill': { latitude: 28.4900, longitude: -82.5268 },
                'largo': { latitude: 27.9095, longitude: -82.7873 },
                'palm bay': { latitude: 28.0345, longitude: -80.5887 },
                'west palm beach': { latitude: 26.7153, longitude: -80.0534 }
            },
            'new york': {
                'new york': { latitude: 40.7128, longitude: -74.0060 },
                'buffalo': { latitude: 42.8864, longitude: -78.8784 },
                'rochester': { latitude: 43.1566, longitude: -77.6088 },
                'yonkers': { latitude: 40.9312, longitude: -73.8988 },
                'syracuse': { latitude: 43.0481, longitude: -76.1474 },
                'albany': { latitude: 42.6526, longitude: -73.7562 },
                'new rochelle': { latitude: 40.9115, longitude: -73.7826 },
                'mount vernon': { latitude: 40.9126, longitude: -73.8370 },
                'schenectady': { latitude: 42.8142, longitude: -73.9396 },
                'utica': { latitude: 43.1009, longitude: -75.2327 }
            },
            'illinois': {
                'chicago': { latitude: 41.8781, longitude: -87.6298 },
                'aurora': { latitude: 41.7606, longitude: -88.3201 },
                'rockford': { latitude: 42.2711, longitude: -89.0940 },
                'joliet': { latitude: 41.5250, longitude: -88.0817 },
                'naperville': { latitude: 41.7508, longitude: -88.1535 },
                'springfield': { latitude: 39.7817, longitude: -89.6501 },
                'peoria': { latitude: 40.6936, longitude: -89.5890 },
                'elgin': { latitude: 42.0354, longitude: -88.2826 },
                'waukegan': { latitude: 42.3636, longitude: -87.8448 },
                'cicero': { latitude: 41.8456, longitude: -87.7539 }
            }
        };
        
        if (cityDatabase[stateKey] && cityDatabase[stateKey][cityName]) {
            return cityDatabase[stateKey][cityName];
        }
        
        return null;
    }

    // Get state center coordinates for better fallback
    getStateCenterCoordinates(state) {
        const stateCenters = {
            'texas': { latitude: 31.9686, longitude: -99.9018 },
            'california': { latitude: 36.7783, longitude: -119.4179 },
            'florida': { latitude: 27.6648, longitude: -81.5158 },
            'new york': { latitude: 40.7589, longitude: -73.9851 },
            'illinois': { latitude: 40.6331, longitude: -89.3985 },
            'pennsylvania': { latitude: 41.2033, longitude: -77.1945 },
            'ohio': { latitude: 40.4173, longitude: -82.9071 },
            'georgia': { latitude: 32.1656, longitude: -82.9001 },
            'north carolina': { latitude: 35.7796, longitude: -78.6382 },
            'michigan': { latitude: 44.3148, longitude: -85.6024 },
            'new jersey': { latitude: 40.0583, longitude: -74.4057 },
            'virginia': { latitude: 37.4316, longitude: -78.6569 },
            'washington': { latitude: 47.7511, longitude: -120.7401 },
            'arizona': { latitude: 34.0489, longitude: -111.0937 },
            'massachusetts': { latitude: 42.4072, longitude: -71.3824 },
            'tennessee': { latitude: 35.5175, longitude: -86.5804 },
            'indiana': { latitude: 40.2732, longitude: -86.1349 },
            'missouri': { latitude: 37.9643, longitude: -91.8318 },
            'maryland': { latitude: 39.0458, longitude: -76.6413 },
            'wisconsin': { latitude: 43.7844, longitude: -88.7879 },
            'colorado': { latitude: 39.5501, longitude: -105.7821 },
            'minnesota': { latitude: 46.7296, longitude: -94.6859 },
            'south carolina': { latitude: 33.8361, longitude: -81.1637 },
            'alabama': { latitude: 32.3617, longitude: -86.2792 },
            'louisiana': { latitude: 30.9843, longitude: -91.9623 },
            'kentucky': { latitude: 37.8393, longitude: -84.2700 },
            'oregon': { latitude: 43.8041, longitude: -120.5542 },
            'oklahoma': { latitude: 35.0078, longitude: -97.0929 },
            'connecticut': { latitude: 41.6032, longitude: -73.0877 },
            'utah': { latitude: 39.3210, longitude: -111.0937 },
            'iowa': { latitude: 42.0751, longitude: -93.4960 },
            'nevada': { latitude: 38.8026, longitude: -116.4194 },
            'arkansas': { latitude: 35.2010, longitude: -91.8318 },
            'mississippi': { latitude: 32.3547, longitude: -89.3985 },
            'kansas': { latitude: 39.0119, longitude: -98.4842 },
            'new mexico': { latitude: 34.5199, longitude: -105.8701 },
            'nebraska': { latitude: 41.4925, longitude: -99.9018 },
            'west virginia': { latitude: 38.5976, longitude: -80.4549 },
            'idaho': { latitude: 44.0682, longitude: -114.7420 },
            'hawaii': { latitude: 19.8968, longitude: -155.5828 },
            'new hampshire': { latitude: 43.1939, longitude: -71.5724 },
            'maine': { latitude: 45.2538, longitude: -69.4455 },
            'montana': { latitude: 47.0527, longitude: -109.6333 },
            'rhode island': { latitude: 41.5801, longitude: -71.4774 },
            'delaware': { latitude: 38.9108, longitude: -75.5277 },
            'south dakota': { latitude: 43.9695, longitude: -99.9018 },
            'north dakota': { latitude: 47.5515, longitude: -101.0020 },
            'alaska': { latitude: 64.0685, longitude: -152.2782 },
            'vermont': { latitude: 44.2601, longitude: -72.5806 },
            'wyoming': { latitude: 43.0759, longitude: -107.2903 }
        };
        
        return stateCenters[state.toLowerCase()] || null;
    }

    getZipCodeCoordinates(zipCode) {
        // Database of major ZIP codes with coordinates
        // This provides better geocoding for common ZIP codes
        const zipDatabase = {
            // Major Cities - California
            '90210': { latitude: 34.0901, longitude: -118.4065 }, // Beverly Hills
            '90211': { latitude: 34.0668, longitude: -118.3744 }, // Beverly Hills
            '90028': { latitude: 34.1016, longitude: -118.3267 }, // Hollywood
            '90212': { latitude: 34.0836, longitude: -118.3967 }, // Beverly Hills
            '90213': { latitude: 34.0668, longitude: -118.3744 }, // Beverly Hills
            '90401': { latitude: 34.0195, longitude: -118.4912 }, // Santa Monica
            '94102': { latitude: 37.7849, longitude: -122.4094 }, // San Francisco
            '94103': { latitude: 37.7716, longitude: -122.4108 }, // San Francisco
            '94110': { latitude: 37.7484, longitude: -122.4156 }, // San Francisco
            '94111': { latitude: 37.7983, longitude: -122.4015 }, // San Francisco
            '10001': { latitude: 40.7505, longitude: -73.9971 }, // NYC - Manhattan
            '10002': { latitude: 40.7156, longitude: -73.9881 }, // NYC - Lower East Side
            '10003': { latitude: 40.7318, longitude: -73.9888 }, // NYC - East Village
            '10011': { latitude: 40.7411, longitude: -74.0015 }, // NYC - Chelsea
            '10012': { latitude: 40.7255, longitude: -73.9983 }, // NYC - SoHo
            '10014': { latitude: 40.7342, longitude: -74.0063 }, // NYC - West Village
            '10016': { latitude: 40.7452, longitude: -73.9740 }, // NYC - Murray Hill
            '10017': { latitude: 40.7527, longitude: -73.9731 }, // NYC - Midtown East
            '10018': { latitude: 40.7549, longitude: -73.9926 }, // NYC - Garment District
            '10019': { latitude: 40.7656, longitude: -73.9863 }, // NYC - Hell's Kitchen
            '10021': { latitude: 40.7648, longitude: -73.9626 }, // NYC - Upper East Side
            '10022': { latitude: 40.7589, longitude: -73.9658 }, // NYC - Midtown East
            '10023': { latitude: 40.7756, longitude: -73.9805 }, // NYC - Upper West Side
            '10024': { latitude: 40.7993, longitude: -73.9738 }, // NYC - Upper West Side
            '10025': { latitude: 40.7957, longitude: -73.9667 }, // NYC - Upper West Side
            '10026': { latitude: 40.8019, longitude: -73.9538 }, // NYC - Harlem
            '10027': { latitude: 40.8115, longitude: -73.9533 }, // NYC - Harlem
            '10028': { latitude: 40.7761, longitude: -73.9536 }, // NYC - Upper East Side
            '60601': { latitude: 41.8825, longitude: -87.6388 }, // Chicago - Loop
            '60602': { latitude: 41.8796, longitude: -87.6307 }, // Chicago - Loop
            '60603': { latitude: 41.8781, longitude: -87.6298 }, // Chicago - Loop
            '60604': { latitude: 41.8781, longitude: -87.6298 }, // Chicago - Loop
            '60605': { latitude: 41.8708, longitude: -87.6245 }, // Chicago - South Loop
            '60606': { latitude: 41.8825, longitude: -87.6388 }, // Chicago - Loop
            '60607': { latitude: 41.8748, longitude: -87.6513 }, // Chicago - West Loop
            '60610': { latitude: 41.8982, longitude: -87.6324 }, // Chicago - Near North Side
            '60611': { latitude: 41.8955, longitude: -87.6244 }, // Chicago - Near North Side
            '60614': { latitude: 41.9248, longitude: -87.6487 }, // Chicago - Lincoln Park
            '77001': { latitude: 29.7472, longitude: -95.3816 }, // Houston - Downtown
            '77002': { latitude: 29.7604, longitude: -95.3698 }, // Houston - Downtown
            '77003': { latitude: 29.7424, longitude: -95.3507 }, // Houston - Third Ward
            '77004': { latitude: 29.7199, longitude: -95.3896 }, // Houston - Museum District
            '77005': { latitude: 29.7199, longitude: -95.4077 }, // Houston - Rice University
            '77006': { latitude: 29.7328, longitude: -95.4009 }, // Houston - Montrose
            '77007': { latitude: 29.7805, longitude: -95.3863 }, // Houston - Heights
            '19101': { latitude: 39.9526, longitude: -75.1652 }, // Philadelphia - Center City
            '19102': { latitude: 39.9526, longitude: -75.1652 }, // Philadelphia - Center City
            '19103': { latitude: 39.9526, longitude: -75.1652 }, // Philadelphia - Center City
            '19104': { latitude: 39.9619, longitude: -75.1963 }, // Philadelphia - University City
            '19106': { latitude: 39.9548, longitude: -75.1456 }, // Philadelphia - Old City
            '19107': { latitude: 39.9446, longitude: -75.1588 }, // Philadelphia - Society Hill
            '33101': { latitude: 25.7617, longitude: -80.1918 }, // Miami - Downtown
            '33102': { latitude: 25.7617, longitude: -80.1918 }, // Miami - Downtown
            '33109': { latitude: 25.7933, longitude: -80.1420 }, // Miami Beach
            '33139': { latitude: 25.7743, longitude: -80.1342 }, // Miami Beach - South Beach
            '33141': { latitude: 25.8676, longitude: -80.1234 }, // Miami Beach - North Beach
            '30301': { latitude: 33.7590, longitude: -84.3880 }, // Atlanta - Downtown
            '30302': { latitude: 33.7490, longitude: -84.3880 }, // Atlanta - Downtown
            '30303': { latitude: 33.7590, longitude: -84.3880 }, // Atlanta - Downtown
            '30309': { latitude: 33.7831, longitude: -84.3831 }, // Atlanta - Midtown
            '80202': { latitude: 39.7392, longitude: -104.9903 }, // Denver - Downtown
            '80203': { latitude: 39.7391, longitude: -104.9847 }, // Denver - Capitol Hill
            '80204': { latitude: 39.7392, longitude: -104.9903 }, // Denver - Downtown
            '80205': { latitude: 39.7392, longitude: -104.9903 }, // Denver - Five Points
            '80206': { latitude: 39.7392, longitude: -104.9552 }, // Denver - Cherry Creek
            '80209': { latitude: 39.7084, longitude: -104.9536 }, // Denver - Glendale
            '80210': { latitude: 39.6934, longitude: -104.9378 }, // Denver - Cherry Hills
            '80211': { latitude: 39.7817, longitude: -105.0178 }, // Denver - Regis
            '80212': { latitude: 39.7817, longitude: -105.0178 }, // Denver - Regis
            '80218': { latitude: 39.7186, longitude: -104.9492 }, // Denver - Congress Park
            '80220': { latitude: 39.7348, longitude: -104.9056 }, // Denver - Lowry
            '80221': { latitude: 39.8361, longitude: -105.0178 }, // Westminster
            '80222': { latitude: 39.6934, longitude: -104.9378 }, // Denver - Cherry Hills
            '80223': { latitude: 39.6934, longitude: -104.9378 }, // Denver - Glendale
            '80224': { latitude: 39.6720, longitude: -104.9036 }, // Denver - Glendale
            '80020': { latitude: 39.9205, longitude: -105.0866 }, // Broomfield, CO
            '80226': { latitude: 39.6720, longitude: -104.9036 }, // Lakewood
            '98101': { latitude: 47.6062, longitude: -122.3321 }, // Seattle - Downtown
            '98102': { latitude: 47.6249, longitude: -122.3207 }, // Seattle - Capitol Hill
            '98103': { latitude: 47.6694, longitude: -122.3417 }, // Seattle - Fremont
            '98104': { latitude: 47.6062, longitude: -122.3321 }, // Seattle - Downtown
            '98105': { latitude: 47.6694, longitude: -122.3017 }, // Seattle - University District
            '98106': { latitude: 47.5218, longitude: -122.3515 }, // Seattle - White Center
            '98107': { latitude: 47.6694, longitude: -122.3750 }, // Seattle - Ballard
            '98108': { latitude: 47.5218, longitude: -122.3181 }, // Seattle - Georgetown
            '98109': { latitude: 47.6231, longitude: -122.3510 }, // Seattle - South Lake Union
            '98110': { latitude: 47.6297, longitude: -122.5326 }, // Bainbridge Island
            '98111': { latitude: 47.6062, longitude: -122.3321 }, // Seattle - Downtown
            '98112': { latitude: 47.6249, longitude: -122.3017 }, // Seattle - Capitol Hill
            '98115': { latitude: 47.6908, longitude: -122.3017 }, // Seattle - Northgate
            '98116': { latitude: 47.5657, longitude: -122.3968 }, // Seattle - West Seattle
            '98117': { latitude: 47.6908, longitude: -122.3750 }, // Seattle - Ballard
            '98118': { latitude: 47.5355, longitude: -122.2513 }, // Seattle - Rainier Valley
            '98119': { latitude: 47.6231, longitude: -122.3510 }, // Seattle - Interbay
            '85001': { latitude: 33.4484, longitude: -112.0740 }, // Phoenix - Downtown
            '85002': { latitude: 33.4734, longitude: -112.0879 }, // Phoenix - Midtown
            '85003': { latitude: 33.4484, longitude: -112.0740 }, // Phoenix - Downtown
            '85004': { latitude: 33.4734, longitude: -112.0879 }, // Phoenix - Midtown
            '85006': { latitude: 33.4734, longitude: -112.0879 }, // Phoenix - Midtown
            '85007': { latitude: 33.4734, longitude: -112.0879 }, // Phoenix - Laveen
            '85008': { latitude: 33.4152, longitude: -112.0879 }, // Phoenix - Ahwatukee
            '85009': { latitude: 33.4734, longitude: -112.1168 }, // Phoenix - Maryvale
            '85012': { latitude: 33.4734, longitude: -112.0740 }, // Phoenix - Central
            '85013': { latitude: 33.4734, longitude: -112.1168 }, // Phoenix - Maryvale
            '85014': { latitude: 33.4734, longitude: -112.0451 }, // Phoenix - Biltmore
            '85015': { latitude: 33.4734, longitude: -112.0451 }, // Phoenix - Ahwatukee
            '85016': { latitude: 33.4734, longitude: -112.0451 }, // Phoenix - Ahwatukee
            '85017': { latitude: 33.4734, longitude: -112.1168 }, // Phoenix - Maryvale
            '85018': { latitude: 33.4152, longitude: -112.0451 }, // Phoenix - Ahwatukee
            '85020': { latitude: 33.4152, longitude: -112.0451 }, // Phoenix - Ahwatukee
            '85021': { latitude: 33.5347, longitude: -112.1168 }, // Phoenix - North Mountain
            '85022': { latitude: 33.5994, longitude: -112.0740 }, // Phoenix - North Phoenix
            '85023': { latitude: 33.4734, longitude: -112.1457 }, // Phoenix - Maryvale
            '85024': { latitude: 33.4152, longitude: -112.0162 }, // Phoenix - Ahwatukee
            '85027': { latitude: 33.4152, longitude: -112.0451 }, // Phoenix - Ahwatukee
            '85028': { latitude: 33.4152, longitude: -112.0162 }, // Phoenix - Ahwatukee
            '85029': { latitude: 33.5994, longitude: -112.1457 }, // Phoenix - North Phoenix
            '85032': { latitude: 33.3918, longitude: -112.0162 }, // Phoenix - Ahwatukee
            '85033': { latitude: 33.4734, longitude: -112.1457 }, // Phoenix - Laveen
            '85034': { latitude: 33.4152, longitude: -112.0740 }, // Phoenix - Ahwatukee
            '85035': { latitude: 33.4152, longitude: -112.1168 }, // Phoenix - Laveen
            '85037': { latitude: 33.4734, longitude: -112.1746 }, // Phoenix - Laveen
            '85040': { latitude: 33.4152, longitude: -112.0451 }, // Phoenix - Ahwatukee
            '85041': { latitude: 33.3918, longitude: -112.0451 }, // Phoenix - Ahwatukee
            '85042': { latitude: 33.3918, longitude: -112.0162 }, // Phoenix - Ahwatukee
            '85043': { latitude: 33.4152, longitude: -112.1168 }, // Phoenix - Laveen
            '85044': { latitude: 33.3918, longitude: -112.0162 }, // Phoenix - Ahwatukee
            '85045': { latitude: 33.3918, longitude: -112.0451 }, // Phoenix - Ahwatukee
            '85048': { latitude: 33.3918, longitude: -112.0162 }, // Phoenix - Ahwatukee
            '85050': { latitude: 33.3918, longitude: -112.0162 }, // Phoenix - Ahwatukee
            '85051': { latitude: 33.4734, longitude: -112.1746 }, // Phoenix - Laveen
            
            // Additional Major Metropolitan Areas
            // Boston Area
            '02101': { latitude: 42.3601, longitude: -71.0589 }, // Boston - Downtown
            '02114': { latitude: 42.3601, longitude: -71.0656 }, // Boston - Beacon Hill
            '02115': { latitude: 42.3467, longitude: -71.0872 }, // Boston - Back Bay
            '02134': { latitude: 42.3534, longitude: -71.1311 }, // Boston - Allston
            '02135': { latitude: 42.3534, longitude: -71.1311 }, // Boston - Brighton
            '02155': { latitude: 42.4184, longitude: -71.1061 }, // Medford
            
            // Atlanta Area
            '30301': { latitude: 33.7590, longitude: -84.3880 }, // Atlanta - Downtown
            '30303': { latitude: 33.7590, longitude: -84.3880 }, // Atlanta - Downtown
            '30309': { latitude: 33.7831, longitude: -84.3831 }, // Atlanta - Midtown
            '30318': { latitude: 33.7831, longitude: -84.4277 }, // Atlanta - Northwest
            '30324': { latitude: 33.8207, longitude: -84.3733 }, // Atlanta - Buckhead
            '30327': { latitude: 33.8431, longitude: -84.3733 }, // Atlanta - Buckhead
            
            // Dallas Area
            '75201': { latitude: 32.7767, longitude: -96.7970 }, // Dallas - Downtown
            '75202': { latitude: 32.7767, longitude: -96.7970 }, // Dallas - Downtown
            '75204': { latitude: 32.7767, longitude: -96.7970 }, // Dallas - Deep Ellum
            '75218': { latitude: 32.8207, longitude: -96.7970 }, // Dallas - Lakewood
            '75230': { latitude: 32.9207, longitude: -96.7670 }, // Dallas - North
            
            // Richardson Area
            '75080': { latitude: 32.9483, longitude: -96.7299 }, // Richardson - Southwest
            '75081': { latitude: 32.9483, longitude: -96.7299 }, // Richardson - Southeast
            '75082': { latitude: 32.9483, longitude: -96.7299 }, // Richardson - Northeast
            '75083': { latitude: 32.9483, longitude: -96.7299 }, // Richardson - Northwest
            '75085': { latitude: 32.9483, longitude: -96.7299 }, // Richardson - Central
            
            // Portland Area
            '97201': { latitude: 45.5152, longitude: -122.6784 }, // Portland - Downtown
            '97202': { latitude: 45.4642, longitude: -122.6648 }, // Portland - Southeast
            '97205': { latitude: 45.5152, longitude: -122.6927 }, // Portland - Northwest
            '97210': { latitude: 45.5376, longitude: -122.6927 }, // Portland - Pearl District
            '97214': { latitude: 45.5376, longitude: -122.6648 }, // Portland - Southeast
            
            // Las Vegas Area
            '89101': { latitude: 36.1699, longitude: -115.1398 }, // Las Vegas - Downtown
            '89102': { latitude: 36.1215, longitude: -115.1739 }, // Las Vegas - West
            '89103': { latitude: 36.1316, longitude: -115.1754 }, // Las Vegas - Southwest
            '89104': { latitude: 36.1699, longitude: -115.1398 }, // Las Vegas - Downtown
            '89109': { latitude: 36.1146, longitude: -115.1722 }, // Las Vegas - Strip
            '89110': { latitude: 36.1316, longitude: -115.0755 }, // Las Vegas - East
            '89117': { latitude: 36.1316, longitude: -115.2606 }, // Las Vegas - West
            '89119': { latitude: 36.0731, longitude: -115.1372 }, // Las Vegas - Southwest
            '89123': { latitude: 36.0731, longitude: -115.1372 }, // Las Vegas - Southwest
            '89128': { latitude: 36.1905, longitude: -115.2606 }, // Las Vegas - Northwest
            '89129': { latitude: 36.1905, longitude: -115.2606 }, // Las Vegas - Northwest
            '89134': { latitude: 36.1905, longitude: -115.3606 }, // Las Vegas - Summerlin
            '89135': { latitude: 36.1905, longitude: -115.3606 }, // Las Vegas - Summerlin
            
            // New Jersey Major ZIPs (fixing the previous issues)
            '08002': { latitude: 39.9343, longitude: -75.0379 }, // Cherry Hill
            '08021': { latitude: 39.7137, longitude: -75.1379 }, // Moorestown
            '08028': { latitude: 39.7029, longitude: -75.1118 }, // Glassboro
            '08052': { latitude: 39.8929, longitude: -75.0118 }, // Marlton
            '08077': { latitude: 39.8529, longitude: -74.9718 }, // Riverton
            '08096': { latitude: 39.7429, longitude: -75.0318 }, // Deptford
            '08109': { latitude: 39.9229, longitude: -75.0818 }, // Merchantville
            '08234': { latitude: 39.3729, longitude: -74.4518 }, // Pleasantville
            
            // Connecticut Major ZIPs
            '06040': { latitude: 41.7729, longitude: -72.6018 }, // Manchester
            '06457': { latitude: 41.5529, longitude: -72.5518 }, // Middletown
            
            // Vermont Major ZIPs
            '05401': { latitude: 44.4759, longitude: -73.2121 }, // Burlington
            '05701': { latitude: 43.6106, longitude: -72.9726 }, // Rutland
            
            // Maine Major ZIPs
            '04106': { latitude: 43.6591, longitude: -70.3178 }, // South Portland
            '04240': { latitude: 44.0959, longitude: -70.2178 }, // Lewiston
            '04412': { latitude: 44.8259, longitude: -68.7778 }, // Bangor
        };

        return zipDatabase[zipCode] || null;
    }

    async searchNearbyCenter(coords) {
        const { latitude, longitude } = coords;
        const radius = this.filters.distance;
        
        // Use local data instead of API
        const allCenters = this.allCenters;
        
        // Calculate distances and filter by radius
        const centersWithDistance = allCenters.map(center => ({
            ...center,
            distance: this.calculateDistance(latitude, longitude, center.latitude, center.longitude)
        })).filter(center => center.distance <= radius)
          .sort((a, b) => a.distance - b.distance)
          .slice(0, this.pageSize);
        
        this.centers = centersWithDistance;
        this.filteredCenters = [...this.centers];
        this.displayCenters();
        this.updateResultsInfo(`Found ${this.centers.length} centers within ${radius} miles`);
    }

    async searchByText(location) {
        console.log('🔍 === STARTING SEARCH ===');
        console.log('🔍 Searching locally for:', location);
        
        // Reset pagination and set search mode
        this.currentPage = 0;
        this.lastSearchQuery = location;
        this.isSearchMode = true;
        console.log('🔍 Search mode set, pagination reset');
        
        // Use the loaded center data (from JSON or hardcoded fallback)
        console.log('🔍 Getting loaded centers...');
        console.log('🔍 this.allCenters is:', this.allCenters);
        console.log('🔍 this.allCenters type:', typeof this.allCenters);
        console.log('🔍 this.allCenters length:', this.allCenters?.length);
        
        let allCenters = this.allCenters;
        
        if (!allCenters || allCenters.length === 0) {
            console.error('❌ No centers found! Using hardcoded fallback...');
            allCenters = this.getHardcodedCenters();
            console.log('📊 Using', allCenters.length, 'fallback centers');
        }
        
        console.log('📊 Got', allCenters.length, 'centers from loaded data');
        
        // Debug: Check if 80020 is in the data
        const zip80020 = allCenters.find(center => center.postal_code === '80020');
        console.log('🔍 ZIP 80020 center found:', zip80020 ? zip80020.name : 'NOT FOUND');
        
        // Debug: Show all ZIP codes in data
        const allZips = allCenters.map(c => c.postal_code).join(', ');
        console.log('🔍 All ZIP codes in data:', allZips);
        
        // Search logic - match ZIP code, city, or state
        const searchTerm = location.toLowerCase();
        let matchedCenters = [];
        console.log('🔍 Starting search logic for term:', searchTerm);
        
        // If it's a ZIP code search, find exact matches and nearby ZIP codes
        if (/^\d{5}$/.test(location)) {
            console.log('🔍 ZIP code search for:', location);
            
            // First, try exact ZIP match
            matchedCenters = allCenters.filter(center => center.postal_code === location);
            console.log('📍 Exact ZIP matches:', matchedCenters.length);
            
            // If no exact match, find by ZIP coordinates and sort by distance
            if (matchedCenters.length === 0) {
                console.log('🌍 No exact ZIP match, trying geocoding and distance-based search...');
                
                try {
                    // Try to get coordinates for the ZIP code
                    const coords = await this.geocodeLocation(location);
                    
                    if (coords) {
                        console.log('📍 Got coordinates for ZIP', location, ':', coords);
                        console.log('📍 Coordinates source: ZIP database lookup successful');
                        
                        // Find all centers and calculate distances
                        const centersWithDistance = allCenters.map(center => {
                            if (!center.latitude || !center.longitude) return null;
                            
                            const distance = this.calculateDistance(
                                coords.latitude, coords.longitude,
                                center.latitude, center.longitude
                            );
                            
                            return { ...center, distance };
                        }).filter(center => center && center.distance <= 100) // 100 mile radius for ZIP searches
                          .sort((a, b) => a.distance - b.distance)
                          .slice(0, 30); // Limit to 30 closest results
                        
                        matchedCenters = centersWithDistance;
                        console.log(`🎯 Found ${matchedCenters.length} centers within 100 miles of ZIP ${location}, sorted by distance`);
                        
                        if (matchedCenters.length > 0) {
                            console.log('📍 Closest centers to ZIP', location, ':');
                            matchedCenters.slice(0, 5).forEach((center, i) => {
                                console.log(`${i + 1}. ${center.name} - ${center.city}, ${center.state} (${center.distance.toFixed(1)} miles)`);
                            });
                        }
                    } else {
                        // Fallback to state-based search if geocoding fails
                        console.log('⚠️ Geocoding failed, falling back to state-based search');
                        
                        // Comprehensive ZIP to state mapping for ALL 50 states
                        const getStateFromZip = (zipCode) => {
                            const zip = parseInt(zipCode);
                            
                            // Northeast
                            if (zip >= 1000 && zip <= 2799) return "Massachusetts";
                            if (zip >= 2800 && zip <= 2999) return "Rhode Island";
                            if (zip >= 3000 && zip <= 3899) return "New Hampshire";
                            if (zip >= 4000 && zip <= 4999) return "Maine";
                            if (zip >= 5000 && zip <= 5999) return "Vermont";
                            if (zip >= 6000 && zip <= 6999) return "Connecticut";
                            if (zip >= 7000 && zip <= 8999) return "New Jersey";
                            if (zip >= 10000 && zip <= 14999) return "New York";
                            if (zip >= 15000 && zip <= 19999) return "Pennsylvania";
                            
                            // Southeast
                            if (zip >= 20000 && zip <= 20599) return "DC";
                            if (zip >= 20600 && zip <= 21999) return "Maryland";
                            if (zip >= 22000 && zip <= 24699) return "Virginia";
                            if (zip >= 24700 && zip <= 26999) return "West Virginia";
                            if (zip >= 27000 && zip <= 28999) return "North Carolina";
                            if (zip >= 29000 && zip <= 29999) return "South Carolina";
                            if (zip >= 30000 && zip <= 31999) return "Georgia";
                            if (zip >= 32000 && zip <= 34999) return "Florida";
                            if (zip >= 35000 && zip <= 36999) return "Alabama";
                            if (zip >= 37000 && zip <= 38599) return "Tennessee";
                            if (zip >= 38600 && zip <= 39999) return "Mississippi";
                            if (zip >= 40000 && zip <= 42999) return "Kentucky";
                            if (zip >= 43000 && zip <= 45999) return "Ohio";
                            if (zip >= 46000 && zip <= 47999) return "Indiana";
                            if (zip >= 48000 && zip <= 49999) return "Michigan";
                            
                            // Midwest
                            if (zip >= 50000 && zip <= 52999) return "Iowa";
                            if (zip >= 53000 && zip <= 54999) return "Wisconsin";
                            if (zip >= 55000 && zip <= 56999) return "Minnesota";
                            if (zip >= 57000 && zip <= 57999) return "South Dakota";
                            if (zip >= 58000 && zip <= 58999) return "North Dakota";
                            if (zip >= 59000 && zip <= 59999) return "Montana";
                            if (zip >= 60000 && zip <= 62999) return "Illinois";
                            if (zip >= 63000 && zip <= 65999) return "Missouri";
                            if (zip >= 66000 && zip <= 67999) return "Kansas";
                            if (zip >= 68000 && zip <= 69999) return "Nebraska";
                            
                            // South/Southwest
                            if (zip >= 70000 && zip <= 71599) return "Louisiana";
                            if (zip >= 71600 && zip <= 72999) return "Arkansas";
                            if (zip >= 73000 && zip <= 74999) return "Oklahoma";
                            if (zip >= 75000 && zip <= 79999) return "Texas";
                            if (zip >= 80000 && zip <= 81999) return "Colorado";
                            if (zip >= 82000 && zip <= 83199) return "Wyoming";
                            if (zip >= 83200 && zip <= 83999) return "Idaho";
                            if (zip >= 84000 && zip <= 84999) return "Utah";
                            if (zip >= 85000 && zip <= 86999) return "Arizona";
                            if (zip >= 87000 && zip <= 88499) return "New Mexico";
                            if (zip >= 88500 && zip <= 88999) return "Texas";
                            if (zip >= 89000 && zip <= 89999) return "Nevada";
                            if (zip >= 90000 && zip <= 96199) return "California";
                            if (zip >= 96700 && zip <= 96999) return "Hawaii";
                            if (zip >= 97000 && zip <= 97999) return "Oregon";
                            if (zip >= 98000 && zip <= 99999) return "Washington";
                            
                            // Alaska
                            if (zip >= 99500 && zip <= 99999) return "Alaska";
                            
                            return null;
                        };
                        
                        const searchState = getStateFromZip(location);
                        
                        // Enhanced border area detection for ZIP codes
                        const getBorderStatesForZip = (zipCode) => {
                            const zip = parseInt(zipCode);
                            
                            // Philadelphia Metro (19xxx) - PA, NJ, DE
                            if (zipCode.startsWith('19')) return ['PA', 'NJ', 'DE'];
                            
                            // NYC Metro - NY, NJ, CT
                            if (zipCode.startsWith('10') || zipCode.startsWith('11') || 
                                zipCode.startsWith('07') || zipCode.startsWith('06')) return ['NY', 'NJ', 'CT'];
                            
                            // DC Metro - DC, MD, VA
                            if (zipCode.startsWith('20') || zipCode.startsWith('21') || 
                                zipCode.startsWith('22')) return ['DC', 'MD', 'VA'];
                            
                            // Chicago Metro - IL, IN, WI
                            if (zipCode.startsWith('60') || zipCode.startsWith('46') || 
                                zipCode.startsWith('53')) return ['IL', 'IN', 'WI'];
                            
                            // Kansas City Metro - MO, KS
                            if (zip >= 64000 && zip <= 66999) return ['MO', 'KS'];
                            
                            // St. Louis Metro - MO, IL
                            if (zip >= 63000 && zip <= 63999) return ['MO', 'IL'];
                            
                            // Cincinnati Metro - OH, KY, IN
                            if (zip >= 45000 && zip <= 45999) return ['OH', 'KY', 'IN'];
                            
                            // Memphis Metro - TN, AR, MS
                            if (zip >= 38000 && zip <= 38999) return ['TN', 'AR', 'MS'];
                            
                            // Portland Metro - OR, WA
                            if (zip >= 97000 && zip <= 97999) return ['OR', 'WA'];
                            
                            // Providence Metro - RI, MA
                            if (zipCode.startsWith('02')) return ['RI', 'MA'];
                            
                            return null;
                        };
                        
                        const borderStates = getBorderStatesForZip(location);
                        const states = borderStates || [searchState].filter(Boolean);
                        
                        console.log('🗺️ ZIP', location, 'mapped to states:', states);
                        
                        if (states.length > 0) {
                            matchedCenters = allCenters.filter(center => states.includes(center.state));
                            console.log('🏛️ State matches found for', states, ':', matchedCenters.length);
                            
                            // Log the first few centers to verify correct state
                            if (matchedCenters.length > 0) {
                                console.log('🏛️ Sample state centers:');
                                matchedCenters.slice(0, 3).forEach((center, i) => {
                                    console.log(`${i + 1}. ${center.name} - ${center.city}, ${center.state}`);
                                });
                            }
                        }
                        
                        // If still no results, try ZIP prefix (first 3 digits)
                        if (matchedCenters.length === 0) {
                            const zipPrefix = location.substring(0, 3);
                            matchedCenters = allCenters.filter(center => 
                                center.postal_code && center.postal_code.startsWith(zipPrefix)
                            );
                            console.log('📮 ZIP prefix', zipPrefix, 'matches:', matchedCenters.length);
                        }
                    }
                } catch (geocodeError) {
                    console.log('⚠️ Geocoding error:', geocodeError);
                    // Fallback to state-based search
                    // [Same state-based fallback code as above would go here]
                }
            }
        } else {
            // City or state search
            console.log('🏙️ City/state search for:', searchTerm);
            console.log('🏙️ Sample cities in data:', allCenters.slice(0, 5).map(c => c.city));
            
            // Enhanced city search including cross-border areas
            const getBorderStatesForCity = (cityName) => {
                const borderCities = {
                    'philadelphia': ['PA', 'NJ', 'DE'], // Philly metro area
                    'new york': ['NY', 'NJ', 'CT'], // NYC metro area
                    'washington': ['DC', 'MD', 'VA'], // DC metro area
                    'chicago': ['IL', 'IN', 'WI'], // Chicago metro area
                    'kansas city': ['MO', 'KS'], // KC metro area
                    'memphis': ['TN', 'AR', 'MS'], // Memphis metro area
                    'cincinnati': ['OH', 'KY', 'IN'], // Cincinnati metro area
                    'louisville': ['KY', 'IN'], // Louisville metro area
                    'st louis': ['MO', 'IL'], // St. Louis metro area
                    'texarkana': ['TX', 'AR'], // Texarkana area
                    'el paso': ['TX', 'NM'], // El Paso area
                    'portland': ['OR', 'WA'], // Portland metro area
                    'bristol': ['TN', 'VA'], // Bristol twin cities
                    'augusta': ['GA', 'SC'], // Augusta metro area
                    'chattanooga': ['TN', 'GA'], // Chattanooga area
                    'providence': ['RI', 'MA'], // Providence metro area
                    'omaha': ['NE', 'IA'], // Omaha metro area
                    'davenport': ['IA', 'IL'], // Quad Cities
                    'rock island': ['IL', 'IA'], // Quad Cities
                    'moline': ['IL', 'IA'], // Quad Cities
                    'bettendorf': ['IA', 'IL'], // Quad Cities
                    'dallas': ['TX'], // Dallas metro area
                    'richardson': ['TX'], // Richardson is part of Dallas metro
                    'plano': ['TX'], // Plano is part of Dallas metro  
                    'garland': ['TX'], // Garland is part of Dallas metro
                    'irving': ['TX'], // Irving is part of Dallas metro
                    'mesquite': ['TX'], // Mesquite is part of Dallas metro
                    'carrollton': ['TX'], // Carrollton is part of Dallas metro
                    'fort worth': ['TX'], // Fort Worth metro area
                };
                
                return borderCities[cityName.toLowerCase()] || null;
            };
            
            const borderStates = getBorderStatesForCity(searchTerm);
            
            // First try exact city/state/name matches
            matchedCenters = allCenters.filter(center => {
                // Add null checks for safety
                const city = center.city || '';
                const state = center.state || '';
                const name = center.name || '';
                
                const cityMatch = city.toLowerCase().includes(searchTerm);
                const stateMatch = state.toLowerCase().includes(searchTerm);
                const nameMatch = name.toLowerCase().includes(searchTerm);
                
                // For border cities, also include centers from neighboring states
                let borderMatch = false;
                if (borderStates && cityMatch) {
                    borderMatch = borderStates.includes(center.state);
                }
                
                if (cityMatch || stateMatch || nameMatch || borderMatch) {
                    console.log(`✅ Match found: ${name} - ${city}, ${state}${borderMatch ? ' (border area)' : ''}`);
                }
                
                return cityMatch || stateMatch || nameMatch || borderMatch;
            });
            
            // If we found a border city, also search nearby metros
            if (borderStates && matchedCenters.length > 0) {
                console.log(`🌉 Border city detected for ${searchTerm}, including ${borderStates.join(', ')} states`);
                
                // Add centers from all border states within reasonable distance
                const additionalCenters = allCenters.filter(center => {
                    const state = center.state || '';
                    return borderStates.includes(state) && !matchedCenters.find(mc => mc.id === center.id);
                });
                
                console.log(`🌉 Added ${additionalCenters.length} additional centers from border states`);
                matchedCenters = [...matchedCenters, ...additionalCenters];
            }
            
            console.log('🏙️ City/state search complete, found:', matchedCenters.length);
            
            // If no direct matches, try geographic proximity search for small cities
            if (matchedCenters.length === 0) {
                console.log('🌍 No direct matches, trying geographic proximity search...');
                
                try {
                    const coords = await this.geocodeLocation(location);
                    if (coords) {
                        console.log('📍 Got coordinates for', location, ':', coords);
                        
                        // Find centers within 100 miles first
                        let centersWithDistance = allCenters.map(center => {
                            if (!center.latitude || !center.longitude) return null;
                            
                            const distance = this.calculateDistance(
                                coords.latitude, coords.longitude,
                                center.latitude, center.longitude
                            );
                            
                            return { ...center, distance };
                        }).filter(center => center && center.distance <= 100)
                          .sort((a, b) => a.distance - b.distance);
                        
                        // If no centers within 100 miles, expand to 200 miles
                        if (centersWithDistance.length === 0) {
                            console.log('🌍 No centers within 100 miles, expanding to 200 miles...');
                            centersWithDistance = allCenters.map(center => {
                                if (!center.latitude || !center.longitude) return null;
                                
                                const distance = this.calculateDistance(
                                    coords.latitude, coords.longitude,
                                    center.latitude, center.longitude
                                );
                                
                                return { ...center, distance };
                            }).filter(center => center && center.distance <= 200)
                              .sort((a, b) => a.distance - b.distance);
                        }
                        
                        // If still no centers, show all centers with distance
                        if (centersWithDistance.length === 0) {
                            console.log('🌍 No centers within 200 miles, showing all centers with distance...');
                            centersWithDistance = allCenters.map(center => {
                                if (!center.latitude || !center.longitude) return null;
                                
                                const distance = this.calculateDistance(
                                    coords.latitude, coords.longitude,
                                    center.latitude, center.longitude
                                );
                                
                                return { ...center, distance };
                            }).filter(center => center !== null)
                              .sort((a, b) => a.distance - b.distance);
                        }
                        
                        matchedCenters = centersWithDistance;
                        const searchRadius = centersWithDistance.length > 0 ? 
                            (centersWithDistance[centersWithDistance.length - 1].distance <= 100 ? '100' : 
                             centersWithDistance[centersWithDistance.length - 1].distance <= 200 ? '200' : 'unlimited') : 'unlimited';
                        
                        console.log(`🌍 Found ${matchedCenters.length} centers within ${searchRadius} miles of ${location}`);
                        
                        if (matchedCenters.length > 0) {
                            console.log('📍 Closest centers:');
                            matchedCenters.slice(0, 3).forEach((center, i) => {
                                console.log(`${i + 1}. ${center.name} - ${center.city}, ${center.state} (${center.distance.toFixed(1)} miles)`);
                            });
                        }
                    }
                } catch (error) {
                    console.log('⚠️ Geocoding failed:', error);
                    // Fallback: if geocoding fails, show message about adding state
                    if (!/,?\s*[a-z]{2}$/i.test(location) && location.split(' ').length <= 2) {
                        console.log('💡 City without state detected, suggesting state addition');
                        // This will be handled in the no results display
                    }
                }
            }
        }
        
        console.log('📊 Found', matchedCenters.length, 'centers');
        
        // Log first few centers for debugging
        if (matchedCenters.length > 0) {
            console.log('📊 Sample matched centers:');
            matchedCenters.slice(0, 3).forEach((center, index) => {
                console.log(`${index + 1}. ${center.name} - ${center.city}, ${center.state} (${center.postal_code})`);
            });
        }
        
        try {
            if (matchedCenters.length === 0) {
                console.warn('⚠️ No centers found for:', location);
                this.centers = [];
                this.filteredCenters = [];
                console.log('🔍 Calling displayNoResults...');
                this.displayNoResults(location);
                console.log('🔍 Calling updateResultsInfo...');
                this.updateResultsInfo(`No centers found matching "${location}"`);
                console.log('✅ No results handling completed');
            } else {
                console.log('✅ Found centers, processing results...');
                matchedCenters.forEach((center, index) => {
                    console.log(`${index + 1}. ${center.name} in ${center.city}, ${center.state}`);
                });
                
                this.centers = matchedCenters;
                this.filteredCenters = [...this.centers];
                console.log('🏪 Updated this.centers:', this.centers.length);
                console.log('🔍 Updated this.filteredCenters:', this.filteredCenters.length);
                
                console.log('🔍 Calling displaySearchResults...');
                this.displaySearchResults(matchedCenters);
                
                // Check if this was a ZIP code search or proximity search
                const isZipSearch = /^\d{5}$/.test(location);
                const hasDistanceInfo = matchedCenters.length > 0 && matchedCenters[0].distance !== undefined;
                
                console.log('🔍 Calling updateResultsInfo...');
                if (isZipSearch) {
                    this.updateResultsInfo(`Found ${this.centers.length} centers near ZIP ${location}`);
                } else if (hasDistanceInfo) {
                    const maxDistance = Math.max(...matchedCenters.map(c => c.distance));
                    const radius = maxDistance <= 100 ? 'within 100 miles' : maxDistance <= 200 ? 'within 200 miles' : 'nationwide';
                    this.updateResultsInfo(`Found ${this.centers.length} centers ${radius} of ${location}`);
                } else {
                    this.updateResultsInfo(`Found ${this.centers.length} centers matching "${location}"`);
                }
                console.log('✅ Search results processing completed');
            }
        } catch (displayError) {
            console.error('❌ Error displaying search results:', displayError);
            console.error('❌ Error stack:', displayError.stack);
            // Fallback to showing no results
            this.centers = [];
            this.filteredCenters = [];
            this.displayNoResults(location);
            this.updateResultsInfo(`Search completed but display failed`);
        }
        
        console.log('🔍 === SEARCH COMPLETE ===');
    }

    handleAutocomplete(event) {
        const query = event.target.value.trim();
        
        if (query.length < 2) {
            this.hideAutocomplete();
            return;
        }
        
        const suggestions = this.generateSuggestions(query);
        this.displayAutocomplete(suggestions);
    }

    generateSuggestions(query) {
        const allCenters = this.allCenters;
        const queryLower = query.toLowerCase();
        const suggestions = new Set();
        
        // Add unique cities and states from our center data
        allCenters.forEach(center => {
            // Add null checks for safety
            const city = center.city || '';
            const state = center.state || '';
            const postalCode = center.postal_code || '';
            const cityState = `${city}, ${state}`;
            
            // Skip if essential data is missing
            if (!city || !state) return;
            
            // Match city names
            if (city.toLowerCase().includes(queryLower)) {
                suggestions.add({
                    text: cityState,
                    type: 'city',
                    icon: '🏙️'
                });
            }
            
            // Match state names or abbreviations
            if (state.toLowerCase().includes(queryLower)) {
                suggestions.add({
                    text: state,
                    type: 'state', 
                    icon: '🏛️'
                });
            }
            
            // Match ZIP codes
            if (postalCode && postalCode.startsWith(query)) {
                suggestions.add({
                    text: `${postalCode} - ${city}, ${state}`,
                    type: 'zip',
                    icon: '📍'
                });
            }
        });
        
        // Add common major cities even if not in our data
        const majorCities = [
            'New York, NY', 'Los Angeles, CA', 'Chicago, IL', 'Houston, TX',
            'Philadelphia, PA', 'Phoenix, AZ', 'San Antonio, TX', 'San Diego, CA',
            'Dallas, TX', 'San Jose, CA', 'Austin, TX', 'Jacksonville, FL',
            'Fort Worth, TX', 'Columbus, OH', 'Charlotte, NC', 'San Francisco, CA',
            'Indianapolis, IN', 'Seattle, WA', 'Denver, CO', 'Boston, MA'
        ];
        
        majorCities.forEach(city => {
            if (city.toLowerCase().includes(queryLower)) {
                suggestions.add({
                    text: city,
                    type: 'city',
                    icon: '🏙️'
                });
            }
        });
        
        return Array.from(suggestions).slice(0, 8);
    }

    displayAutocomplete(suggestions) {
        const dropdown = document.getElementById('autocomplete-dropdown');
        
        if (suggestions.length === 0) {
            this.hideAutocomplete();
            return;
        }
        
        dropdown.innerHTML = suggestions.map((suggestion, index) => `
            <div class="autocomplete-item" data-value="${suggestion.text}" data-index="${index}">
                <span class="autocomplete-icon">${suggestion.icon}</span>
                <span class="autocomplete-location">${suggestion.text}</span>
            </div>
        `).join('');
        
        // Add click listeners
        dropdown.querySelectorAll('.autocomplete-item').forEach(item => {
            item.addEventListener('mousedown', (e) => {
                e.preventDefault(); // Prevent blur event
                this.selectSuggestion(item.dataset.value);
            });
        });
        
        dropdown.style.display = 'block';
        this.currentHighlightIndex = -1;
    }

    hideAutocomplete() {
        setTimeout(() => {
            const dropdown = document.getElementById('autocomplete-dropdown');
            if (dropdown) {
                dropdown.style.display = 'none';
            }
            // If dropdown doesn't exist, just ignore
        }, 150);
    }

    selectSuggestion(value) {
        const searchInput = document.getElementById('location-search');
        searchInput.value = value;
        this.hideAutocomplete();
        this.performSearch();
    }

    handleAutocompleteKeydown(event) {
        const dropdown = document.getElementById('autocomplete-dropdown');
        const items = dropdown.querySelectorAll('.autocomplete-item');
        
        if (items.length === 0) return;
        
        switch (event.key) {
            case 'ArrowDown':
                event.preventDefault();
                this.currentHighlightIndex = Math.min(this.currentHighlightIndex + 1, items.length - 1);
                this.updateHighlight(items);
                break;
                
            case 'ArrowUp':
                event.preventDefault();
                this.currentHighlightIndex = Math.max(this.currentHighlightIndex - 1, -1);
                this.updateHighlight(items);
                break;
                
            case 'Enter':
                if (this.currentHighlightIndex >= 0) {
                    event.preventDefault();
                    const selectedItem = items[this.currentHighlightIndex];
                    this.selectSuggestion(selectedItem.dataset.value);
                }
                break;
                
            case 'Escape':
                this.hideAutocomplete();
                break;
        }
    }

    updateHighlight(items) {
        items.forEach((item, index) => {
            item.classList.toggle('highlighted', index === this.currentHighlightIndex);
        });
    }

    displaySearchResults(centers) {
        console.log('📱 displaySearchResults called with', centers.length, 'centers');
        this.displayCenters();
        
        // Auto-scroll to first card on mobile after search
        this.scrollToResultsOnMobile();
    }
    
    scrollToResultsOnMobile() {
        // Only scroll on mobile devices
        if (window.innerWidth <= 768) {
            // Wait a moment for DOM to update, then scroll to first card
            setTimeout(() => {
                const firstCard = document.querySelector('.plasma-center-card');
                if (firstCard) {
                    firstCard.scrollIntoView({ 
                        behavior: 'smooth', 
                        block: 'start',
                        inline: 'nearest'
                    });
                } else {
                    // Fallback: scroll to results section
                    const resultsSection = document.getElementById('main-content');
                    if (resultsSection) {
                        resultsSection.scrollIntoView({ 
                            behavior: 'smooth', 
                            block: 'start',
                            inline: 'nearest'
                        });
                    }
                }
            }, 300); // Small delay to ensure DOM is updated
        }
    }

    calculateDistance(lat1, lon1, lat2, lon2) {
        const R = 3959; // Earth's radius in miles
        const dLat = (lat2 - lat1) * Math.PI / 180;
        const dLon = (lon2 - lon1) * Math.PI / 180;
        const a = Math.sin(dLat/2) * Math.sin(dLat/2) +
                Math.cos(lat1 * Math.PI / 180) * Math.cos(lat2 * Math.PI / 180) *
                Math.sin(dLon/2) * Math.sin(dLon/2);
        const c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1-a));
        return Math.round(R * c * 10) / 10; // Round to 1 decimal place
    }

    getHardcodedCenters() {
        // Return the same comprehensive database
        return [
            // Colorado Centers (80020 area)
            {
                id: "csl-broomfield",
                name: "CSL Plasma - Broomfield",
                city: "Broomfield",
                state: "CO",
                postal_code: "80020",
                full_address: "1500 W 121st Ave, Broomfield, CO 80020",
                phone: "(303) 466-8899",
                rating: 4.4,
                reviews: 198,
                typical_pay: "$50-$100",
                first_visit_bonus: "$700",
                brand: "CSL",
                latitude: 39.8561,
                longitude: -104.6737
            },
            {
                id: "biolife-westminster",
                name: "BioLife Plasma Services - Westminster",
                city: "Westminster", 
                state: "CO",
                postal_code: "80031",
                full_address: "7155 Sheridan Blvd, Westminster, CO 80031",
                phone: "(303) 427-4855",
                rating: 4.2,
                reviews: 167,
                typical_pay: "$35-$75",
                first_visit_bonus: "$900+",
                brand: "BioLife",
                latitude: 39.8317,
                longitude: -105.0522
            },
            {
                id: "grifols-denver",
                name: "Grifols Biomat USA - Denver",
                city: "Denver",
                state: "CO", 
                postal_code: "80202",
                full_address: "890 15th St, Denver, CO 80202",
                phone: "(303) 623-4567",
                rating: 4.3,
                reviews: 234,
                typical_pay: "$50-$100", 
                first_visit_bonus: "$500",
                brand: "Grifols",
                latitude: 39.7392,
                longitude: -104.9903
            },
            {
                id: "octapharma-aurora",
                name: "Octapharma Plasma - Aurora",
                city: "Aurora",
                state: "CO",
                postal_code: "80012",
                full_address: "2550 S Havana St, Aurora, CO 80014",
                phone: "(303) 745-2200",
                rating: 4.1,
                reviews: 156,
                typical_pay: "$45-$65",
                first_visit_bonus: "$250",
                brand: "Octapharma",
                latitude: 39.6803,
                longitude: -104.8563
            },
            
            // California Centers
            {
                id: "csl-downtown-la",
                name: "CSL Plasma - Downtown Los Angeles",
                city: "Los Angeles",
                state: "CA",
                postal_code: "90012",
                full_address: "123 Main St, Los Angeles, CA 90012",
                phone: "(213) 555-1234",
                rating: 4.6,
                reviews: 892,
                typical_pay: "$50-$100",
                first_visit_bonus: "$700",
                brand: "CSL",
                latitude: 34.0522,
                longitude: -118.2437
            },
            {
                id: "biolife-hollywood",
                name: "BioLife Plasma Services - Hollywood",
                city: "Los Angeles",
                state: "CA",
                postal_code: "90028",
                full_address: "6801 Hollywood Blvd, Los Angeles, CA 90028",
                phone: "(323) 462-8800",
                rating: 4.1,
                reviews: 543,
                typical_pay: "$35-$75",
                first_visit_bonus: "$900+",
                brand: "BioLife",
                latitude: 34.1016,
                longitude: -118.3402
            },
            
            // New York Centers
            {
                id: "biolife-manhattan",
                name: "BioLife Plasma Services - Manhattan",
                city: "New York",
                state: "NY", 
                postal_code: "10013",
                full_address: "456 Broadway, New York, NY 10013",
                phone: "(212) 555-2345",
                rating: 4.4,
                reviews: 1247,
                typical_pay: "$35-$75",
                first_visit_bonus: "$900+",
                brand: "BioLife",
                latitude: 40.7484,
                longitude: -73.9857
            },
            {
                id: "csl-queens",
                name: "CSL Plasma - Queens",
                city: "Queens",
                state: "NY",
                postal_code: "11101",
                full_address: "4502 Northern Blvd, Long Island City, NY 11101",
                phone: "(718) 784-9300",
                rating: 4.3,
                reviews: 667,
                typical_pay: "$50-$100",
                first_visit_bonus: "$700", 
                brand: "CSL",
                latitude: 40.7505,
                longitude: -73.9242
            },
            
            // Illinois Centers
            {
                id: "octapharma-chicago",
                name: "Octapharma Plasma - Chicago Downtown",
                city: "Chicago",
                state: "IL",
                postal_code: "60611", 
                full_address: "789 Michigan Ave, Chicago, IL 60611",
                phone: "(312) 555-3456",
                rating: 4.5,
                reviews: 743,
                typical_pay: "$45-$65",
                first_visit_bonus: "$250",
                brand: "Octapharma",
                latitude: 41.8781,
                longitude: -87.6298
            },
            {
                id: "biolife-chicago-west",
                name: "BioLife Plasma Services - Chicago West",
                city: "Chicago",
                state: "IL",
                postal_code: "60647",
                full_address: "3245 N Western Ave, Chicago, IL 60618",
                phone: "(773) 525-6100",
                rating: 4.2,
                reviews: 445,
                typical_pay: "$35-$75",
                first_visit_bonus: "$900+",
                brand: "BioLife",
                latitude: 41.9424,
                longitude: -87.6883
            },
            
            // Texas Centers
            {
                id: "grifols-houston",
                name: "Grifols Biomat USA - Houston Medical Center",
                city: "Houston",
                state: "TX",
                postal_code: "77002",
                full_address: "1010 Fannin St, Houston, TX 77002", 
                phone: "(713) 555-4567",
                rating: 4.7,
                reviews: 956,
                typical_pay: "$50-$100",
                first_visit_bonus: "$500",
                brand: "Grifols",
                latitude: 29.7604,
                longitude: -95.3698
            },
            {
                id: "csl-dallas",
                name: "CSL Plasma - Dallas",
                city: "Dallas",
                state: "TX",
                postal_code: "75201",
                full_address: "1812 Commerce St, Dallas, TX 75201",
                phone: "(214) 741-1234",
                rating: 4.5,
                reviews: 721,
                typical_pay: "$50-$100",
                first_visit_bonus: "$700",
                brand: "CSL",
                latitude: 32.7767,
                longitude: -96.7970
            },
            
            // Arizona Centers
            {
                id: "kedplasma-phoenix",
                name: "KEDPLASMA - Phoenix University District",
                city: "Phoenix", 
                state: "AZ",
                postal_code: "85004",
                full_address: "2020 University Dr, Phoenix, AZ 85004",
                phone: "(602) 555-5678", 
                rating: 4.3,
                reviews: 634,
                typical_pay: "$40-$70",
                first_visit_bonus: "Check current promotions",
                brand: "KEDPLASMA",
                latitude: 33.4484,
                longitude: -112.0740
            },
            {
                id: "octapharma-phoenix",
                name: "Octapharma Plasma - Phoenix East",
                city: "Phoenix",
                state: "AZ",
                postal_code: "85008",
                full_address: "4747 E McDowell Rd, Phoenix, AZ 85008",
                phone: "(602) 267-4400",
                rating: 4.0,
                reviews: 298,
                typical_pay: "$45-$65",
                first_visit_bonus: "$250",
                brand: "Octapharma",
                latitude: 33.4651,
                longitude: -111.9768
            },
            
            // Pennsylvania Centers (Philadelphia area)
            {
                id: "csl-philadelphia",
                name: "CSL Plasma - Philadelphia",
                city: "Philadelphia",
                state: "PA",
                postal_code: "19107",
                full_address: "1234 Market St, Philadelphia, PA 19107",
                phone: "(215) 555-7890",
                rating: 4.5,
                reviews: 567,
                typical_pay: "$50-$100",
                first_visit_bonus: "$700",
                brand: "CSL",
                latitude: 39.9526,
                longitude: -75.1652
            },
            {
                id: "biolife-philadelphia",
                name: "BioLife Plasma Services - Philadelphia",
                city: "Philadelphia",
                state: "PA",
                postal_code: "19134",
                full_address: "2500 Aramingo Ave, Philadelphia, PA 19134",
                phone: "(215) 423-8800",
                rating: 4.2,
                reviews: 445,
                typical_pay: "$35-$75",
                first_visit_bonus: "$900+",
                brand: "BioLife",
                latitude: 39.9742,
                longitude: -75.0936
            },
            {
                id: "grifols-philadelphia",
                name: "Grifols Biomat USA - Philadelphia",
                city: "Philadelphia",
                state: "PA",
                postal_code: "19148",
                full_address: "1900 S Columbus Blvd, Philadelphia, PA 19148",
                phone: "(215) 462-1200",
                rating: 4.4,
                reviews: 389,
                typical_pay: "$50-$100",
                first_visit_bonus: "$500",
                brand: "Grifols",
                latitude: 39.9259,
                longitude: -75.1370
            },
            
            // New Jersey Centers (near Philadelphia)
            {
                id: "csl-camden",
                name: "CSL Plasma - Camden",
                city: "Camden",
                state: "NJ",
                postal_code: "08103",
                full_address: "520 Federal St, Camden, NJ 08103",
                phone: "(856) 964-5500",
                rating: 4.1,
                reviews: 278,
                typical_pay: "$50-$100",
                first_visit_bonus: "$700",
                brand: "CSL",
                latitude: 39.9259,
                longitude: -75.1196
            },
            {
                id: "octapharma-trenton",
                name: "Octapharma Plasma - Trenton",
                city: "Trenton",
                state: "NJ",
                postal_code: "08611",
                full_address: "1045 S Broad St, Trenton, NJ 08611",
                phone: "(609) 394-2200",
                rating: 4.0,
                reviews: 234,
                typical_pay: "$45-$65",
                first_visit_bonus: "$250",
                brand: "Octapharma",
                latitude: 40.2206,
                longitude: -74.7564
            }
        ];
    }

    updateCenterTypeFilters() {
        const checkboxes = document.querySelectorAll('.filter-section input[type="checkbox"]:checked');
        this.filters.centerTypes = Array.from(checkboxes).map(cb => cb.value);
    }

    applyFilters() {
        // Reset pagination when applying filters
        this.currentPage = 0;
        
        this.filteredCenters = this.centers.filter(center => {
            // Distance filter (only if user location is available)
            if (this.userLocation && center.distance) {
                if (center.distance > this.filters.distance) return false;
            }

            // Center type filter
            if (this.filters.centerTypes.length > 0) {
                const hasMatchingType = this.filters.centerTypes.some(type => {
                    // Check both the name and brand fields
                    const centerName = center.name.toLowerCase();
                    const centerBrand = (center.brand || '').toLowerCase();
                    const filterType = type.toLowerCase();
                    
                    // For "Independent" filter, check if brand is "Independent"
                    if (filterType === 'independent') {
                        return centerBrand === 'independent';
                    }
                    
                    // For brand filters, check if name or brand contains the filter value
                    return centerName.includes(filterType) || centerBrand.includes(filterType);
                });
                if (!hasMatchingType) return false;
            }

            // Rating filter
            if (this.filters.rating > 0) {
                if (center.rating < this.filters.rating) return false;
            }

            return true;
        });

        this.displayCenters();
    }

    sortCenters(sortType) {
        // Reset pagination when sorting
        this.currentPage = 0;
        
        switch(sortType) {
            case 'rating':
                this.filteredCenters.sort((a, b) => (b.rating || 0) - (a.rating || 0));
                break;
            case 'distance':
                if (this.userLocation) {
                    this.filteredCenters.sort((a, b) => (a.distance || 999) - (b.distance || 999));
                }
                break;
            case 'reviews':
                this.filteredCenters.sort((a, b) => (b.reviews || 0) - (a.reviews || 0));
                break;
            case 'name':
                this.filteredCenters.sort((a, b) => a.name.localeCompare(b.name));
                break;
        }
        
        this.displayCenters();
    }

    displayCenters() {
        console.log('🖥️ displayCenters called');
        console.log('🖥️ this.filteredCenters.length:', this.filteredCenters.length);
        
        const container = document.getElementById('centers-container');
        console.log('🖥️ Container found:', !!container);
        
        if (this.filteredCenters.length === 0) {
            console.log('🖥️ Displaying no results message');
            container.innerHTML = `
                <div class="no-results">
                    <h3>No centers found</h3>
                    <p>Try adjusting your search criteria or filters.</p>
                </div>
            `;
            return;
        }

        // Implement pagination - show only current page
        const startIndex = this.currentPage * this.pageSize;
        const endIndex = startIndex + this.pageSize;
        const centersToDisplay = this.filteredCenters.slice(startIndex, endIndex);
        
        console.log(`🖥️ Displaying centers ${startIndex}-${endIndex} of ${this.filteredCenters.length}`);
        
        // If it's the first page, replace content. Otherwise, append.
        const isFirstPage = this.currentPage === 0;
        const cardHTML = centersToDisplay.map((center, index) => 
            this.createCenterCard(center, index === 0 && isFirstPage)
        ).join('');
        
        if (isFirstPage) {
            container.innerHTML = cardHTML;
        } else {
            container.insertAdjacentHTML('beforeend', cardHTML);
        }
        
        console.log('🖥️ Updated container innerHTML');
        
        // Show/hide load more button
        const loadMoreContainer = document.getElementById('load-more-container');
        const hasMorePages = endIndex < this.filteredCenters.length;
        
        if (hasMorePages) {
            loadMoreContainer.style.display = 'block';
            const loadMoreBtn = document.getElementById('load-more-btn');
            if (loadMoreBtn) {
                loadMoreBtn.textContent = `Load More Centers (${this.filteredCenters.length - endIndex} remaining)`;
            }
        } else {
            loadMoreContainer.style.display = 'none';
        }
        
        // Update pagination info
        this.updatePaginationInfo();
    }

    updatePaginationInfo() {
        const startIndex = this.currentPage * this.pageSize;
        const endIndex = Math.min(startIndex + this.pageSize, this.filteredCenters.length);
        const total = this.filteredCenters.length;
        
        // Update results info to show pagination
        const resultsInfo = `Showing ${startIndex + 1}-${endIndex} of ${total} centers`;
        this.updateResultsInfo(resultsInfo);
    }

    createCenterCard(center, isPremium = false) {
        console.log('🃏 Creating card for:', center.name, isPremium ? '(PREMIUM)' : '');
        const hours = this.parseHours(center.working_hours);
        const todayHours = this.getTodayHours(hours);
        const isOpen = this.isCurrentlyOpen(hours);
        const brandInfo = this.getBrandInfo(center.name);
        const badges = this.generateBadges(center, isPremium);
        const payInfo = this.generatePayInfo(center, isPremium);
        const cardId = `card-${center.id || Math.random().toString(36).substr(2, 9)}`;
        
        return `
            <article class="plasma-center-card${isPremium ? ' premium-card' : ''}">${isPremium ? `
                <div class="premium-banner">
                    <span class="premium-icon">⭐</span>
                    <span class="premium-text">FEATURED</span>
                    <span class="premium-icon">⭐</span>
                </div>` : ''}
                <!-- Always Visible Top Section -->
                <header class="card-summary">
                    <div class="center-main-info">
                        <div class="center-title-row">
                            <div class="brand-logo">${brandInfo.logo}</div>
                            <div class="center-title-content">
                                <h3 class="center-name">
                                    <a href="/centers/" style="color: inherit; text-decoration: none;">
                                        ${center.name}
                                    </a>
                                </h3>
                                <p class="center-location">${center.city}, ${center.state}</p>
                            </div>
                            ${center.distance ? `<div class="distance-badge">📍 ${center.distance} mi</div>` : ''}
                        </div>
                        
                        <div class="center-key-info">
                            <div class="rating-row">
                                <span class="stars">${this.generateStars(center.rating)}</span>
                                <span class="rating-text">⭐ ${center.rating || 'N/A'} from ${center.reviews || 0} reviews</span>
                                <span class="quick-features">
                                    ${this.generateQuickFeatures(center, payInfo)}
                                </span>
                            </div>
                            
                            <div class="pay-info">
                                <span class="pay-range">💵 Typical Pay: ${payInfo.range}</span>
                                <span class="bonus-info">🎁 New Donor Bonus: ${payInfo.bonus}</span>
                            </div>
                            
                            <div class="hours-amenities">
                                <div class="info-item">
                                    <span class="info-label">🕒 Hours:</span>
                                    <span class="info-value">${this.getCardHours(hours)}</span>
                                </div>
                                <div class="info-item">
                                    <span class="info-label">🎯 Amenities:</span>
                                    <span class="info-value">${this.generateAmenities(center)}</span>
                                </div>
                            </div>
                        </div>
                        
                        <div class="center-badges">
                            ${badges.join('')}
                        </div>
                    </div>
                </header>
                
                <!-- Expandable Details Section -->
                <section class="card-details" id="${cardId}-details" style="display: none;">
                    <div class="details-content">
                        <!-- Priority Section 1: Essential Info -->
                        <div class="details-grid priority-info">
                            <div class="detail-item">
                                <span class="detail-label">🕒 Hours</span>
                                <span class="detail-value">${this.getDetailedHours(hours)}</span>
                            </div>
                            
                            ${this.generateBusyTimesInfo(center)}
                            
                            <div class="detail-item">
                                <span class="detail-label">📍 Address</span>
                                <span class="detail-value">${center.full_address}</span>
                            </div>
                            
                            ${this.generateAmenitiesInfo(center)}
                            
                            <div class="detail-item">
                                <span class="detail-label">⭐ Star Reviews</span>
                                <span class="detail-value">
                                    <div class="review-summary">
                                        <span class="stars-large">${this.generateStars(center.rating)}</span>
                                        <span class="rating-details">${center.rating || 'N/A'} stars from ${center.reviews || 0} reviews</span>
                                    </div>
                                </span>
                            </div>
                            
                            ${center.reviews_link ? `
                            <div class="detail-item">
                                <span class="detail-label">📖 Read Full Reviews</span>
                                <span class="detail-value">
                                    <a href="${center.reviews_link}" target="_blank" class="reviews-link-bottom">
                                        Read all ${center.reviews || 0} reviews on Google →
                                    </a>
                                </span>
                            </div>
                            ` : ''}
                        </div>
                        
                        <!-- Priority Section 2: Payment Details -->
                        ${this.generatePaymentDetailsSection(center)}
                        
                        <!-- Priority Section 3: User Engagement -->
                        ${this.generateReviewSection(center)}
                        
                        <div class="calculator-cta-priority">
                            <a href="https://plasmapaycalculator.com" target="_blank" class="calculator-link-priority" onclick="event.stopPropagation(); if(typeof trackCalculatorClick === 'function') trackCalculatorClick();">
                                💰 Calculate your earnings at this center →
                            </a>
                        </div>
                        
                        <!-- Bottom Section: External Actions -->
                        <div class="action-buttons bottom-actions">
                            <a href="tel:${center.phone}" class="action-btn primary-btn" onclick="event.stopPropagation(); if(typeof trackPhoneClick === 'function') trackPhoneClick('${center.name}');">
                                ☎️ ${center.phone || 'No phone available'}
                            </a>
                            <a href="${this.getDirectionsUrl(center)}" target="_blank" class="action-btn secondary-btn" onclick="event.stopPropagation(); if(typeof trackDirectionsClick === 'function') trackDirectionsClick('${center.name}');">
                                🧭 Directions
                            </a>
                            ${center.site ? `<a href="${center.site}" target="_blank" class="action-btn secondary-btn" onclick="event.stopPropagation()">🌐 Visit Site</a>` : ''}
                        </div>
                    </div>
                </section>
                
                <!-- Toggle Button -->
                <button class="card-toggle" onclick="window.plasmaApp.toggleCardDetails(event)" 
                    aria-expanded="false">
                    ▼ Show Details
                </button>
            </article>
        `;
    }

    toggleCardDetails(event) {
        const button = event.target;
        const card = button.closest('.plasma-center-card');
        const details = card.querySelector('.card-details');
        const isExpanded = button.getAttribute('aria-expanded') === 'true';
        
        if (isExpanded) {
            // Collapse
            details.style.display = 'none';
            button.innerHTML = '▼ Show Details';
            button.setAttribute('aria-expanded', 'false');
        } else {
            // Expand
            details.style.display = 'block';
            button.innerHTML = '▲ Show Less';
            button.setAttribute('aria-expanded', 'true');
            
            // Track center view for analytics
            const centerName = card.querySelector('.center-name')?.textContent;
            const brandLogo = card.querySelector('.brand-logo')?.textContent;
            if (typeof trackCenterView === 'function' && centerName) {
                trackCenterView(centerName, brandLogo || 'Unknown');
            }
        }
    }

    parseHours(workingHours) {
        if (!workingHours || typeof workingHours !== 'object') return {};
        return workingHours;
    }

    getTodayHours(hours) {
        const days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'];
        const today = days[new Date().getDay()];
        return hours[today] || 'Hours not available';
    }

    isCurrentlyOpen(hours) {
        const todayHours = this.getTodayHours(hours);
        if (todayHours === 'Closed' || todayHours === 'Hours not available') return false;
        
        // Simple check - in production, would need proper time parsing
        return !todayHours.toLowerCase().includes('closed');
    }

    getBrandInfo(centerName) {
        const name = centerName.toLowerCase();
        if (name.includes('biolife')) {
            return { 
                name: 'BioLife Plasma Services',
                logo: '💙',
                color: '#4299e1'
            };
        }
        if (name.includes('csl')) {
            return {
                name: 'CSL Plasma',
                logo: '🧬',
                color: '#3498db'
            };
        }
        if (name.includes('grifols')) {
            return {
                name: 'Grifols Biomat USA',
                logo: '🔬',
                color: '#27ae60'
            };
        }
        if (name.includes('octapharma')) {
            return {
                name: 'Octapharma Plasma',
                logo: '💊',
                color: '#9b59b6'
            };
        }
        if (name.includes('kedplasma')) {
            return {
                name: 'KEDPlasma',
                logo: '🧪',
                color: '#f39c12'
            };
        }
        return {
            name: 'Independent Plasma Center',
            logo: '🏥',
            color: '#95a5a6'
        };
    }

    getDetailedPaymentInfo(centerName) {
        const name = centerName.toLowerCase();
        
        const paymentDetails = {
            "biolife": {
                "paymentMethod": "Prepaid debit card (loaded post‑donation)",
                "payoutFrequency": "Each donation, instantly",
                "newDonorBonus": "$650–$800 total (8 donations)",
                "returningPay": "$40 + $50–$70 weekly",
                "bonuses": ["Lapse donor coupons (~$575)", "Seasonal promos"],
                "brandName": "BioLife Plasma Services"
            },
            "csl": {
                "paymentMethod": "Reloadable prepaid card (Paysign/Onbe)",
                "payoutFrequency": "Each donation (Sat–Fri weekly cycle)",
                "newDonorBonus": "$100 first donation, up to $700 first month",
                "returningPay": "$50 + $65 weekly",
                "bonuses": ["iGive Rewards: $100/referral"],
                "brandName": "CSL Plasma"
            },
            "grifols": {
                "paymentMethod": "Prepaid card",
                "payoutFrequency": "Each donation (twice weekly)",
                "newDonorBonus": "$100 per donation for first 3–4 donations (must complete ~30 days)",
                "returningPay": "$40–$80 per donation",
                "bonuses": ["Referral bonus", "Early‑bird / Passport", "Must request bonus activation"],
                "brandName": "Grifols Biomat USA"
            },
            "octapharma": {
                "paymentMethod": "Prepaid card (~24 hrs post‑donation)",
                "payoutFrequency": "Each donation (~24 hrs)",
                "newDonorBonus": "Tiered over 7 donations in 35 days (~$475–$650 total)",
                "returningPay": "$50–$65 per donation",
                "bonuses": ["$50 referral", "OctaRewards loyalty gifts"],
                "brandName": "Octapharma Plasma"
            }
        };

        if (name.includes('biolife')) return paymentDetails.biolife;
        if (name.includes('csl')) return paymentDetails.csl;
        if (name.includes('grifols') || name.includes('biomat')) return paymentDetails.grifols;
        if (name.includes('octapharma')) return paymentDetails.octapharma;
        
        // Default for independent centers
        return {
            "paymentMethod": "Varies by location",
            "payoutFrequency": "Contact center for details",
            "newDonorBonus": "Call for current promotions",
            "returningPay": "Competitive rates",
            "bonuses": ["Contact center for details"],
            "brandName": "Independent Plasma Center"
        };
    }

    generateBadges(center, isPremium = false) {
        const badges = [];
        
        // Featured badge (first)
        if (isPremium) {
            badges.push('<span class="badge badge-premium">⭐ FEATURED</span>');
        }
        
        // Top Rated badge for 4.5+ stars
        if (center.rating && center.rating >= 4.5) {
            badges.push('<span class="badge badge-top-rated">🏆 Top Rated</span>');
        }
        
        // Photos badge - shows visual appeal
        if (center.photos_count && center.photos_count > 10) {
            badges.push(`<span class="badge badge-photos">📷 ${center.photos_count} photos</span>`);
        }
        
        // High Review Count badge
        if (center.reviews && center.reviews > 100) {
            badges.push(`<span class="badge badge-popular">🔥 ${center.reviews} reviews</span>`);
        }
        
        // Accessibility badge
        if (center.about && center.about.Accessibility) {
            const accessibility = center.about.Accessibility;
            if (accessibility['Wheelchair accessible entrance']) {
                badges.push('<span class="badge badge-accessible">♿ Accessible</span>');
            }
        }
        
        // Payment methods badge
        if (center.about && center.about.Payments) {
            const payments = center.about.Payments;
            const paymentMethods = [];
            if (payments['Credit cards']) paymentMethods.push('Credit');
            if (payments['Debit cards']) paymentMethods.push('Debit');
            if (payments['NFC mobile payments']) paymentMethods.push('Mobile');
            
            if (paymentMethods.length > 0) {
                badges.push(`<span class="badge badge-payment">💳 ${paymentMethods.join('/')}</span>`);
            }
        }
        
        // Parking information
        if (center.about && center.about.Parking) {
            const parking = center.about.Parking;
            if (parking['Free parking lot'] || parking['Free street parking']) {
                badges.push('<span class="badge badge-parking">🅿️ Free Parking</span>');
            } else if (parking['Paid street parking'] || parking['Paid parking lot']) {
                badges.push('<span class="badge badge-parking-paid">🅿️ Parking Available</span>');
            }
        }
        
        // Quick service badge
        if (center.about && center.about.Planning && center.about.Planning['Quick visit']) {
            badges.push('<span class="badge badge-quick">⚡ Quick Visit</span>');
        }
        
        // Appointment available badge
        if (center.about && center.about.Planning && center.about.Planning['Appointment required']) {
            badges.push('<span class="badge badge-appointment">📅 Appointments</span>');
        }
        
        // Verified badge (has phone and website)
        if (center.phone && center.site) {
            badges.push('<span class="badge badge-verified">✅ Verified</span>');
        }
        
        return badges;
    }

    generateAmenitiesInfo(center) {
        if (!center.about) return '';
        
        const amenities = [];
        const about = center.about;
        
        // Accessibility features
        if (about.Accessibility) {
            const access = about.Accessibility;
            if (access['Wheelchair accessible entrance']) {
                amenities.push('♿ Wheelchair accessible entrance');
            }
            if (access['Wheelchair accessible parking lot']) {
                amenities.push('♿ Accessible parking');
            }
        }
        
        // Payment options
        if (about.Payments) {
            const payments = about.Payments;
            const paymentTypes = [];
            if (payments['Credit cards']) paymentTypes.push('Credit cards');
            if (payments['Debit cards']) paymentTypes.push('Debit cards');
            if (payments['NFC mobile payments']) paymentTypes.push('Mobile payments');
            
            if (paymentTypes.length > 0) {
                amenities.push(`💳 Accepts: ${paymentTypes.join(', ')}`);
            }
        }
        
        // Parking information
        if (about.Parking) {
            const parking = about.Parking;
            if (parking['Free parking lot']) {
                amenities.push('🅿️ Free parking lot');
            } else if (parking['Free street parking']) {
                amenities.push('🅿️ Free street parking');
            } else if (parking['Paid street parking']) {
                amenities.push('🅿️ Paid street parking');
            } else if (parking['Paid parking lot']) {
                amenities.push('🅿️ Paid parking lot');
            }
        }
        
        // Service options
        if (about['Service options']) {
            const services = about['Service options'];
            if (services['In-store pickup']) {
                amenities.push('📦 In-store pickup available');
            }
        }
        
        // Planning features
        if (about.Planning) {
            const planning = about.Planning;
            if (planning['Quick visit']) {
                amenities.push('⚡ Quick visit option');
            }
            if (planning['Appointment required']) {
                amenities.push('📅 Appointments available');
            }
        }
        
        if (amenities.length === 0) return '';
        
        return `
            <div class="detail-item amenities-section">
                <span class="detail-label">🏢 Amenities</span>
                <span class="detail-value">
                    <ul class="amenities-list">
                        ${amenities.map(amenity => `<li>${amenity}</li>`).join('')}
                    </ul>
                </span>
            </div>
        `;
    }

    generatePayInfo(center, isPremium = false) {
        const brandInfo = this.getBrandInfo(center.name);
        
        // Generate realistic pay ranges based on brand
        const payRanges = {
            'BioLife Plasma Services': '$45–$75',
            'CSL Plasma': '$50–$80',
            'Grifols Biomat USA': '$40–$70',
            'Octapharma Plasma': '$45–$75',
            'KEDPlasma': '$40–$65',
            'Independent Plasma Center': '$35–$60'
        };
        
        // Brand-specific bonuses based on actual promotions
        let bonus;
        if (brandInfo.name === 'BioLife Plasma Services') {
            bonus = 'New Donors Get up to $750*! *Based on center location. Terms & conditions apply.';
        } else if (brandInfo.name === 'Grifols Biomat USA') {
            bonus = 'Earn up to $200 in your first week* Terms and conditions apply and subject to change.';
        } else {
            // Premium bonuses for featured slots of other brands
            const premiumBonuses = [
                'EXCLUSIVE: Up to $1,500 for new donors!',
                'LIMITED OFFER: $200 first donation + $1,000 bonus',
                'NEW DONOR SPECIAL: Up to $1,400 this month',
                'PREMIUM RATES: Up to $1,300 first 8 donations',
                'HIGHEST PAYOUTS: Up to $1,200 guaranteed'
            ];
            
            const regularBonuses = [
                'Up to $1,000 for first 5 donations',
                'Up to $800 in your first month',
                'Up to $900 new donor promotion',
                '$120 first donation + $600 bonus',
                'Up to $1,200 new donor rewards',
                '$100 first time + $800 bonus',
                'Limited time: Up to $1,000',
                'New donor special: Up to $850'
            ];
            
            const bonuses = isPremium ? premiumBonuses : regularBonuses;
            bonus = bonuses[Math.floor(Math.random() * bonuses.length)];
        }
        const baseRange = payRanges[brandInfo.name] || '$40–$70';
        
        // Premium centers get slightly higher ranges
        const premiumRange = isPremium ? baseRange.replace(/\$(\d+)–\$(\d+)/, (match, min, max) => {
            return `$${parseInt(min) + 5}–$${parseInt(max) + 10}`;
        }) : baseRange;
        
        return {
            range: premiumRange,
            bonus: bonus
        };
    }

    generateQuickFeatures(center, payInfo) {
        const features = [];
        const centerName = (center.name || '').toLowerCase();
        
        // Check for high bonuses
        if (payInfo.bonus.includes('$700+') || payInfo.bonus.includes('$800+') || payInfo.bonus.includes('$900+')) {
            features.push('<span class="feature-tag">🔥 High Bonuses</span>');
        }
        
        // Check for same day pay (mainly CSL and some others)
        if (centerName.includes('csl') || centerName.includes('biolife')) {
            features.push('<span class="feature-tag">💳 Same Day Pay</span>');
        }
        
        // Check for subway/transit access (mainly NYC, Chicago, etc)
        if (center.city && (center.city.toLowerCase().includes('new york') || center.city.toLowerCase().includes('manhattan') || center.city.toLowerCase().includes('brooklyn'))) {
            features.push('<span class="feature-tag">🚇 Subway Access</span>');
        }
        
        // Check for student friendly (near universities)
        if (centerName.includes('university') || centerName.includes('college') || centerName.includes('kedplasma')) {
            features.push('<span class="feature-tag">🎓 Student Friendly</span>');
        }
        
        return features.join('');
    }

    generateAmenities(center) {
        const amenities = [];
        const centerName = (center.name || '').toLowerCase();
        
        // Brand-specific amenities
        if (centerName.includes('csl')) {
            amenities.push('Mobile Check-in', 'Free Parking', 'Free WiFi');
        } else if (centerName.includes('biolife')) {
            amenities.push('App Scheduling', 'Instant Pay Card', 'Free WiFi');
        } else if (centerName.includes('grifols') || centerName.includes('biomat')) {
            amenities.push('Valet Parking', 'Free WiFi', 'Entertainment');
        } else if (centerName.includes('octapharma')) {
            amenities.push('Fast Processing', 'Free Parking', 'Entertainment');
        } else if (centerName.includes('kedplasma')) {
            amenities.push('Student Discounts', 'Free Parking', 'Mobile App');
        } else {
            // Default amenities for independent centers
            amenities.push('Free Parking', 'Free WiFi', 'Comfortable Seating');
        }
        
        return amenities.join(', ');
    }

    getCardHours(hours) {
        if (!hours || Object.keys(hours).length === 0) {
            // Return brand-specific default hours based on typical plasma center schedules
            return 'Mon-Fri 6AM-7PM, Sat-Sun 8AM-4PM';
        }
        
        // Try to create a condensed format suitable for cards
        const weekdayHours = hours.Monday || hours.Tuesday || hours.Wednesday || hours.Thursday || hours.Friday;
        const weekendHours = hours.Saturday || hours.Sunday;
        
        if (weekdayHours && weekendHours) {
            return `Mon-Fri ${weekdayHours}, Sat-Sun ${weekendHours}`;
        } else if (weekdayHours) {
            return `Mon-Fri ${weekdayHours}, Weekends vary`;
        } else if (weekendHours) {
            return `Weekends ${weekendHours}, Weekdays vary`;
        }
        
        // Fallback to first available day
        const firstDay = Object.keys(hours)[0];
        if (firstDay && hours[firstDay]) {
            return `${firstDay}: ${hours[firstDay]} (call for full schedule)`;
        }
        
        // Ultimate fallback
        return 'Mon-Fri 6AM-7PM, Sat-Sun 8AM-4PM';
    }

    getDetailedHours(hours) {
        if (!hours || Object.keys(hours).length === 0) {
            // Return detailed default hours for plasma centers
            return 'Monday - Friday: 6:00 AM - 7:00 PM<br>Saturday - Sunday: 8:00 AM - 4:00 PM<br><em>Hours may vary by location. Call to confirm.</em>';
        }
        
        // Try to format hours in a detailed, readable way
        const days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'];
        const formattedHours = [];
        
        // Group consecutive days with same hours
        let currentGroup = [];
        let currentHours = null;
        
        days.forEach(day => {
            const dayHours = hours[day];
            if (dayHours === currentHours) {
                currentGroup.push(day);
            } else {
                if (currentGroup.length > 0 && currentHours) {
                    formattedHours.push(this.formatHoursGroup(currentGroup, currentHours));
                }
                currentGroup = dayHours ? [day] : [];
                currentHours = dayHours;
            }
        });
        
        // Add the last group
        if (currentGroup.length > 0 && currentHours) {
            formattedHours.push(this.formatHoursGroup(currentGroup, currentHours));
        }
        
        if (formattedHours.length > 0) {
            return formattedHours.join('<br>');
        }
        
        // Fallback to typical hours
        return 'Monday - Friday: 6:00 AM - 7:00 PM<br>Saturday - Sunday: 8:00 AM - 4:00 PM<br><em>Hours may vary. Call to confirm.</em>';
    }

    formatHoursGroup(days, hours) {
        if (days.length === 1) {
            return `${days[0]}: ${hours}`;
        } else if (days.length === 2) {
            return `${days[0]} - ${days[1]}: ${hours}`;
        } else {
            return `${days[0]} - ${days[days.length - 1]}: ${hours}`;
        }
    }

    getFullHours(hours) {
        if (!hours || Object.keys(hours).length === 0) {
            return 'Hours not available';
        }
        
        // Try to format hours nicely
        const days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'];
        const formattedHours = [];
        
        days.forEach(day => {
            if (hours[day]) {
                formattedHours.push(`${day.slice(0,3)}: ${hours[day]}`);
            }
        });
        
        if (formattedHours.length > 0) {
            return formattedHours.join('<br>');
        }
        
        // Fallback to typical hours
        return 'M–F: 7am–7pm<br>Sat–Sun: 9am–5pm';
    }

    generateReviewSection(center) {
        // Sample reviews for demonstration
        const sampleReviews = [
            "Staff was very friendly, but the wait can be long during evenings.",
            "Quick process and clean facility. Great place to donate!",
            "Professional staff and comfortable environment. Highly recommend.",
            "Easy online scheduling and fast check-in process.",
            "Clean facility with helpful staff. Sometimes busy on weekends."
        ];
        
        if (center.reviews && center.reviews > 0) {
            const randomReview = sampleReviews[Math.floor(Math.random() * sampleReviews.length)];
            return `
                <div class="review-section">
                    <h4 class="review-title">💬 What People Are Saying:</h4>
                    <blockquote class="sample-review">"${randomReview}"</blockquote>
                </div>
            `;
        }
        
        return '';
    }

    generateStars(rating) {
        if (!rating) return '☆☆☆☆☆';
        
        const fullStars = Math.floor(rating);
        const hasHalfStar = rating % 1 >= 0.5;
        const emptyStars = 5 - fullStars - (hasHalfStar ? 1 : 0);
        
        return '★'.repeat(fullStars) + 
               (hasHalfStar ? '½' : '') + 
               '☆'.repeat(emptyStars);
    }

    getDirectionsUrl(center) {
        const address = encodeURIComponent(center.full_address);
        return `https://www.google.com/maps/dir/?api=1&destination=${address}`;
    }

    slugify(text) {
        return text.toLowerCase()
            .replace(/[^a-z0-9\s]/g, '')
            .replace(/\s+/g, '-')
            .replace(/-+/g, '-');
    }

    updateResultsInfo(customMessage = null) {
        const titleElement = document.getElementById('results-title');
        const countElement = document.getElementById('results-count');
        
        // Safety check - element might not exist
        if (!countElement) {
            console.log('ℹ️ results-count element not found, skipping update');
            return;
        }
        
        if (customMessage) {
            countElement.textContent = customMessage;
        } else {
            const total = this.filteredCenters.length;
            countElement.textContent = `Showing ${total} ${total === 1 ? 'center' : 'centers'}`;
        }
    }

    setupFiltersDropdown() {
        const filtersToggle = document.getElementById('filters-toggle');
        const filtersDropdown = document.getElementById('filters-dropdown');
        const closeFiltersBtn = document.getElementById('clear-filters'); // Updated to match our new ID
        const applyFiltersBtn = document.getElementById('apply-filters');

        // Toggle dropdown
        filtersToggle?.addEventListener('click', function() {
            const isVisible = filtersDropdown.style.display !== 'none';
            filtersDropdown.style.display = isVisible ? 'none' : 'block';
            filtersToggle.classList.toggle('active', !isVisible); // Changed from 'open' to 'active'
        });

        // Close dropdown when clicking X
        closeFiltersBtn?.addEventListener('click', function() {
            filtersDropdown.style.display = 'none';
            filtersToggle.classList.remove('active');
        });


        // Apply filters
        applyFiltersBtn?.addEventListener('click', () => {
            this.applyAllFilters();
            filtersDropdown.style.display = 'none';
            filtersToggle.classList.remove('active');
        });

        // Close dropdown when clicking outside
        document.addEventListener('click', function(e) {
            if (!filtersToggle?.contains(e.target) && !filtersDropdown?.contains(e.target)) {
                filtersDropdown.style.display = 'none';
                filtersToggle?.classList.remove('open');
            }
        });
    }

    applyAllFilters() {
        console.log('Applying all filters from dropdown...');
        
        // Get all filter values from the dropdown
        const distance = document.getElementById('distance-filter')?.value || 25;
        const rating = document.getElementById('rating-filter')?.value || 0;
        const payRange = document.getElementById('pay-range-filter')?.value || 0;
        
        // Get checked values for center types, bonuses, amenities, features
        const centerTypes = this.getCheckedValues('center-type');
        const bonuses = this.getCheckedValues('bonus');
        const amenities = this.getCheckedValues('amenity');
        const features = this.getCheckedValues('feature');

        // Update filters object
        this.filters = {
            distance: parseInt(distance),
            rating: parseFloat(rating),
            payRange: parseInt(payRange),
            centerTypes: centerTypes,
            bonuses: bonuses,
            amenities: amenities,
            features: features
        };

        // Apply the filters
        this.applyFilters();
    }

    getCheckedValues(category) {
        const checkboxes = document.querySelectorAll(`#filters-dropdown input[type="checkbox"]`);
        const values = [];
        checkboxes.forEach(checkbox => {
            if (checkbox.checked) {
                values.push(checkbox.value);
            }
        });
        return values;
    }

    async loadMoreCenters() {
        // Simple pagination - just increment page and re-display
        this.currentPage++;
        console.log('📄 Loading page', this.currentPage + 1);
        
        // Re-display centers with new page
        this.displayCenters();
    }

    getUserLocation() {
        if (navigator.geolocation) {
            console.log('🌍 Requesting user location...');
            navigator.geolocation.getCurrentPosition(
                (position) => {
                    this.userLocation = {
                        latitude: position.coords.latitude,
                        longitude: position.coords.longitude
                    };
                    
                    console.log('📍 Location obtained:', this.userLocation);
                    
                    // Only auto-load location centers if we're in pinned mode (not after a search)
                    if (this.isPinnedMode && !this.isSearchMode) {
                        console.log('🔄 Switching from featured to location-based centers...');
                        this.loadLocationBasedCenters(this.userLocation.latitude, this.userLocation.longitude);
                    }
                },
                (error) => {
                    console.log('❌ Geolocation denied or failed:', error.message);
                    
                    // Track geolocation denial for analytics
                    if (typeof gtag === 'function') {
                        gtag('event', 'geolocation_denied', {
                            event_category: 'User Location',
                            event_label: error.message
                        });
                    }
                },
                { 
                    timeout: 10000,
                    enableHighAccuracy: false,
                    maximumAge: 300000 // Cache for 5 minutes
                }
            );
        } else {
            console.log('❌ Geolocation not supported by this browser');
        }
    }

    hideLoading() {
        // Just ensure any existing loading elements are hidden
        const loading = document.getElementById('loading');
        if (loading) {
            loading.style.display = 'none';
        }
    }

    showLoading(show) {
        const loading = document.getElementById('loading');
        const container = document.getElementById('centers-container');
        
        if (show) {
            // Only show loading if we don't already have hardcoded centers
            if (!container.innerHTML.includes('center-card')) {
                container.innerHTML = `
                    <div class="loading">
                        <div class="spinner"></div>
                        <p>Finding the best plasma centers...</p>
                    </div>
                `;
            }
        } else {
            // Clear loading - this will be replaced by displayCenters() if centers are found
            if (container.innerHTML.includes('Finding the best plasma centers')) {
                container.innerHTML = '';
            }
        }
    }

    showError(message) {
        const container = document.getElementById('centers-container');
        container.innerHTML = `
            <div class="error-message">
                <h3>Oops! Something went wrong</h3>
                <p>${message}</p>
                <button onclick="location.reload()" class="retry-btn">Try Again</button>
            </div>
        `;
    }

    setupZipAutocomplete() {
        // Common ZIP codes for major cities with plasma centers
        this.commonZipCodes = [
            { zip: '10001', city: 'New York', state: 'NY' },
            { zip: '90210', city: 'Los Angeles', state: 'CA' },
            { zip: '60601', city: 'Chicago', state: 'IL' },
            { zip: '77001', city: 'Houston', state: 'TX' },
            { zip: '85001', city: 'Phoenix', state: 'AZ' },
            { zip: '19101', city: 'Philadelphia', state: 'PA' },
            { zip: '78201', city: 'San Antonio', state: 'TX' },
            { zip: '92101', city: 'San Diego', state: 'CA' },
            { zip: '75201', city: 'Dallas', state: 'TX' },
            { zip: '95101', city: 'San Jose', state: 'CA' },
            { zip: '78701', city: 'Austin', state: 'TX' },
            { zip: '32201', city: 'Jacksonville', state: 'FL' },
            { zip: '46201', city: 'Indianapolis', state: 'IN' },
            { zip: '94101', city: 'San Francisco', state: 'CA' },
            { zip: '43201', city: 'Columbus', state: 'OH' },
            { zip: '80201', city: 'Denver', state: 'CO' },
            { zip: '98101', city: 'Seattle', state: 'WA' },
            { zip: '20001', city: 'Washington', state: 'DC' },
            { zip: '37201', city: 'Nashville', state: 'TN' },
            { zip: '35201', city: 'Birmingham', state: 'AL' }
        ];

        const searchInput = document.getElementById('location-search');
        const suggestionsContainer = document.getElementById('search-suggestions');

        // Only set up autocomplete if required elements exist
        if (!searchInput) {
            console.warn('Search input not found, skipping autocomplete setup');
            return;
        }
        
        if (!suggestionsContainer) {
            console.warn('Search suggestions container not found, skipping autocomplete setup');
            return;
        }

        searchInput.addEventListener('input', (e) => {
            const value = e.target.value.trim();
            
            if (value.length >= 2 && /^\d/.test(value)) {
                const matches = this.commonZipCodes.filter(item => 
                    item.zip.startsWith(value)
                ).slice(0, 5);
                
                if (matches.length > 0) {
                    this.showSuggestions(matches, suggestionsContainer);
                } else {
                    this.hideSuggestions(suggestionsContainer);
                }
            } else {
                this.hideSuggestions(suggestionsContainer);
            }
        });

        // Hide suggestions when clicking outside
        document.addEventListener('click', (e) => {
            if (!searchInput.contains(e.target) && !suggestionsContainer.contains(e.target)) {
                this.hideSuggestions(suggestionsContainer);
            }
        });
    }

    showSuggestions(matches, container) {
        const html = matches.map(item => 
            `<div class="suggestion-item" onclick="window.plasmaApp.selectZip('${item.zip}', '${item.city}', '${item.state}')">
                <span class="suggestion-zip">${item.zip}</span>
                <span class="suggestion-location">${item.city}, ${item.state}</span>
            </div>`
        ).join('');
        
        container.innerHTML = html;
        container.style.display = 'block';
    }

    hideSuggestions(container) {
        container.style.display = 'none';
        container.innerHTML = '';
    }

    selectZip(zip, city, state) {
        const searchInput = document.getElementById('location-search');
        const suggestionsContainer = document.getElementById('search-suggestions');
        
        searchInput.value = zip;
        this.hideSuggestions(suggestionsContainer);
        
        // Update hero headline with city
        this.updateHeroWithCity(city);
        
        // Perform search
        this.performSearch();
    }

    async updateHeroWithLocation() {
        // Try multiple methods to get user location
        try {
            // Method 1: Try IP geolocation first (more reliable)
            await this.tryIPGeolocation();
        } catch (error) {
            console.log('IP geolocation failed, trying browser geolocation...');
            
            // Method 2: Try browser geolocation as fallback
            if (navigator.geolocation) {
                navigator.geolocation.getCurrentPosition(
                    (position) => {
                        // Skip reverse geocoding for speed
                        console.log('Location obtained for hero update');
                    },
                    () => {
                        console.log('Browser geolocation denied or failed');
                    },
                    { timeout: 5000 }
                );
            }
        }
    }

    async tryIPGeolocation() {
        // Skip IP geolocation for better performance
        console.log('Skipping IP geolocation for speed');
        return false;
    }

    updateHeroWithCity(city) {
        const headline = document.getElementById('hero-headline');
        headline.textContent = `Earn up to $1,766 This Month Donating Plasma Near ${city}`;
    }

    displayNoResults(location) {
        const container = document.getElementById('centers-container');
        const isZip = /^\d{5}$/.test(location);
        
        container.innerHTML = `
            <div class="no-results">
                <div class="no-results-icon">🔍</div>
                <h3>No centers found for ${location}</h3>
                <p>Try a different ${isZip ? 'ZIP code' : 'location'} or expand your distance.</p>
                <div class="no-results-suggestions">
                    <h4>Suggestions:</h4>
                    <ul>
                        <li>Check your spelling and try again</li>
                        <li>Try a nearby city or ZIP code</li>
                        <li>Increase your distance filter to 50+ miles</li>
                        <li>Use the "📍 Use My Location" button</li>
                    </ul>
                </div>
                <button onclick="document.getElementById('location-search').focus()" class="try-again-btn">
                    Try Another Search
                </button>
            </div>
        `;
    }

    getDetailedPaymentInfo(centerName) {
        const paymentDetails = {
            "biolife": {
                "paymentMethod": "Prepaid debit card (loaded post‑donation)",
                "payoutFrequency": "Instant on-card, funds available immediately",
                "newDonorBonus": "$650–$800 total (8 donations in first month)",
                "returningPay": "~$20 first donation/week, ~$30+ second/week",
                "specialBonuses": "Lapse donor coupons: up to ~$575 for 6th donation after 3–6 month break",
                "notes": "Funds can be transferred to bank via ACH, PayPal, CashApp, etc."
            },
            "csl": {
                "paymentMethod": "Reloadable debit card (loaded immediately post-donation)",
                "payoutFrequency": "End-of-donation load to debit card",
                "newDonorBonus": "Up to $100 first donation, up to $700 in first month",
                "returningPay": "Often $100 for first 5 donations (weight-dependent)",
                "specialBonuses": "iGive Rewards: $100 referral bonus per person",
                "notes": "Periodic bonus campaigns available"
            },
            "grifols": {
                "paymentMethod": "Prepaid card (paid after every donation)",
                "payoutFrequency": "Post-donation, up to twice weekly",
                "newDonorBonus": "$50 on 3rd donation (within 14 days), $100 on 8th (within 8 weeks)",
                "returningPay": "Up to ~$100 per donation, up to twice per week",
                "specialBonuses": "Passport program: $5 Early Bird weekly bonus, monthly thresholds earn $25–$35",
                "notes": "Bonus amounts must be claimed with staff—not auto-applied"
            },
            "octapharma": {
                "paymentMethod": "Prepaid card (loaded within 24 hours)",
                "payoutFrequency": "Within 24 hours of each donation",
                "newDonorBonus": "$75 first donation, $125 second donation",
                "returningPay": "$50 for first five, then $50–$65 per donation",
                "specialBonuses": "OctaRewards loyalty program, $50 referral bonus",
                "notes": "Payment depends on weight and frequency"
            }
        };

        // Determine brand from center name
        const lowerName = centerName.toLowerCase();
        let brand = "generic";
        
        if (lowerName.includes("biolife")) {
            brand = "biolife";
        } else if (lowerName.includes("csl")) {
            brand = "csl";
        } else if (lowerName.includes("grifols") || lowerName.includes("biomat")) {
            brand = "grifols";
        } else if (lowerName.includes("octapharma")) {
            brand = "octapharma";
        }

        return paymentDetails[brand] || {
            paymentMethod: "Cash or prepaid card (varies by location)",
            payoutFrequency: "After each donation",
            newDonorBonus: "$50-$100 first donation, up to $600 first month",
            returningPay: "$20-$50 per donation",
            specialBonuses: "Referral bonuses and loyalty programs available",
            notes: "Contact center for specific payment details"
        };
    }

    generatePaymentDetailsSection(center) {
        const paymentInfo = this.getDetailedPaymentInfo(center.name);
        
        return `
            <div class="detail-item payment-details-section">
                <span class="detail-label">💳 Payment Details</span>
                <div class="detail-value payment-details">
                    <div class="payment-method">
                        <strong>Payment Method:</strong> ${paymentInfo.paymentMethod}
                    </div>
                    <div class="payout-frequency">
                        <strong>When You Get Paid:</strong> ${paymentInfo.payoutFrequency}
                    </div>
                    <div class="new-donor-bonus">
                        <strong>New Donor Bonus:</strong> ${paymentInfo.newDonorBonus}
                    </div>
                    <div class="returning-pay">
                        <strong>Regular Pay:</strong> ${paymentInfo.returningPay}
                    </div>
                    ${paymentInfo.specialBonuses ? `
                    <div class="special-bonuses">
                        <strong>Special Bonuses:</strong> ${paymentInfo.specialBonuses}
                    </div>
                    ` : ''}
                    <div class="payment-disclaimer">
                        <em>💡 Pay and bonus rates vary by center and time—always call your local center to confirm today's offers.</em>
                    </div>
                </div>
            </div>
        `;
    }

    generateBusyTimesInfo(center) {
        // Generate realistic busy times based on typical plasma center patterns
        const busyTimes = [
            "Busiest: Weekday evenings 4-7pm, Saturday mornings",
            "Peak times: Monday/Tuesday evenings, first week of month", 
            "Quieter: Mid-week mornings 9am-12pm",
            "Less busy: Thursday/Friday mornings, late evenings",
            "Avoid: End of month (long waits), lunch hours 12-2pm"
        ];
        
        // Use center ID to consistently assign busy times
        const timeIndex = center.id ? (parseInt(center.id.toString().slice(-1)) || 0) % busyTimes.length : 0;
        const selectedTime = busyTimes[timeIndex];
        
        return `
            <div class="detail-item">
                <span class="detail-label">⏰ Best Times to Visit</span>
                <span class="detail-value busy-times-info">${selectedTime}</span>
            </div>
        `;
    }
}

// Initialize the application when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
    console.log('🚀 DOM loaded, initializing PlasmaApp...');
    try {
        window.plasmaApp = new PlasmaApp();
        console.log('✅ PlasmaApp initialized successfully');
    } catch (error) {
        console.error('❌ PlasmaApp initialization failed:', error);
    }
});

// Analytics helper functions
function trackCenterClick(centerName) {
    gtag('event', 'center_click', {
        'center_name': centerName,
        'event_category': 'engagement'
    });
}

function trackSearch(searchTerm) {
    gtag('event', 'search', {
        'search_term': searchTerm,
        'event_category': 'engagement'
    });
}