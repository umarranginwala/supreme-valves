#!/usr/bin/env python3
"""
Fix footer structure on all product pages to match homepage
"""

import os
import re

# Product directory
products_dir = 'products'

# Correct footer structure (matching homepage)
correct_footer = '''    <footer class="footer-new">
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
                        <li><a href="../index.html">Home</a></li>
                        <li><a href="../about.html">About Us</a></li>
                        <li><a href="../products.html">Products</a></li>
                        <li><a href="../industries.html">Industries</a></li>
                        <li><a href="../projects.html">Projects</a></li>
                        <li><a href="../resources.html">Resources</a></li>
                        <li><a href="../contact.html">Contact Us</a></li>
                        <li><a href="../ibr-certified-valve-manufacturer.html">IBR Certified Valves</a></li>
                        <li><a href="../valve-exporter-middle-east.html">Export to Middle East</a></li>
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
                &copy; 2025 Supreme Valves India. All Rights Reserved.
            </div>
        </div>
    </footer>'''

updated_count = 0

# Get all HTML files in products directory
for filename in os.listdir(products_dir):
    if not filename.endswith('.html'):
        continue
    
    filepath = os.path.join(products_dir, filename)
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find and replace footer section
        # Pattern to match from <footer to </footer>
        footer_pattern = r'<footer class="footer-new">.*?</footer>'
        
        if re.search(footer_pattern, content, re.DOTALL):
            # Replace footer
            new_content = re.sub(footer_pattern, correct_footer, content, flags=re.DOTALL)
            
            # Write back
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            
            print(f"✅ Updated: {filename}")
            updated_count += 1
        else:
            print(f"⚠️  No footer found: {filename}")
    
    except Exception as e:
        print(f"❌ Error updating {filename}: {e}")

print(f"\n🎉 Updated {updated_count} product pages successfully!")
