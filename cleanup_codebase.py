#!/usr/bin/env python3
"""
Comprehensive Code Cleanup Script
Removes unnecessary files, consolidates code, and improves modularity
"""

import os
import shutil
from pathlib import Path

# Files and directories to remove
CLEANUP_ITEMS = {
    'python_scripts': [
        # One-time migration scripts (no longer needed)
        'add_all_technical_specs.py',
        'add_missing_schema.py',
        'add_technical_specs.py',
        'fix_cta_buttons.py',
        'fix_old_footers.py',
        'fix_product_footers.py',
        'fix_product_schema.py',
        'update_all_footers.py',
        'update_headers_footers.py',
        'update_ic_ball_valve_specs.py',
        'update_product_images.py',
        'update_schema_prices.py',
        'replace_manufacturer_with_exporter.py',
        'generate_ic_ball_valve_pages.py',
    ],
    'old_directories': [
        'site_updates',
        'site_updates 2',
        'site_updates_products_from_catalogue',
    ],
    'old_html_files': [
        'projects-old.html',
    ],
    'documentation_to_consolidate': [
        # Keep only essential docs, remove redundant ones
        'BLOG_DISCOVERY_STRATEGY.md',
        'CONSISTENCY_UPDATE_SUMMARY.md',
        'FAQ_DEPLOYMENT_SUMMARY.md',
        'GLOBE_VALVE_SEO_STRATEGY.md',
        'MODULAR_SYSTEM_SUMMARY.md',
        'NAVIGATION_GUIDE.md',
        'PRODUCTS_README.md',
        'PRODUCT_PAGE_GUIDE.md',
        'QUICK_ADD_PRODUCT.md',
        'README_SEO.md',
        'SEO_COMPETITOR_KEYWORD_ANALYSIS.md',
        'SEO_IMPLEMENTATION_SUMMARY.md',
    ],
}

# Keep these essential scripts
KEEP_SCRIPTS = [
    'auto_generate_product_pages.py',  # Core functionality
    'generate_blog_posts.py',           # Core functionality
    'generate_country_pages.py',        # Core functionality
    'generate_project_pages.py',        # Core functionality
    'cleanup_codebase.py',              # This script
]

def remove_file(file_path):
    """Safely remove a file"""
    try:
        if os.path.exists(file_path):
            os.remove(file_path)
            print(f"✅ Removed file: {file_path}")
            return True
    except Exception as e:
        print(f"❌ Error removing {file_path}: {e}")
    return False

def remove_directory(dir_path):
    """Safely remove a directory"""
    try:
        if os.path.exists(dir_path):
            shutil.rmtree(dir_path)
            print(f"✅ Removed directory: {dir_path}")
            return True
    except Exception as e:
        print(f"❌ Error removing {dir_path}: {e}")
    return False

def main():
    print("🧹 Starting Code Cleanup...\n")
    
    removed_count = 0
    
    # Remove old Python scripts
    print("📝 Removing one-time migration scripts...")
    for script in CLEANUP_ITEMS['python_scripts']:
        if remove_file(script):
            removed_count += 1
    
    # Remove old directories
    print("\n📁 Removing old/backup directories...")
    for directory in CLEANUP_ITEMS['old_directories']:
        if remove_directory(directory):
            removed_count += 1
    
    # Remove old HTML files
    print("\n🌐 Removing old HTML files...")
    for html_file in CLEANUP_ITEMS['old_html_files']:
        if remove_file(html_file):
            removed_count += 1
    
    # Remove redundant documentation
    print("\n📚 Removing redundant documentation...")
    for doc_file in CLEANUP_ITEMS['documentation_to_consolidate']:
        if remove_file(doc_file):
            removed_count += 1
    
    # Create consolidated README
    print("\n📖 Creating consolidated README...")
    create_consolidated_readme()
    
    print(f"\n🎉 Cleanup Complete!")
    print(f"   Total items removed: {removed_count}")
    print(f"\n✅ Kept essential scripts:")
    for script in KEEP_SCRIPTS:
        if os.path.exists(script):
            print(f"   - {script}")

def create_consolidated_readme():
    """Create a single comprehensive README"""
    readme_content = """# Supreme Valves India - Website

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
"""
    
    with open('README.md', 'w', encoding='utf-8') as f:
        f.write(readme_content)
    print("✅ Created consolidated README.md")

if __name__ == '__main__':
    main()
