// Product Search and Filter Functionality
class ProductSearch {
    constructor() {
        this.products = allProducts || [];
        this.filteredProducts = [...this.products];
        this.currentCategory = 'all';
        this.searchQuery = '';
    }

    // Search products by query
    search(query) {
        this.searchQuery = query.toLowerCase().trim();
        this.applyFilters();
        return this.filteredProducts;
    }

    // Filter by category
    filterByCategory(categoryKey) {
        this.currentCategory = categoryKey;
        this.applyFilters();
        return this.filteredProducts;
    }

    // Apply all active filters
    applyFilters() {
        this.filteredProducts = this.products.filter(product => {
            // Category filter
            const categoryMatch = this.currentCategory === 'all' || 
                                product.categoryKey === this.currentCategory;

            // Search query filter
            const searchMatch = !this.searchQuery || 
                              product.name.toLowerCase().includes(this.searchQuery) ||
                              product.category.toLowerCase().includes(this.searchQuery) ||
                              (product.tags && product.tags.some(tag => 
                                  tag.toLowerCase().includes(this.searchQuery)));

            return categoryMatch && searchMatch;
        });
    }

    // Get search suggestions
    getSuggestions(query, limit = 5) {
        const q = query.toLowerCase().trim();
        if (!q) return [];

        const suggestions = this.products
            .filter(product => 
                product.name.toLowerCase().includes(q) ||
                product.category.toLowerCase().includes(q) ||
                (product.tags && product.tags.some(tag => tag.toLowerCase().includes(q)))
            )
            .slice(0, limit);

        return suggestions;
    }

    // Get products by tag
    getByTag(tag) {
        return this.products.filter(product => 
            product.tags && product.tags.includes(tag)
        );
    }

    // Get all unique tags
    getAllTags() {
        const tags = new Set();
        this.products.forEach(product => {
            if (product.tags) {
                product.tags.forEach(tag => tags.add(tag));
            }
        });
        return Array.from(tags).sort();
    }

    // Reset all filters
    reset() {
        this.currentCategory = 'all';
        this.searchQuery = '';
        this.filteredProducts = [...this.products];
        return this.filteredProducts;
    }
}

// Initialize search instance
const productSearch = new ProductSearch();

// Render product cards
function renderProductCard(product) {
    return `
        <a href="${product.url}" class="product-card-new">
            <div class="product-card-icon">
                <i class="fas ${product.categoryIcon}"></i>
            </div>
            <h3>${product.name}</h3>
            <p class="product-category">${product.category}</p>
            ${product.tags && product.tags.length > 0 ? `
                <div class="product-tags">
                    ${product.tags.slice(0, 3).map(tag => 
                        `<span class="product-tag">${tag}</span>`
                    ).join('')}
                </div>
            ` : ''}
            <span class="product-link-arrow">View Details →</span>
        </a>
    `;
}

// Render category filters
function renderCategoryFilters() {
    const filterContainer = document.getElementById('category-filter');
    if (!filterContainer) return;

    const categories = Object.keys(productCategories);
    
    let html = `
        <div class="category-filters">
            <button class="category-btn active" data-category="all">
                <i class="fas fa-th"></i>
                All Products
                <span class="count">${allProducts.length}</span>
            </button>
    `;

    categories.forEach(categoryKey => {
        const category = productCategories[categoryKey];
        html += `
            <button class="category-btn" data-category="${categoryKey}">
                <i class="fas ${category.icon}"></i>
                ${category.name}
                <span class="count">${category.products.length}</span>
            </button>
        `;
    });

    html += '</div>';
    filterContainer.innerHTML = html;

    // Add click handlers
    document.querySelectorAll('.category-btn').forEach(btn => {
        btn.addEventListener('click', function() {
            document.querySelectorAll('.category-btn').forEach(b => b.classList.remove('active'));
            this.classList.add('active');
            
            const category = this.dataset.category;
            const results = productSearch.filterByCategory(category);
            renderProducts(results);
        });
    });
}

// Render products grid
function renderProducts(products) {
    const grid = document.getElementById('all-products-grid');
    if (!grid) return;

    if (products.length === 0) {
        grid.innerHTML = `
            <div class="no-results">
                <i class="fas fa-search" style="font-size: 3rem; color: var(--text-light); margin-bottom: 1rem;"></i>
                <h3>No products found</h3>
                <p>Try adjusting your search or filters</p>
            </div>
        `;
        return;
    }

    grid.innerHTML = products.map(product => renderProductCard(product)).join('');
}

// Initialize search bar in header
function initializeSearchBar() {
    const nav = document.querySelector('header nav ul');
    if (!nav) return;

    // Create search container
    const searchLi = document.createElement('li');
    searchLi.className = 'search-container';
    searchLi.innerHTML = `
        <div class="search-wrapper">
            <input type="text" 
                   id="product-search-input" 
                   placeholder="Search products..." 
                   autocomplete="off">
            <i class="fas fa-search search-icon"></i>
            <div id="search-suggestions" class="search-suggestions"></div>
        </div>
    `;

    // Insert before contact link
    const contactLi = Array.from(nav.children).find(li => 
        li.querySelector('a[href="contact.html"]')
    );
    if (contactLi) {
        nav.insertBefore(searchLi, contactLi);
    } else {
        nav.appendChild(searchLi);
    }

    // Add search functionality
    const searchInput = document.getElementById('product-search-input');
    const suggestionsDiv = document.getElementById('search-suggestions');

    let searchTimeout;
    searchInput.addEventListener('input', function() {
        clearTimeout(searchTimeout);
        const query = this.value;

        searchTimeout = setTimeout(() => {
            if (query.length >= 2) {
                const suggestions = productSearch.getSuggestions(query, 8);
                showSuggestions(suggestions, suggestionsDiv);
            } else {
                suggestionsDiv.style.display = 'none';
            }
        }, 300);
    });

    searchInput.addEventListener('keypress', function(e) {
        if (e.key === 'Enter') {
            const query = this.value;
            if (query.trim()) {
                window.location.href = `products.html?search=${encodeURIComponent(query)}`;
            }
        }
    });

    // Close suggestions when clicking outside
    document.addEventListener('click', function(e) {
        if (!searchLi.contains(e.target)) {
            suggestionsDiv.style.display = 'none';
        }
    });
}

// Show search suggestions
function showSuggestions(suggestions, container) {
    if (suggestions.length === 0) {
        container.style.display = 'none';
        return;
    }

    container.innerHTML = suggestions.map(product => `
        <a href="${product.url}" class="suggestion-item">
            <i class="fas ${product.categoryIcon}"></i>
            <div>
                <div class="suggestion-name">${product.name}</div>
                <div class="suggestion-category">${product.category}</div>
            </div>
        </a>
    `).join('');

    container.style.display = 'block';
}

// Handle URL search parameters
function handleURLSearch() {
    const urlParams = new URLSearchParams(window.location.search);
    const searchQuery = urlParams.get('search');
    const categoryFilter = urlParams.get('category');

    if (searchQuery) {
        const results = productSearch.search(searchQuery);
        renderProducts(results);
        
        // Update page title
        const title = document.querySelector('h1.section-title');
        if (title) {
            title.textContent = `Search Results for "${searchQuery}"`;
        }
    } else if (categoryFilter) {
        const results = productSearch.filterByCategory(categoryFilter);
        renderProducts(results);
        
        // Activate category button
        const categoryBtn = document.querySelector(`[data-category="${categoryFilter}"]`);
        if (categoryBtn) {
            document.querySelectorAll('.category-btn').forEach(b => b.classList.remove('active'));
            categoryBtn.classList.add('active');
        }
    } else {
        renderProducts(allProducts);
    }
}

// Initialize on page load
document.addEventListener('DOMContentLoaded', function() {
    // Initialize search bar in header
    initializeSearchBar();

    // Only run on products page
    if (window.location.pathname.includes('products.html')) {
        renderCategoryFilters();
        handleURLSearch();
    }
});
