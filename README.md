# Supreme Valves India - Website

## 🏗️ Modular Architecture

This website is built with a highly modular architecture for easy maintenance and scalability.

### Core Components

#### 1. Data-Driven System
- **`data/products.json`** - Single source of truth for all products
- **`data/projects.json`** - Project case studies data
- **`data/countries.json`** - Country-specific landing pages data

#### 2. Generator Scripts (Python)
- **`auto_generate_product_pages.py`** - Generates all product pages from products.json
- **`generate_country_pages.py`** - Generates country-specific landing pages
- **`generate_project_pages.py`** - Generates project case study pages
- **`generate_blog_posts.py`** - Generates blog posts

#### 3. JavaScript Modules
- **`js/products.js`** - Product rendering and dynamic content
- **`js/product-renderer.js`** - Modular product display system

#### 4. Templates
- **`product-template.html`** - Template for product pages
- **`footer-template.html`** - Reusable footer component

### 📝 Adding New Content

#### Add a New Product
1. Add product entry to `data/products.json`
2. Run: `python3 auto_generate_product_pages.py`
3. Product appears everywhere automatically (dropdown, footer, products page, related products)

#### Add a New Country Page
1. Add country entry to `data/countries.json`
2. Run: `python3 generate_country_pages.py`
3. Update footer links if needed

#### Add a New Project
1. Add project entry to `data/projects.json`
2. Run: `python3 generate_project_pages.py`

### 🎨 Styling
- **`styles.css`** - Main stylesheet with CSS variables for easy theming

### 📊 SEO & Analytics
- **`sitemap.xml`** - Auto-updated sitemap
- **`robots.txt`** - Search engine directives
- Schema.org markup on all pages

### 🚀 Deployment
- Push to GitHub
- Auto-deploys via GitHub Pages or your hosting provider

### 📁 Directory Structure
```
supremevalves_site_v3/
├── data/                    # JSON data files
├── js/                      # JavaScript modules
├── products/                # Generated product pages (106 pages)
├── countries/               # Generated country pages (18 pages)
├── projects/                # Generated project pages
├── blog/                    # Blog posts
├── faqs/                    # FAQ pages
├── docs/                    # Technical resources
├── assets/                  # Images and media
├── *.py                     # Generator scripts
└── *.html                   # Main pages
```

### 🔧 Maintenance
- All product updates: Edit `data/products.json` only
- All styling: Edit `styles.css` only
- Footer changes: Edit `footer-template.html` and regenerate pages

### 📞 Contact
Supreme Valves India
- Website: https://www.supremevalves.in
- Email: info@supremevalves.in
