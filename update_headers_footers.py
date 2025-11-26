#!/usr/bin/env python3
"""
Script to update headers and footers across all HTML pages to match homepage structure
"""

import os
import re
from pathlib import Path

# Standard header HTML from homepage
STANDARD_HEADER = '''    <header>
        <div class="container">
            <div class="logo">
                <a href="{home_path}index.html"><img src="{assets_path}assets/Supreme Valves.svg" alt="Supreme Valves India Logo"></a>
            </div>
            <nav>
                <ul>
                    <li><a href="{home_path}index.html"{home_active}>Home</a></li>
                    <li><a href="{home_path}about.html"{about_active}>About Us</a></li>
                    <li class="dropdown">
                        <a href="{home_path}products.html" class="dropbtn"{products_active}>Products <i class="fas fa-chevron-down"></i></a>
                        <div class="dropdown-content" id="products-dropdown">
                            <!-- Products will be dynamically loaded here -->
                        </div>
                    </li>
                    <li><a href="{home_path}industries.html"{industries_active}>Industries</a></li>
                    <li><a href="{home_path}projects.html"{projects_active}>Projects</a></li>
                    <li><a href="{home_path}resources.html"{resources_active}>Resources</a></li>
                    <li><a href="{home_path}faqs.html"{faqs_active}>FAQs</a></li>
                    <li><a href="{home_path}contact.html"{contact_active}>Contact Us</a></li>
                </ul>
            </nav>
        </div>
    </header>'''

# Standard footer Quick Links section
FOOTER_QUICK_LINKS = '''                    <h4>Quick Links</h4>
                    <ul>
                        <li><a href="{home_path}index.html">Home</a></li>
                        <li><a href="{home_path}about.html">About Us</a></li>
                        <li><a href="{home_path}products.html">Products</a></li>
                        <li><a href="{home_path}industries.html">Industries</a></li>
                        <li><a href="{home_path}projects.html">Projects</a></li>
                        <li><a href="{home_path}resources.html">Resources</a></li>
                        <li><a href="{home_path}contact.html">Contact Us</a></li>
                        <li><a href="{home_path}ibr-certified-valve-manufacturer.html">IBR Certified Valves</a></li>
                        <li><a href="{home_path}valve-exporter-middle-east.html">Export to Middle East</a></li>
                    </ul>'''

# Standard footer socials
FOOTER_SOCIALS = '''            <div class="footer-socials">
                <a href="https://www.facebook.com/p/Supreme-Enterprise-61566023002189/" target="_blank" aria-label="Facebook"><i class="fab fa-facebook-f"></i></a>
                <a href="https://www.instagram.com/supremevalvesindia/" target="_blank" aria-label="Instagram"><i class="fab fa-instagram"></i></a>
                <a href="https://www.linkedin.com/company/supreme-valves-india/posts/?feedView=all" target="_blank" aria-label="LinkedIn"><i class="fab fa-linkedin-in"></i></a>
                <a href="https://x.com/SupremeValves" target="_blank" aria-label="Twitter/X"><i class="fab fa-x-twitter"></i></a>
                <a href="https://www.youtube.com/@SupremeValves" target="_blank" aria-label="YouTube"><i class="fab fa-youtube"></i></a>
                <a href="#" target="_blank" aria-label="Pinterest"><i class="fab fa-pinterest-p"></i></a>
            </div>'''

def get_active_class(filename, page_type):
    """Determine which nav item should have active class"""
    active_map = {
        'index.html': 'home',
        'about.html': 'about',
        'products.html': 'products',
        'industries.html': 'industries',
        'projects.html': 'projects',
        'resources.html': 'resources',
        'faqs.html': 'faqs',
        'contact.html': 'contact'
    }
    
    # Check if it's a product page
    if '/products/' in filename or filename.startswith('products/'):
        return 'products'
    
    # Check if it's an FAQ page
    if '/faqs/' in filename or filename.startswith('faqs/'):
        return 'faqs'
    
    # Get base filename
    base_name = os.path.basename(filename)
    return active_map.get(base_name, '')

def get_path_prefix(filepath):
    """Get the relative path prefix based on file location"""
    if '/products/' in filepath:
        return '../'
    elif '/faqs/' in filepath:
        return '../'
    elif '/docs/' in filepath:
        return '../../'
    else:
        return ''

def update_header(content, filepath):
    """Update header to match homepage structure"""
    home_path = get_path_prefix(filepath)
    assets_path = home_path
    
    active_page = get_active_class(filepath, '')
    
    # Build active class strings
    active_classes = {
        'home': ' class="active"' if active_page == 'home' else '',
        'about': ' class="active"' if active_page == 'about' else '',
        'products': ' class="active"' if active_page == 'products' else '',
        'industries': ' class="active"' if active_page == 'industries' else '',
        'projects': ' class="active"' if active_page == 'projects' else '',
        'resources': ' class="active"' if active_page == 'resources' else '',
        'faqs': ' class="active"' if active_page == 'faqs' else '',
        'contact': ' class="active"' if active_page == 'contact' else ''
    }
    
    new_header = STANDARD_HEADER.format(
        home_path=home_path,
        assets_path=assets_path,
        home_active=active_classes['home'],
        about_active=active_classes['about'],
        products_active=active_classes['products'],
        industries_active=active_classes['industries'],
        projects_active=active_classes['projects'],
        resources_active=active_classes['resources'],
        faqs_active=active_classes['faqs'],
        contact_active=active_classes['contact']
    )
    
    # Replace header section
    header_pattern = r'<header>.*?</header>'
    content = re.sub(header_pattern, new_header, content, flags=re.DOTALL)
    
    return content

def update_footer_quick_links(content, filepath):
    """Update footer quick links section"""
    home_path = get_path_prefix(filepath)
    
    new_quick_links = FOOTER_QUICK_LINKS.format(home_path=home_path)
    
    # Pattern to match Quick Links section
    pattern = r'<h4>Quick Links</h4>\s*<ul>.*?</ul>'
    content = re.sub(pattern, new_quick_links, content, flags=re.DOTALL)
    
    return content

def update_footer_socials(content):
    """Update footer socials section"""
    # Pattern to match footer socials
    pattern = r'<div class="footer-socials">.*?</div>'
    content = re.sub(pattern, FOOTER_SOCIALS, content, flags=re.DOTALL)
    
    return content

def process_html_file(filepath):
    """Process a single HTML file"""
    print(f"Processing: {filepath}")
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Skip if it's a template file
        if 'template' in filepath.lower():
            print(f"  Skipping template file")
            return
        
        original_content = content
        
        # Update header
        content = update_header(content, filepath)
        
        # Update footer quick links
        content = update_footer_quick_links(content, filepath)
        
        # Update footer socials
        content = update_footer_socials(content)
        
        # Only write if content changed
        if content != original_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"  ✓ Updated")
        else:
            print(f"  - No changes needed")
            
    except Exception as e:
        print(f"  ✗ Error: {e}")

def main():
    """Main function to process all HTML files"""
    base_dir = Path('/Users/umarranginwala/Downloads/supremevalves_site_v3')
    
    # Find all HTML files
    html_files = []
    html_files.extend(base_dir.glob('*.html'))
    html_files.extend(base_dir.glob('products/*.html'))
    html_files.extend(base_dir.glob('faqs/*.html'))
    html_files.extend(base_dir.glob('docs/**/*.html'))
    
    print(f"Found {len(html_files)} HTML files to process\n")
    
    for html_file in sorted(html_files):
        process_html_file(str(html_file))
    
    print(f"\n✓ Completed processing {len(html_files)} files")

if __name__ == '__main__':
    main()
