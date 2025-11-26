/**
 * Supreme Valves - Optimized Product Management System
 * Modular, cached, and performance-optimized
 */

class ProductManager {
    constructor() {
        this.products = [];
        this.productsData = null;
        this.cache = new Map();
        this.observers = [];
    }

    /**
     * Load products with caching
     */
    async loadProducts() {
        // Return cached data if available
        if (this.products.length > 0) {
            return this.products;
        }

        // Check sessionStorage cache
        const cached = sessionStorage.getItem('products_cache');
        if (cached) {
            try {
                this.productsData = JSON.parse(cached);
                this.products = this.productsData.products;
                console.log('✅ Products loaded from cache:', this.products.length);
                return this.products;
            } catch (e) {
                console.warn('Cache parse error, fetching fresh data');
            }
        }

        // Fetch fresh data
        try {
            const path = this.getBasePath();
            const jsonPath = `${path}data/products.json`;
            
            const response = await fetch(jsonPath);
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            
            this.productsData = await response.json();
            this.products = this.productsData.products;
            
            // Cache in sessionStorage
            sessionStorage.setItem('products_cache', JSON.stringify(this.productsData));
            
            console.log('✅ Products loaded from API:', this.products.length);
            return this.products;
        } catch (error) {
            console.error('❌ Error loading products:', error);
            return [];
        }
    }

    /**
     * Get base path
     */
    getBasePath() {
        const path = window.location.pathname;
        if (path.includes('/products/')) {
            return '../';
        } else if (path.includes('/faqs/') || path.includes('/docs/')) {
            return '../';
        }
        return '';
    }

    /**
     * Get all products
     */
    getAllProducts() {
        return this.products;
    }

    /**
     * Get featured products
     */
    getFeaturedProducts(limit = null) {
        const featured = this.products.filter(p => p.featured);
        return limit ? featured.slice(0, limit) : featured;
    }

    /**
     * Get products by category
     */
    getProductsByCategory(category) {
        return this.products.filter(p => p.category === category);
    }

    /**
     * Get product by ID
     */
    getProductById(id) {
        return this.products.find(p => p.id === id);
    }

    /**
     * Render products with lazy loading
     */
    renderProducts(containerId, products, options = {}) {
        const container = document.getElementById(containerId);
        if (!container) return;

        const basePath = this.getBasePath();
        const { lazyLoad = true } = options;

        const html = products.map(product => {
            const imgSrc = lazyLoad ? '' : `${basePath}${product.image}`;
            const imgDataSrc = lazyLoad ? `data-src="${basePath}${product.image}"` : '';
            const imgClass = lazyLoad ? 'lazy-load' : '';

            return `
                <div class="product-card">
                    <img src="${imgSrc}" ${imgDataSrc} class="${imgClass}" alt="${product.name}">
                    <h3>${product.shortName}</h3>
                    <p>${product.description}</p>
                    <a href="${basePath}products/${product.id}.html" class="btn btn-secondary">View Details</a>
                </div>
            `;
        }).join('');

        container.innerHTML = html;

        // Initialize lazy loading
        if (lazyLoad) {
            this.initLazyLoading(container);
        }
    }

    /**
     * Initialize lazy loading for images
     */
    initLazyLoading(container) {
        const images = container.querySelectorAll('img.lazy-load');
        
        if ('IntersectionObserver' in window) {
            const imageObserver = new IntersectionObserver((entries, observer) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting) {
                        const img = entry.target;
                        img.src = img.dataset.src;
                        img.classList.remove('lazy-load');
                        imageObserver.unobserve(img);
                    }
                });
            });

            images.forEach(img => imageObserver.observe(img));
        } else {
            // Fallback for older browsers
            images.forEach(img => {
                img.src = img.dataset.src;
                img.classList.remove('lazy-load');
            });
        }
    }

    /**
     * Render featured products
     */
    async renderFeaturedProducts(limit = 6) {
        await this.loadProducts();
        const featured = this.getFeaturedProducts(limit);
        this.renderProducts('featured-products-grid', featured);
    }

    /**
     * Render all products
     */
    async renderAllProducts() {
        await this.loadProducts();
        this.renderProducts('all-products-grid', this.products);
    }

    /**
     * Render category filter
     */
    async renderCategoryFilter() {
        await this.loadProducts();
        
        const categories = [...new Set(this.products.map(p => p.category))];
        const filterContainer = document.getElementById('category-filter');
        
        if (!filterContainer) return;

        const html = `
            <button class="filter-btn active" data-category="all">All Products</button>
            ${categories.map(cat => 
                `<button class="filter-btn" data-category="${cat}">${cat}</button>`
            ).join('')}
        `;

        filterContainer.innerHTML = html;

        // Add event listeners
        filterContainer.querySelectorAll('.filter-btn').forEach(btn => {
            btn.addEventListener('click', (e) => {
                // Update active state
                filterContainer.querySelectorAll('.filter-btn').forEach(b => 
                    b.classList.remove('active')
                );
                e.target.classList.add('active');

                // Filter products
                const category = e.target.dataset.category;
                const filtered = category === 'all' 
                    ? this.products 
                    : this.getProductsByCategory(category);
                
                this.renderProducts('all-products-grid', filtered);
            });
        });
    }

    /**
     * Populate dropdown
     */
    async populateDropdown() {
        await this.loadProducts();
        
        const dropdown = document.getElementById('products-dropdown');
        if (!dropdown) return;

        const basePath = this.getBasePath();
        const html = this.products.map(product => 
            `<a href="${basePath}products/${product.id}.html">${product.shortName}</a>`
        ).join('');
        
        dropdown.innerHTML = html;
    }

    /**
     * Populate footer products
     */
    async populateFooter() {
        await this.loadProducts();
        
        const footerList = document.getElementById('footer-products-list');
        if (!footerList) return;

        const basePath = this.getBasePath();
        const html = this.products.map(product => 
            `<li><a href="${basePath}products/${product.id}.html">${product.shortName}</a></li>`
        ).join('');
        
        footerList.innerHTML = html;
    }

    /**
     * Initialize all product displays
     */
    async init() {
        await this.loadProducts();
        
        // Check which elements exist and populate them
        if (document.getElementById('featured-products-grid')) {
            this.renderFeaturedProducts();
        }
        
        if (document.getElementById('all-products-grid')) {
            this.renderAllProducts();
        }
        
        if (document.getElementById('category-filter')) {
            this.renderCategoryFilter();
        }
        
        if (document.getElementById('products-dropdown')) {
            this.populateDropdown();
        }
        
        if (document.getElementById('footer-products-list')) {
            this.populateFooter();
        }
    }
}

// Create global instance
window.productManager = new ProductManager();

// Auto-initialize on page load
document.addEventListener('DOMContentLoaded', () => {
    window.productManager.init();
});
