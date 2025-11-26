/**
 * Supreme Valves - Product Renderer Module
 * Automatically renders products across all pages from products.json
 * Add a product once in products.json - it appears everywhere automatically
 */

class ProductRenderer {
    constructor() {
        this.products = [];
        this.categories = new Set();
        this.basePath = this.getBasePath();
    }

    /**
     * Get base path based on current location
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
     * Load products from JSON with caching
     */
    async loadProducts() {
        // Check cache first
        const cached = sessionStorage.getItem('products_data');
        if (cached) {
            try {
                const data = JSON.parse(cached);
                this.products = data.products;
                this.extractCategories();
                console.log('✅ Products loaded from cache:', this.products.length);
                return this.products;
            } catch (e) {
                console.warn('Cache parse error, fetching fresh data');
            }
        }

        // Fetch from API
        try {
            const response = await fetch(`${this.basePath}data/products.json`);
            if (!response.ok) throw new Error(`HTTP error! status: ${response.status}`);
            
            const data = await response.json();
            this.products = data.products;
            this.extractCategories();
            
            // Cache the data
            sessionStorage.setItem('products_data', JSON.stringify(data));
            
            console.log('✅ Products loaded from API:', this.products.length);
            return this.products;
        } catch (error) {
            console.error('❌ Error loading products:', error);
            return [];
        }
    }

    /**
     * Extract unique categories
     */
    extractCategories() {
        this.categories = new Set(this.products.map(p => p.category));
    }

    /**
     * Render featured products on homepage
     */
    renderFeaturedProducts(containerId = 'featured-products-grid', limit = 12) {
        const container = document.getElementById(containerId);
        if (!container) return;

        const featured = this.products.filter(p => p.featured).slice(0, limit);
        
        const html = featured.map(product => `
            <div class="product-card" data-category="${product.category}">
                <img src="${this.basePath}${product.image}" alt="${product.name}" loading="lazy">
                <h3>${product.shortName}</h3>
                <p>${product.description}</p>
                <a href="${this.basePath}products/${product.id}.html" class="btn btn-secondary">View Details</a>
            </div>
        `).join('');

        container.innerHTML = html;
    }

    /**
     * Render all products with category filter
     */
    renderAllProducts(containerId = 'all-products-grid') {
        const container = document.getElementById(containerId);
        if (!container) return;

        const html = this.products.map(product => `
            <div class="product-card" data-category="${product.category}">
                <img src="${this.basePath}${product.image}" alt="${product.name}" loading="lazy">
                <h3>${product.shortName}</h3>
                <p>${product.description}</p>
                <a href="${this.basePath}products/${product.id}.html" class="btn btn-secondary">View Details</a>
            </div>
        `).join('');

        container.innerHTML = html;
    }

    /**
     * Render category filter buttons
     */
    renderCategoryFilter(containerId = 'category-filter') {
        const container = document.getElementById(containerId);
        if (!container) return;

        const categories = Array.from(this.categories).sort();
        
        const html = `
            <button class="filter-btn active" data-category="all">All Products (${this.products.length})</button>
            ${categories.map(cat => {
                const count = this.products.filter(p => p.category === cat).length;
                return `<button class="filter-btn" data-category="${cat}">${cat} (${count})</button>`;
            }).join('')}
        `;

        container.innerHTML = html;

        // Add event listeners
        container.querySelectorAll('.filter-btn').forEach(btn => {
            btn.addEventListener('click', (e) => {
                // Update active state
                container.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
                e.target.classList.add('active');

                // Filter products
                const category = e.target.dataset.category;
                this.filterProducts(category);
            });
        });
    }

    /**
     * Filter products by category
     */
    filterProducts(category) {
        const cards = document.querySelectorAll('.product-card');
        
        cards.forEach(card => {
            if (category === 'all' || card.dataset.category === category) {
                card.style.display = '';
                card.style.animation = 'fadeIn 0.3s ease';
            } else {
                card.style.display = 'none';
            }
        });
    }

    /**
     * Render products dropdown in header
     */
    renderProductsDropdown(containerId = 'products-dropdown') {
        const dropdown = document.getElementById(containerId);
        if (!dropdown) return;

        const html = this.products.map(product => 
            `<a href="${this.basePath}products/${product.id}.html">${product.shortName}</a>`
        ).join('');

        dropdown.innerHTML = html;
    }

    /**
     * Render footer products list
     */
    renderFooterProducts(containerId = 'footer-products-list') {
        const footerList = document.getElementById(containerId);
        if (!footerList) return;

        const html = this.products.map(product => 
            `<li><a href="${this.basePath}products/${product.id}.html">${product.shortName}</a></li>`
        ).join('');

        footerList.innerHTML = html;
    }

    /**
     * Render related products (same category, exclude current)
     */
    renderRelatedProducts(currentProductId, containerId = 'related-products', limit = 4) {
        const container = document.getElementById(containerId);
        if (!container) return;

        const currentProduct = this.products.find(p => p.id === currentProductId);
        if (!currentProduct) return;

        // Get products from same category, excluding current
        const related = this.products
            .filter(p => p.category === currentProduct.category && p.id !== currentProductId)
            .slice(0, limit);

        if (related.length === 0) {
            container.style.display = 'none';
            return;
        }

        const html = `
            <h2 class="section-title">Related Products</h2>
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 2rem; margin-top: 2rem;">
                ${related.map(product => `
                    <div class="product-card">
                        <img src="${this.basePath}${product.image}" alt="${product.name}" loading="lazy">
                        <h3>${product.shortName}</h3>
                        <p>${product.description}</p>
                        <a href="${this.basePath}products/${product.id}.html" class="btn btn-secondary">View Details</a>
                    </div>
                `).join('')}
            </div>
        `;

        container.innerHTML = html;
    }

    /**
     * Render product breadcrumb
     */
    renderBreadcrumb(productId, containerId = 'breadcrumb') {
        const container = document.getElementById(containerId);
        if (!container) return;

        const product = this.products.find(p => p.id === productId);
        if (!product) return;

        const html = `
            <nav style="font-size: 0.9rem; color: var(--text-light);">
                <a href="${this.basePath}index.html" style="color: var(--accent-color);">Home</a> / 
                <a href="${this.basePath}products.html" style="color: var(--accent-color);">Products</a> / 
                <a href="${this.basePath}products.html?category=${encodeURIComponent(product.category)}" style="color: var(--accent-color);">${product.category}</a> / 
                <span>${product.shortName}</span>
            </nav>
        `;

        container.innerHTML = html;
    }

    /**
     * Get product by ID
     */
    getProduct(productId) {
        return this.products.find(p => p.id === productId);
    }

    /**
     * Get products by category
     */
    getProductsByCategory(category) {
        return this.products.filter(p => p.category === category);
    }

    /**
     * Search products
     */
    searchProducts(query) {
        const lowerQuery = query.toLowerCase();
        return this.products.filter(p => 
            p.name.toLowerCase().includes(lowerQuery) ||
            p.shortName.toLowerCase().includes(lowerQuery) ||
            p.description.toLowerCase().includes(lowerQuery) ||
            p.category.toLowerCase().includes(lowerQuery) ||
            p.applications.some(app => app.toLowerCase().includes(lowerQuery))
        );
    }

    /**
     * Render search results
     */
    renderSearchResults(query, containerId = 'search-results') {
        const container = document.getElementById(containerId);
        if (!container) return;

        const results = this.searchProducts(query);

        if (results.length === 0) {
            container.innerHTML = `
                <div style="text-align: center; padding: 3rem;">
                    <i class="fas fa-search" style="font-size: 3rem; color: var(--text-light); margin-bottom: 1rem;"></i>
                    <h3>No products found for "${query}"</h3>
                    <p>Try different keywords or browse all products</p>
                    <a href="${this.basePath}products.html" class="btn btn-primary">View All Products</a>
                </div>
            `;
            return;
        }

        const html = `
            <h2 class="section-title">Search Results for "${query}" (${results.length})</h2>
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 2rem; margin-top: 2rem;">
                ${results.map(product => `
                    <div class="product-card">
                        <img src="${this.basePath}${product.image}" alt="${product.name}" loading="lazy">
                        <h3>${product.shortName}</h3>
                        <p>${product.description}</p>
                        <a href="${this.basePath}products/${product.id}.html" class="btn btn-secondary">View Details</a>
                    </div>
                `).join('')}
            </div>
        `;

        container.innerHTML = html;
    }

    /**
     * Auto-initialize based on page elements
     */
    async autoInit() {
        await this.loadProducts();

        // Homepage featured products
        if (document.getElementById('featured-products-grid')) {
            this.renderFeaturedProducts();
        }

        // Products page
        if (document.getElementById('all-products-grid')) {
            this.renderAllProducts();
        }

        // Category filter
        if (document.getElementById('category-filter')) {
            this.renderCategoryFilter();
        }

        // Products dropdown (header)
        if (document.getElementById('products-dropdown')) {
            this.renderProductsDropdown();
        }

        // Footer products
        if (document.getElementById('footer-products-list')) {
            this.renderFooterProducts();
        }

        // Related products (on product pages)
        const relatedContainer = document.getElementById('related-products');
        if (relatedContainer && relatedContainer.dataset.productId) {
            this.renderRelatedProducts(relatedContainer.dataset.productId);
        }

        // Breadcrumb (on product pages)
        const breadcrumbContainer = document.getElementById('breadcrumb');
        if (breadcrumbContainer && breadcrumbContainer.dataset.productId) {
            this.renderBreadcrumb(breadcrumbContainer.dataset.productId);
        }

        // Search results
        const searchContainer = document.getElementById('search-results');
        if (searchContainer) {
            const urlParams = new URLSearchParams(window.location.search);
            const query = urlParams.get('q');
            if (query) {
                this.renderSearchResults(query);
            }
        }

        // Category filter from URL
        const urlParams = new URLSearchParams(window.location.search);
        const categoryParam = urlParams.get('category');
        if (categoryParam && document.getElementById('all-products-grid')) {
            this.filterProducts(categoryParam);
            // Update active filter button
            const filterBtn = document.querySelector(`[data-category="${categoryParam}"]`);
            if (filterBtn) {
                document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
                filterBtn.classList.add('active');
            }
        }
    }
}

// Create global instance
window.productRenderer = new ProductRenderer();

// Auto-initialize on page load
document.addEventListener('DOMContentLoaded', () => {
    window.productRenderer.autoInit();
});
