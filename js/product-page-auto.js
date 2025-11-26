/**
 * Supreme Valves - Product Page Auto-Loader
 * Automatically generates product page elements from products.json
 */

class ProductPageAuto {
    constructor() {
        this.productId = null;
        this.product = null;
        this.basePath = '../';
    }

    /**
     * Get product ID from body data attribute or URL
     */
    getProductId() {
        // Try body data attribute first
        const bodyProductId = document.body.dataset.productId;
        if (bodyProductId) return bodyProductId;

        // Try to extract from URL
        const path = window.location.pathname;
        const match = path.match(/products\/([^\/]+)\.html/);
        return match ? match[1] : null;
    }

    /**
     * Load product data
     */
    async loadProduct() {
        this.productId = this.getProductId();
        if (!this.productId) {
            console.warn('No product ID found');
            return null;
        }

        // Wait for productRenderer to load
        if (!window.productRenderer || !window.productRenderer.products.length) {
            await window.productRenderer.loadProducts();
        }

        this.product = window.productRenderer.getProduct(this.productId);
        return this.product;
    }

    /**
     * Update page title and meta tags
     */
    updateMetaTags() {
        if (!this.product) return;

        // Update title
        document.title = `${this.product.name} | Supreme Valves India`;
        
        // Update or create meta description
        let metaDesc = document.querySelector('meta[name="description"]');
        if (!metaDesc) {
            metaDesc = document.createElement('meta');
            metaDesc.name = 'description';
            document.head.appendChild(metaDesc);
        }
        metaDesc.content = `${this.product.description} - ${this.product.applications.join(', ')}. Premium quality from Supreme Valves India.`;

        // Update or create meta keywords
        let metaKeywords = document.querySelector('meta[name="keywords"]');
        if (!metaKeywords) {
            metaKeywords = document.createElement('meta');
            metaKeywords.name = 'keywords';
            document.head.appendChild(metaKeywords);
        }
        metaKeywords.content = `${this.product.name}, ${this.product.shortName}, ${this.product.category}, ${this.product.applications.join(', ')}`;
    }

    /**
     * Generate product header
     */
    generateProductHeader() {
        if (!this.product) return '';

        return `
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 3rem; margin-bottom: 4rem;">
                <div>
                    <img src="${this.basePath}${this.product.image}" alt="${this.product.name}" style="width: 100%; border-radius: 12px; box-shadow: var(--shadow-lg);">
                </div>
                <div>
                    <span style="display: inline-block; padding: 0.5rem 1rem; background: var(--lighter-gray); color: var(--accent-color); border-radius: 6px; font-size: 0.85rem; font-weight: 600; margin-bottom: 1rem;">${this.product.category}</span>
                    <h1 style="font-size: 2.5rem; color: var(--primary-color); margin-bottom: 1rem;">${this.product.name}</h1>
                    <p style="font-size: 1.15rem; line-height: 1.8; color: var(--text-color); margin-bottom: 2rem;">${this.product.description}</p>
                    
                    <div style="background: var(--lighter-gray); padding: 1.5rem; border-radius: 12px; margin-bottom: 2rem;">
                        <h3 style="font-size: 1.1rem; color: var(--primary-color); margin-bottom: 1rem;">Applications</h3>
                        <div style="display: flex; flex-wrap: wrap; gap: 0.5rem;">
                            ${this.product.applications.map(app => 
                                `<span style="padding: 0.5rem 1rem; background: white; border-radius: 6px; font-size: 0.9rem;">${app}</span>`
                            ).join('')}
                        </div>
                    </div>

                    <div style="display: flex; gap: 1rem;">
                        <a href="${this.basePath}contact.html?product=${encodeURIComponent(this.product.name)}" class="btn btn-primary">Request Quote</a>
                        <a href="https://api.whatsapp.com/send/?phone=919773278770&text=Inquiry%20about%20${encodeURIComponent(this.product.name)}" target="_blank" class="btn btn-secondary">
                            <i class="fab fa-whatsapp"></i> WhatsApp Inquiry
                        </a>
                    </div>
                </div>
            </div>
        `;
    }

    /**
     * Generate header
     */
    generateHeader() {
        return `
            <div class="container">
                <div class="logo">
                    <a href="${this.basePath}index.html">
                        <img src="${this.basePath}assets/Supreme Valves.svg" alt="Supreme Valves India Logo">
                    </a>
                </div>
                <nav>
                    <ul>
                        <li><a href="${this.basePath}index.html">Home</a></li>
                        <li><a href="${this.basePath}about.html">About Us</a></li>
                        <li class="dropdown">
                            <a href="${this.basePath}products.html" class="dropbtn active">
                                Products <i class="fas fa-chevron-down"></i>
                            </a>
                            <div class="dropdown-content" id="products-dropdown"></div>
                        </li>
                        <li><a href="${this.basePath}industries.html">Industries</a></li>
                        <li><a href="${this.basePath}projects.html">Projects</a></li>
                        <li><a href="${this.basePath}resources.html">Resources</a></li>
                        <li><a href="${this.basePath}faqs.html">FAQs</a></li>
                        <li><a href="${this.basePath}contact.html">Contact Us</a></li>
                    </ul>
                </nav>
            </div>
        `;
    }

    /**
     * Generate footer
     */
    generateFooter() {
        return `
            <div class="container">
                <div class="footer-grid">
                    <div class="footer-col footer-products-col">
                        <h4>Product Range</h4>
                        <ul id="footer-products-list" class="footer-products-multicolumn"></ul>
                    </div>
                    <div class="footer-col">
                        <h4>Quick Links</h4>
                        <ul>
                            <li><a href="${this.basePath}index.html">Home</a></li>
                            <li><a href="${this.basePath}about.html">About Us</a></li>
                            <li><a href="${this.basePath}products.html">Products</a></li>
                            <li><a href="${this.basePath}industries.html">Industries</a></li>
                            <li><a href="${this.basePath}projects.html">Projects</a></li>
                            <li><a href="${this.basePath}resources.html">Resources</a></li>
                            <li><a href="${this.basePath}contact.html">Contact Us</a></li>
                            <li><a href="${this.basePath}ibr-certified-valve-manufacturer.html">IBR Certified Valves</a></li>
                            <li><a href="${this.basePath}valve-exporter-middle-east.html">Export to Middle East</a></li>
                        </ul>
                    </div>
                </div>
                
                <div class="footer-company-details">
                    <div class="company-info-grid">
                        <div class="company-info-item">
                            <i class="fas fa-map-marker-alt"></i>
                            <div>
                                <h5>India Office</h5>
                                <p>Ranginwala Building, Relief Road<br>Ahmedabad - 380001, Gujarat, India</p>
                            </div>
                        </div>
                        <div class="company-info-item">
                            <i class="fas fa-globe"></i>
                            <div>
                                <h5>International Offices</h5>
                                <p>Singapore: sg@supremevalves.in<br>
                                Sydney, Australia: aus@supremevalves.in<br>
                                Mississauga, Canada: ca@supremevalves.in</p>
                            </div>
                        </div>
                    </div>
                </div>
                
                <div class="footer-socials">
                    <a href="https://www.facebook.com/p/Supreme-Enterprise-61566023002189/" target="_blank" aria-label="Facebook"><i class="fab fa-facebook-f"></i></a>
                    <a href="https://www.instagram.com/supremevalvesindia/" target="_blank" aria-label="Instagram"><i class="fab fa-instagram"></i></a>
                    <a href="https://www.linkedin.com/company/supreme-valves-india/posts/?feedView=all" target="_blank" aria-label="LinkedIn"><i class="fab fa-linkedin-in"></i></a>
                    <a href="https://x.com/SupremeValves" target="_blank" aria-label="Twitter/X"><i class="fab fa-x-twitter"></i></a>
                    <a href="https://www.youtube.com/@SupremeValves" target="_blank" aria-label="YouTube"><i class="fab fa-youtube"></i></a>
                    <a href="#" target="_blank" aria-label="Pinterest"><i class="fab fa-pinterest-p"></i></a>
                </div>
                
                <div class="copyright">
                    &copy; ${new Date().getFullYear()} Supreme Valves India. All Rights Reserved.
                </div>
            </div>
        `;
    }

    /**
     * Generate WhatsApp widget
     */
    generateWhatsAppWidget() {
        const message = this.product 
            ? `Inquiry%20about%20${encodeURIComponent(this.product.name)}`
            : 'Inquiry';

        return `
            <a href="https://api.whatsapp.com/send/?phone=919773278770&text=${message}" target="_blank" aria-label="Chat with us on WhatsApp">
                <svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" fill="currentColor" viewBox="0 0 16 16">
                    <path d="M13.601 2.326A7.85 7.85 0 0 0 7.994 0C3.627 0 .068 3.558.064 7.926c0 1.399.366 2.76 1.057 3.965L0 16l4.204-1.102a7.9 7.9 0 0 0 3.79.965h.004c4.368 0 7.926-3.558 7.93-7.93A7.89 7.89 0 0 0 13.6 2.326zM7.994 14.521a6.57 6.57 0 0 1-3.356-.92l-.24-.144-2.494.654.666-2.433-.156-.251a6.56 6.56 0 0 1-1.007-3.505c0-3.626 2.957-6.584 6.591-6.584a6.56 6.56 0 0 1 4.66 1.931 6.56 6.56 0 0 1 1.928 4.66c-.004 3.639-2.961 6.592-6.592 6.592m3.615-4.934c-.197-.099-1.17-.578-1.353-.646-.182-.065-.315-.099-.445.099-.133.197-.513.646-.627.775-.114.133-.232.148-.43.05-.197-.1-.836-.308-1.592-.985-.59-.525-.985-1.175-1.103-1.372-.114-.198-.011-.304.088-.403.087-.088.197-.232.296-.346.1-.114.133-.198.198-.33.065-.134.034-.248-.015-.347-.05-.099-.445-1.076-.612-1.47-.16-.389-.323-.335-.445-.34-.114-.007-.247-.007-.38-.007a.73.73 0 0 0-.529.247c-.182.198-.691.677-.691 1.654s.71 1.916.81 2.049c.098.133 1.394 2.132 3.383 2.992.47.205.84.326 1.129.418.475.152.904.129 1.246.08.38-.058 1.171-.48 1.338-.943.164-.464.164-.86.114-.943-.049-.084-.182-.133-.38-.232"/>
                </svg>
            </a>
        `;
    }

    /**
     * Initialize auto-generation
     */
    async init() {
        await this.loadProduct();
        
        if (!this.product) {
            console.warn('Product not found, skipping auto-generation');
            return;
        }

        // Update meta tags
        this.updateMetaTags();

        // Generate header
        const headerEl = document.getElementById('header');
        if (headerEl) {
            headerEl.outerHTML = `<header>${this.generateHeader()}</header>`;
        }

        // Generate product header
        const productHeaderEl = document.getElementById('product-header');
        if (productHeaderEl) {
            productHeaderEl.innerHTML = this.generateProductHeader();
        }

        // Generate footer
        const footerEl = document.getElementById('footer');
        if (footerEl) {
            footerEl.outerHTML = `<footer class="footer-new">${this.generateFooter()}</footer>`;
        }

        // Generate WhatsApp widget
        const whatsappEl = document.getElementById('whatsapp-widget');
        if (whatsappEl) {
            whatsappEl.className = 'whatsapp-widget';
            whatsappEl.innerHTML = this.generateWhatsAppWidget();
        }

        // Trigger productRenderer to populate dropdowns and footer
        if (window.productRenderer) {
            window.productRenderer.renderProductsDropdown();
            window.productRenderer.renderFooterProducts();
        }
    }
}

// Create global instance
window.productPageAuto = new ProductPageAuto();

// Auto-initialize after productRenderer is ready
document.addEventListener('DOMContentLoaded', async () => {
    // Wait a bit for productRenderer to initialize
    setTimeout(() => {
        window.productPageAuto.init();
    }, 100);
});
