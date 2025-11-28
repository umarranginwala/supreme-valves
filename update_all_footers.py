#!/usr/bin/env python3
"""
Update all HTML files with the new footer template
"""

import os
import re
from pathlib import Path

# Read the new footer template
with open('footer-template.html', 'r', encoding='utf-8') as f:
    new_footer = f.read()

# Find all HTML files
html_files = []

# Root directory HTML files
for file in Path('.').glob('*.html'):
    if file.name not in ['footer-template.html', 'product-template.html', 'projects-old.html']:
        html_files.append(str(file))

# Products directory
for file in Path('products').glob('*.html'):
    html_files.append(str(file))

# Countries directory
for file in Path('countries').glob('*.html'):
    html_files.append(str(file))

# FAQs directory
for file in Path('faqs').glob('*.html'):
    html_files.append(str(file))

# Projects directory
if Path('projects').exists():
    for file in Path('projects').glob('*.html'):
        html_files.append(str(file))

# Blog directory
if Path('blog').exists():
    for file in Path('blog').glob('*.html'):
        html_files.append(str(file))

# Docs/technical-resources directory
if Path('docs/technical-resources').exists():
    for file in Path('docs/technical-resources').glob('*.html'):
        html_files.append(str(file))

print(f"Found {len(html_files)} HTML files to update")

# Update each file
updated_count = 0
for html_file in html_files:
    try:
        with open(html_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if file has a footer
        if '<footer' not in content:
            print(f"⏭️  Skipped (no footer): {html_file}")
            continue
        
        # Replace the footer section
        # Pattern to match from <footer to </footer>
        footer_pattern = r'<footer class="footer-new">.*?</footer>'
        
        if re.search(footer_pattern, content, re.DOTALL):
            new_content = re.sub(footer_pattern, new_footer.strip(), content, flags=re.DOTALL)
            
            with open(html_file, 'w', encoding='utf-8') as f:
                f.write(new_content)
            
            print(f"✅ Updated: {html_file}")
            updated_count += 1
        else:
            print(f"⚠️  Footer pattern not found: {html_file}")
    
    except Exception as e:
        print(f"❌ Error updating {html_file}: {e}")

print(f"\n🎉 Updated {updated_count} files!")
