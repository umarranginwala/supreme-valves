
import os
import re
from pathlib import Path

def standardize_layout():
    root_dir = Path('/Users/umarranginwala/Downloads/supremevalves_site_v3')
    
    # Standard Head Template (tags common to all pages)
    head_tags_template = """    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="{prefix}styles.css">
    <link rel="stylesheet" href="{prefix}css/product-search.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css">"""

    # Standard Header Template
    header_template = """    <header>
        <div class="container">
            <div class="logo">
                <a href="{prefix}index.html"><img src="{prefix}assets/Supreme Valves.svg" alt="Supreme Valves India Logo"></a>
            </div>
            <nav>
                <ul>
                    <li><a href="{prefix}index.html">Home</a></li>
                    <li><a href="{prefix}about.html">About Us</a></li>
                    <li class="dropdown">
                        <a href="{prefix}products.html" class="dropbtn">Products <i class="fas fa-chevron-down"></i></a>
                        <div class="dropdown-content" id="products-dropdown">
                            <!-- Products will be dynamically loaded here -->
                        </div>
                    </li>
                    <li><a href="{prefix}industries.html">Industries</a></li>
                    <li><a href="{prefix}projects.html">Projects</a></li>
                    <li><a href="{prefix}resources.html">Resources</a></li>
                    <li><a href="{prefix}faqs.html">FAQs</a></li>
                    <li><a href="{prefix}blog.html">Blog</a></li>
                    <li><a href="{prefix}contact.html">Contact Us</a></li>
                </ul>
            </nav>
        </div>
    </header>"""

    # Standard Footer Template
    footer_template = """    <footer class="footer-new">
        <div class="container">
            <div class="footer-grid">
                <div class="footer-col footer-products-col">
                    <h4>Product Range</h4>
                    <ul id="footer-products-list" class="footer-products-multicolumn">
                        <!-- Products will be dynamically loaded here -->
                    </ul>
                </div>
                <div class="footer-col">
                    <h4>Quick Links</h4>
                    <ul>
                        <li><a href="{prefix}index.html">Home</a></li>
                        <li><a href="{prefix}about.html">About Us</a></li>
                        <li><a href="{prefix}products.html">Products</a></li>
                        <li><a href="{prefix}industries.html">Industries</a></li>
                        <li><a href="{prefix}projects.html">Projects</a></li>
                        <li><a href="{prefix}resources.html">Resources</a></li>
                        <li><a href="{prefix}faqs.html">FAQs</a></li>
                        <li><a href="{prefix}blog.html">Blog</a></li>
                        <li><a href="{prefix}contact.html">Contact Us</a></li>
                    </ul>
                </div>
                <div class="footer-col">
                    <h4>Resources & Info</h4>
                    <ul>
                        <li><a href="{prefix}ibr-certified-valve-exporter.html">IBR Certified Valves</a></li>
                        <li><a href="{prefix}globe-valve-exporters-india.html">Globe Valve Exporters</a></li>
                        <li><a href="{prefix}valve-exporter-middle-east.html">Valve Exporter Middle East</a></li>
                        <li><a href="{prefix}faqs/valve-types-selection.html">Valve Types & Selection</a></li>
                        <li><a href="{prefix}faqs/valve-materials.html">Valve Materials</a></li>
                        <li><a href="{prefix}faqs/valve-standards.html">Valve Standards</a></li>
                        <li><a href="{prefix}faqs/valve-maintenance.html">Valve Maintenance</a></li>
                        <li><a href="{prefix}docs/technical-resources/technical-resources.html">Technical Resources</a></li>
                    </ul>
                </div>
            </div>
            <div class="footer-bottom">
                <div class="footer-company-details">
                    <p>&copy; 2025 Supreme Valves India. All Rights Reserved. | Managed by <a href="https://www.social-sense.in" target="_blank" style="color: var(--accent-color);">Social Sense</a></p>
                </div>
            </div>
        </div>
    </footer>"""

    # Directories to process
    dirs_to_process = ['', 'products', 'blog', 'faqs', 'countries', 'docs/technical-resources', 'projects']

    for dir_name in dirs_to_process:
        dir_path = root_dir / dir_name
        if not dir_path.exists():
            continue
            
        depth = len(dir_name.split('/')) if dir_name else 0
        prefix = '../' * depth if depth > 0 else ''
        
        for html_file in dir_path.glob('*.html'):
            with open(html_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original_content = content
            
            # Unify head tags (styles and fonts)
            # Find the head section
            head_match = re.search(r'<head>(.*?)</head>', content, re.DOTALL)
            if head_match:
                head_content = head_match.group(1)
                # Remove common head tags that we are replacing
                head_content = re.sub(r'<link rel="preconnect"[^>]*>', '', head_content)
                head_content = re.sub(r'<link href="https://fonts.googleapis.com[^>]*" rel="stylesheet">', '', head_content)
                head_content = re.sub(r'<link rel="stylesheet" href="[^"]*styles.css"[^>]*>', '', head_content)
                head_content = re.sub(r'<link rel="stylesheet" href="[^"]*product-search.css"[^>]*>', '', head_content)
                head_content = re.sub(r'<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/[^>]*>', '', head_content)
                
                # Reconstruct head
                new_head_content = head_content.strip() + "\n" + head_tags_template.format(prefix=prefix)
                content = content.replace(head_match.group(1), new_head_content)

            # Replace Header
            content = re.sub(r'<header>.*?</header>', header_template.format(prefix=prefix), content, flags=re.DOTALL)
            
            # Replace Footer
            content = re.sub(r'<footer.*?>.*?</footer>', footer_template.format(prefix=prefix), content, flags=re.DOTALL)
            
            # Remove Font Awesome Kit Script (conflicts with CDN)
            content = re.sub(r'<script src="https://kit.fontawesome.com/[^"]+js"[^>]*></script>', '', content)
            
            # 1. Fix white-on-white or low contrast buttons in known dark sections
            # Find sections with background gradients (typical for hero/CTA)
            dark_sections = re.findall(r'(<section[^>]*style="[^"]*background:\s*linear-gradient[^"]*"[^>]*>.*?</section>)', content, re.DOTALL)
            for section in dark_sections:
                # In these sections, btn-secondary should be btn-outline-light
                fixed_section = section.replace('btn-secondary', 'btn-outline-light')
                content = content.replace(section, fixed_section)

            # 2. General cleanup of inline styles on buttons that might conflict with new CSS
            content = re.sub(r'(class="btn[^"]*")\s+style="[^"]*background:[^"]*;?\s*color:[^"]*;?[^"]*"', r'\1', content)
            
            if content != original_content:
                with open(html_file, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"Standardized layout for {html_file.relative_to(root_dir)}")

if __name__ == "__main__":
    standardize_layout()
