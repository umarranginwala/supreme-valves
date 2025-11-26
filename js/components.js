/**
 * Supreme Valves - Modular Component System
 * Reusable components for consistent UI across all pages
 */

class ComponentLoader {
    constructor() {
        this.components = new Map();
        this.config = null;
    }

    /**
     * Load site configuration
     */
    async loadConfig() {
        if (this.config) return this.config;
        
        try {
            const path = this.getBasePath();
            const response = await fetch(`${path}data/config.json`);
            this.config = await response.json();
            return this.config;
        } catch (error) {
            console.error('Error loading config:', error);
            return null;
        }
    }

    /**
     * Get base path based on current location
     */
    getBasePath() {
        const path = window.location.pathname;
        if (path.includes('/products/') || path.includes('/faqs/')) {
            return '../';
        } else if (path.includes('/docs/')) {
            return '../../';
        }
        return '';
    }

    /**
     * Render header component
     */
    async renderHeader(activePage = '') {
        const config = await this.loadConfig();
        if (!config) return;

        const basePath = this.getBasePath();
        const header = document.querySelector('header');
        if (!header) return;

        const navItems = config.navigation.map(item => {
            const isActive = activePage === item.id ? 'class="active"' : '';
            const href = `${basePath}${item.href}`;
            
            if (item.dropdown) {
                return `
                    <li class="dropdown">
                        <a href="${href}" class="dropbtn" ${isActive}>
                            ${item.label} <i class="fas fa-chevron-down"></i>
                        </a>
                        <div class="dropdown-content" id="products-dropdown"></div>
                    </li>
                `;
            }
            
            return `<li><a href="${href}" ${isActive}>${item.label}</a></li>`;
        }).join('');

        header.innerHTML = `
            <div class="container">
                <div class="logo">
                    <a href="${basePath}index.html">
                        <img src="${basePath}assets/Supreme Valves.svg" alt="Supreme Valves India Logo">
                    </a>
                </div>
                <nav>
                    <ul>${navItems}</ul>
                </nav>
            </div>
        `;
    }

    /**
     * Render footer component
     */
    async renderFooter() {
        const config = await this.loadConfig();
        if (!config) return;

        const basePath = this.getBasePath();
        const footer = document.querySelector('footer');
        if (!footer) return;

        const quickLinks = config.quickLinks.map(link => 
            `<li><a href="${basePath}${link.href}">${link.label}</a></li>`
        ).join('');

        const socialLinks = config.socialMedia.map(social => 
            `<a href="${social.url}" target="_blank" aria-label="${social.name}">
                <i class="${social.icon}"></i>
            </a>`
        ).join('');

        footer.innerHTML = `
            <div class="container">
                <div class="footer-grid">
                    <div class="footer-col footer-products-col">
                        <h4>Product Range</h4>
                        <ul id="footer-products-list" class="footer-products-multicolumn"></ul>
                    </div>
                    <div class="footer-col">
                        <h4>Quick Links</h4>
                        <ul>${quickLinks}</ul>
                    </div>
                </div>
                
                <div class="footer-company-details">
                    <div class="company-info-grid">
                        <div class="company-info-item">
                            <i class="fas fa-map-marker-alt"></i>
                            <div>
                                <h5>India Office</h5>
                                <p>${config.company.address.india}</p>
                            </div>
                        </div>
                        <div class="company-info-item">
                            <i class="fas fa-globe"></i>
                            <div>
                                <h5>International Offices</h5>
                                <p>${config.company.address.international}</p>
                            </div>
                        </div>
                    </div>
                </div>
                
                <div class="footer-socials">${socialLinks}</div>
                
                <div class="copyright">
                    &copy; ${new Date().getFullYear()} ${config.company.name}. All Rights Reserved.
                </div>
            </div>
        `;
    }

    /**
     * Render WhatsApp widget
     */
    async renderWhatsAppWidget(productName = '') {
        const config = await this.loadConfig();
        if (!config) return;

        const message = productName 
            ? `Inquiry%20about%20${encodeURIComponent(productName)}`
            : 'Inquiry';

        const widget = document.createElement('div');
        widget.className = 'whatsapp-widget';
        widget.innerHTML = `
            <a href="https://api.whatsapp.com/send/?phone=${config.company.whatsapp}&text=${message}" 
               target="_blank" 
               aria-label="Chat with us on WhatsApp">
                <svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" fill="currentColor" viewBox="0 0 16 16">
                    <path d="M13.601 2.326A7.85 7.85 0 0 0 7.994 0C3.627 0 .068 3.558.064 7.926c0 1.399.366 2.76 1.057 3.965L0 16l4.204-1.102a7.9 7.9 0 0 0 3.79.965h.004c4.368 0 7.926-3.558 7.93-7.93A7.89 7.89 0 0 0 13.6 2.326zM7.994 14.521a6.57 6.57 0 0 1-3.356-.92l-.24-.144-2.494.654.666-2.433-.156-.251a6.56 6.56 0 0 1-1.007-3.505c0-3.626 2.957-6.584 6.591-6.584a6.56 6.56 0 0 1 4.66 1.931 6.56 6.56 0 0 1 1.928 4.66c-.004 3.639-2.961 6.592-6.592 6.592m3.615-4.934c-.197-.099-1.17-.578-1.353-.646-.182-.065-.315-.099-.445.099-.133.197-.513.646-.627.775-.114.133-.232.148-.43.05-.197-.1-.836-.308-1.592-.985-.59-.525-.985-1.175-1.103-1.372-.114-.198-.011-.304.088-.403.087-.088.197-.232.296-.346.1-.114.133-.198.198-.33.065-.134.034-.248-.015-.347-.05-.099-.445-1.076-.612-1.47-.16-.389-.323-.335-.445-.34-.114-.007-.247-.007-.38-.007a.73.73 0 0 0-.529.247c-.182.198-.691.677-.691 1.654s.71 1.916.81 2.049c.098.133 1.394 2.132 3.383 2.992.47.205.84.326 1.129.418.475.152.904.129 1.246.08.38-.058 1.171-.48 1.338-.943.164-.464.164-.86.114-.943-.049-.084-.182-.133-.38-.232"/>
                </svg>
            </a>
        `;

        // Insert before footer
        const footer = document.querySelector('footer');
        if (footer) {
            footer.parentNode.insertBefore(widget, footer);
        }
    }

    /**
     * Initialize all components
     */
    async init(options = {}) {
        await this.loadConfig();
        await this.renderHeader(options.activePage);
        await this.renderFooter();
        await this.renderWhatsAppWidget(options.productName);
    }
}

// Create global instance
window.componentLoader = new ComponentLoader();

// Auto-initialize on page load
document.addEventListener('DOMContentLoaded', () => {
    const activePage = document.body.dataset.page || '';
    const productName = document.body.dataset.product || '';
    
    window.componentLoader.init({ activePage, productName });
});
