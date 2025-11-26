/**
 * Supreme Valves - Performance Optimization
 * Page load optimization, caching, and monitoring
 */

const Performance = {
    /**
     * Initialize performance optimizations
     */
    init() {
        this.preloadCriticalResources();
        this.setupServiceWorker();
        this.optimizeImages();
        this.deferNonCriticalCSS();
        this.monitorPerformance();
    },

    /**
     * Preload critical resources
     */
    preloadCriticalResources() {
        const criticalResources = [
            { href: 'styles.css', as: 'style' },
            { href: 'js/products.js', as: 'script' },
            { href: 'data/products.json', as: 'fetch', crossorigin: 'anonymous' }
        ];

        criticalResources.forEach(resource => {
            const link = document.createElement('link');
            link.rel = 'preload';
            link.href = resource.href;
            link.as = resource.as;
            if (resource.crossorigin) {
                link.crossOrigin = resource.crossorigin;
            }
            document.head.appendChild(link);
        });
    },

    /**
     * Setup service worker for offline support
     */
    async setupServiceWorker() {
        if ('serviceWorker' in navigator) {
            try {
                const registration = await navigator.serviceWorker.register('/sw.js');
                console.log('✅ Service Worker registered:', registration);
            } catch (error) {
                console.log('❌ Service Worker registration failed:', error);
            }
        }
    },

    /**
     * Optimize images with lazy loading
     */
    optimizeImages() {
        // Add loading="lazy" to all images
        document.querySelectorAll('img:not([loading])').forEach(img => {
            img.loading = 'lazy';
        });

        // Use Intersection Observer for custom lazy loading
        if ('IntersectionObserver' in window) {
            const imageObserver = new IntersectionObserver((entries) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting) {
                        const img = entry.target;
                        if (img.dataset.src) {
                            img.src = img.dataset.src;
                            img.removeAttribute('data-src');
                        }
                        imageObserver.unobserve(img);
                    }
                });
            }, {
                rootMargin: '50px 0px',
                threshold: 0.01
            });

            document.querySelectorAll('img[data-src]').forEach(img => {
                imageObserver.observe(img);
            });
        }
    },

    /**
     * Defer non-critical CSS
     */
    deferNonCriticalCSS() {
        const nonCriticalCSS = document.querySelectorAll('link[rel="stylesheet"][data-defer]');
        
        nonCriticalCSS.forEach(link => {
            link.media = 'print';
            link.onload = function() {
                this.media = 'all';
            };
        });
    },

    /**
     * Monitor performance metrics
     */
    monitorPerformance() {
        if ('PerformanceObserver' in window) {
            // Monitor Largest Contentful Paint (LCP)
            try {
                const lcpObserver = new PerformanceObserver((list) => {
                    const entries = list.getEntries();
                    const lastEntry = entries[entries.length - 1];
                    console.log('📊 LCP:', lastEntry.renderTime || lastEntry.loadTime);
                });
                lcpObserver.observe({ entryTypes: ['largest-contentful-paint'] });
            } catch (e) {
                // LCP not supported
            }

            // Monitor First Input Delay (FID)
            try {
                const fidObserver = new PerformanceObserver((list) => {
                    list.getEntries().forEach(entry => {
                        console.log('📊 FID:', entry.processingStart - entry.startTime);
                    });
                });
                fidObserver.observe({ entryTypes: ['first-input'] });
            } catch (e) {
                // FID not supported
            }

            // Monitor Cumulative Layout Shift (CLS)
            try {
                let clsScore = 0;
                const clsObserver = new PerformanceObserver((list) => {
                    list.getEntries().forEach(entry => {
                        if (!entry.hadRecentInput) {
                            clsScore += entry.value;
                        }
                    });
                    console.log('📊 CLS:', clsScore);
                });
                clsObserver.observe({ entryTypes: ['layout-shift'] });
            } catch (e) {
                // CLS not supported
            }
        }

        // Log page load time
        window.addEventListener('load', () => {
            const perfData = performance.timing;
            const pageLoadTime = perfData.loadEventEnd - perfData.navigationStart;
            const connectTime = perfData.responseEnd - perfData.requestStart;
            const renderTime = perfData.domComplete - perfData.domLoading;

            console.log('📊 Performance Metrics:');
            console.log('  Page Load Time:', pageLoadTime + 'ms');
            console.log('  Connect Time:', connectTime + 'ms');
            console.log('  Render Time:', renderTime + 'ms');
        });
    },

    /**
     * Prefetch next page
     */
    prefetchPage(url) {
        const link = document.createElement('link');
        link.rel = 'prefetch';
        link.href = url;
        document.head.appendChild(link);
    },

    /**
     * Optimize fonts
     */
    optimizeFonts() {
        // Use font-display: swap for web fonts
        const style = document.createElement('style');
        style.textContent = `
            @font-face {
                font-family: 'Inter';
                font-display: swap;
            }
        `;
        document.head.appendChild(style);
    },

    /**
     * Reduce JavaScript execution time
     */
    async deferJavaScript() {
        // Load non-critical scripts after page load
        window.addEventListener('load', () => {
            const deferredScripts = [
                'https://kit.fontawesome.com/a076d05399.js'
            ];

            deferredScripts.forEach(src => {
                const script = document.createElement('script');
                script.src = src;
                script.defer = true;
                document.body.appendChild(script);
            });
        });
    },

    /**
     * Enable resource hints
     */
    enableResourceHints() {
        // DNS prefetch for external domains
        const domains = [
            'https://fonts.googleapis.com',
            'https://cdnjs.cloudflare.com',
            'https://kit.fontawesome.com'
        ];

        domains.forEach(domain => {
            const link = document.createElement('link');
            link.rel = 'dns-prefetch';
            link.href = domain;
            document.head.appendChild(link);
        });
    },

    /**
     * Compress and cache API responses
     */
    cacheAPIResponse(key, data, expiryMinutes = 60) {
        try {
            const item = {
                data: data,
                expiry: Date.now() + (expiryMinutes * 60 * 1000),
                compressed: true
            };
            sessionStorage.setItem(key, JSON.stringify(item));
        } catch (e) {
            console.warn('Cache storage failed:', e);
        }
    },

    getCachedAPIResponse(key) {
        try {
            const item = sessionStorage.getItem(key);
            if (!item) return null;

            const parsed = JSON.parse(item);
            if (Date.now() > parsed.expiry) {
                sessionStorage.removeItem(key);
                return null;
            }

            return parsed.data;
        } catch (e) {
            return null;
        }
    }
};

// Auto-initialize performance optimizations
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', () => Performance.init());
} else {
    Performance.init();
}

// Export for use in other modules
window.Performance = Performance;
