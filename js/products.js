/**
 * Supreme Valves - Product Management System
 * Dynamically loads and renders products from JSON data
 */

class ProductManager {
    constructor() {
        this.products = [];
        this.productsData = null;
    }

    /**
     * Load products from JSON file
     */
    async loadProducts() {
        if (this.products.length > 0) {
            return this.products; // Already loaded
        }
        
        try {
            // Determine the correct path based on current location
            const path = window.location.pathname;
            let jsonPath = 'data/products.json';
            
            // Comprehensive path detection for all subdirectories
            const pathParts = path.split('/').filter(p => p.length > 0);
            const isInSubdir = pathParts.length > 0 && !path.endsWith('index.html') && !path.endsWith('.html');
            const depth = pathParts.length;
            
            // Simple depth detection based on directory structure
            if (path.includes('/products/') || path.includes('/blog/') || path.includes('/faqs/') || path.includes('/projects/') || path.includes('/countries/') || path.includes('/docs/')) {
                jsonPath = '../data/products.json';
                // Handle deeper nested docs
                if (path.includes('/technical-resources/')) {
                    jsonPath = '../../data/products.json';
                }
            }
            
            const response = await fetch(jsonPath);
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            this.productsData = await response.json();
            this.products = this.productsData.products;
            console.log('Products loaded:', this.products.length);
            return this.products;
        } catch (error) {
            console.error('Error loading products:', error);
            return [];
        }
    }

    /**
     * Get featured products for homepage
     */
    getFeaturedProducts(limit = null) {
        const featured = this.products.filter(p => p.featured);
        return limit ? featured.slice(0, limit) : featured;
    }

    /**
     * Get all products
     */
    getAllProducts() {
        return this.products;
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
     * Render product card HTML
     */
    renderProductCard(product) {
        // Adjust URL path based on current location
        const currentPath = window.location.pathname;
        let productUrl = `products/${product.id}.html`;
        
        // Comprehensive relative path handling
        if (currentPath.includes('/products/')) {
            productUrl = `${product.id}.html`;
        } else if (currentPath.includes('/blog/') || currentPath.includes('/faqs/') || currentPath.includes('/projects/') || currentPath.includes('/countries/')) {
            productUrl = `../products/${product.id}.html`;
        } else if (currentPath.includes('/technical-resources/')) {
            productUrl = `../../products/${product.id}.html`;
        }
        
        return `
            <a href="${productUrl}" class="product-card-new">
                <div class="product-card-icon">
                    <i class="fas ${product.categoryIcon || 'fa-cog'}"></i>
                </div>
                <h3>${product.shortName || product.name}</h3>
                <p class="product-category">${product.category}</p>
                ${product.tags && product.tags.length > 0 ? `
                    <div class="product-tags">
                        ${product.tags.slice(0, 3).map(tag => 
                            `<span class="product-tag">${tag}</span>`
                        ).join('')}
                    </div>
                ` : ''}
                <span class="product-link-arrow">View Details</span>
            </a>
        `;
    }

    /**
     * Render products to a container
     */
    renderProducts(containerId, products) {
        const container = document.getElementById(containerId);
        if (!container) {
            console.error(`Container ${containerId} not found`);
            return;
        }

        if (!products || products.length === 0) {
            container.innerHTML = '<p style="text-align: center; padding: 3rem; color: #666;">No products found.</p>';
            console.warn('No products to render');
            return;
        }

        const html = products.map(product => this.renderProductCard(product)).join('');
        container.innerHTML = html;
        console.log(`Rendered ${products.length} products to ${containerId}`);
    }

    /**
     * Render featured products on homepage
     */
    async renderFeaturedProducts(containerId = 'featured-products-grid') {
        await this.loadProducts();
        const featured = this.getFeaturedProducts();
        this.renderProducts(containerId, featured);
    }

    /**
     * Render all products on products page
     */
    async renderAllProducts(containerId = 'all-products-grid') {
        await this.loadProducts();
        this.renderProducts(containerId, this.products);
    }

    /**
     * Render products by category
     */
    async renderProductsByCategory(category, containerId) {
        await this.loadProducts();
        const products = this.getProductsByCategory(category);
        this.renderProducts(containerId, products);
    }

    /**
     * Get unique categories
     */
    getCategories() {
        const categories = [...new Set(this.products.map(p => p.category))];
        return categories.sort();
    }

    /**
     * Render category filter
     */
    renderCategoryFilter(containerId = 'category-filter') {
        const container = document.getElementById(containerId);
        if (!container) return;

        const categories = this.getCategories();
        const html = `
            <div class="category-filter-buttons">
                <button class="filter-btn active" data-category="all">All Products</button>
                ${categories.map(cat => `
                    <button class="filter-btn" data-category="${cat}">${cat}</button>
                `).join('')}
            </div>
        `;
        container.innerHTML = html;

        // Add click handlers
        container.querySelectorAll('.filter-btn').forEach(btn => {
            btn.addEventListener('click', (e) => {
                // Update active state
                container.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
                e.target.classList.add('active');

                // Filter products
                const category = e.target.dataset.category;
                const filteredProducts = category === 'all' 
                    ? this.products 
                    : this.getProductsByCategory(category);
                this.renderProducts('all-products-grid', filteredProducts);
            });
        });
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
            p.category.toLowerCase().includes(lowerQuery)
        );
    }

    /**
     * Render Two-Fold Category Menu (for homepage)
     */
    async renderCategoryFoldMenu(containerId = 'category-fold-container') {
        const container = document.getElementById(containerId);
        if (!container) return;

        await this.loadProducts();
        
        // Get categories from products-data.js if available, otherwise from products.json
        let categories = {};
        if (typeof productCategories !== 'undefined') {
            categories = productCategories;
        } else {
            // Fallback: Group products by category from this.products
            const uniqueCategories = [...new Set(this.products.map(p => p.category))];
            uniqueCategories.forEach(cat => {
                categories[cat.toLowerCase().replace(/\s+/g, '-')] = {
                    name: cat,
                    icon: 'fa-valve',
                    products: this.products.filter(p => p.category === cat).map(p => ({
                        name: p.shortName,
                        url: `products/${p.id}.html`
                    }))
                };
            });
        }

        const categoryKeys = Object.keys(categories);
        if (categoryKeys.length === 0) return;

        const sidebarHtml = categoryKeys.map((key, index) => `
            <div class="category-sidebar-item ${index === 0 ? 'active' : ''}" data-category-key="${key}">
                <i class="fas ${categories[key].icon || 'fa-cog'}"></i>
                <span>${categories[key].name}</span>
            </div>
        `).join('');

        container.innerHTML = `
            <div class="category-sidebar">
                ${sidebarHtml}
            </div>
            <div class="product-display-area">
                <div class="product-display-header">
                    <h3 id="selected-category-name">${categories[categoryKeys[0]].name}</h3>
                </div>
                <div class="product-display-grid" id="fold-products-grid">
                    <!-- Products will be loaded here -->
                </div>
            </div>
        `;

        // Function to update products in the display area
        const updateProducts = (key) => {
            const category = categories[key];
            document.getElementById('selected-category-name').textContent = category.name;
            const grid = document.getElementById('fold-products-grid');
            
            // Adjust paths based on current location
            const currentPath = window.location.pathname;
            const isSubdir = currentPath.includes('/products/') || currentPath.includes('/blog/') || currentPath.includes('/faqs/');
            
            grid.innerHTML = category.products.map(p => {
                let url = p.url;
                if (isSubdir && !url.startsWith('http') && !url.startsWith('../')) {
                    url = '../' + url;
                }
                return `
                    <a href="${url}" class="mini-product-card">
                        <h4>${p.name}</h4>
                        <span class="view-link">View Details <i class="fas fa-chevron-right"></i></span>
                    </a>
                `;
            }).join('');
        };

        // Initialize first category
        updateProducts(categoryKeys[0]);

        // Add click handlers to sidebar items
        container.querySelectorAll('.category-sidebar-item').forEach(item => {
            item.addEventListener('click', (e) => {
                const target = e.currentTarget;
                container.querySelectorAll('.category-sidebar-item').forEach(i => i.classList.remove('active'));
                target.classList.add('active');
                updateProducts(target.dataset.categoryKey);
            });
        });
    }
}

// Create global instance
const productManager = new ProductManager();

// Auto-initialize on page load
document.addEventListener('DOMContentLoaded', () => {
    console.log('ProductManager initialized');
    
    // Check which page we're on and render accordingly
    const featuredContainer = document.getElementById('featured-products-grid');
    const allProductsContainer = document.getElementById('all-products-grid');
    const categoryFilter = document.getElementById('category-filter');
    const footerProductsList = document.getElementById('footer-products-list');
    
    console.log('Containers found:', {
        featured: !!featuredContainer,
        allProducts: !!allProductsContainer,
        categoryFilter: !!categoryFilter,
        footer: !!footerProductsList
    });

    if (featuredContainer) {
        productManager.renderFeaturedProducts();
    }

    if (allProductsContainer) {
        productManager.renderAllProducts();
    }

    if (categoryFilter) {
        productManager.loadProducts().then(() => {
            productManager.renderCategoryFilter();
        });
    }

    const categoryFoldContainer = document.getElementById('category-fold-container');
    if (categoryFoldContainer) {
        productManager.renderCategoryFoldMenu();
    }

    // Populate footer with all products
    if (footerProductsList) {
        productManager.loadProducts().then(() => {
            const products = productManager.getAllProducts();
            console.log('Footer products:', products.length);
            if (products && products.length > 0) {
                // Determine correct path prefix based on current location
                const path = window.location.pathname;
                let pathPrefix = 'products/';
                
                if (path.includes('/products/')) {
                    pathPrefix = '';
                } else if (path.includes('/blog/') || path.includes('/faqs/') || path.includes('/projects/') || path.includes('/countries/')) {
                    pathPrefix = '../products/';
                } else if (path.includes('/technical-resources/')) {
                    pathPrefix = '../../products/';
                }
                
                const html = products.map(product => 
                    `<li><a href="${pathPrefix}${product.id}.html">${product.shortName}</a></li>`
                ).join('');
                footerProductsList.innerHTML = html;
            } else {
                footerProductsList.innerHTML = '<li>Loading products...</li>';
            }
        }).catch(error => {
            console.error('Error loading footer products:', error);
            footerProductsList.innerHTML = '<li>Error loading products</li>';
        });
    }

    // Populate header dropdown with all products
    const productsDropdown = document.getElementById('products-dropdown');
    if (productsDropdown) {
        productManager.loadProducts().then(() => {
            const products = productManager.getAllProducts();
            // Determine correct path prefix based on current location
            const path = window.location.pathname;
            let pathPrefix = 'products/';
            
            if (path.includes('/products/')) {
                pathPrefix = '';
            } else if (path.includes('/blog/') || path.includes('/faqs/') || path.includes('/projects/') || path.includes('/countries/')) {
                pathPrefix = '../products/';
            } else if (path.includes('/technical-resources/')) {
                pathPrefix = '../../products/';
            }
            
            const html = products.map(product => 
                `<a href="${pathPrefix}${product.id}.html">${product.shortName}</a>`
            ).join('');
            productsDropdown.innerHTML = html;
        }).catch(error => {
            console.error('Error loading dropdown products:', error);
            productsDropdown.innerHTML = '<a href="products.html">View All Products</a>';
        });
    }
});
