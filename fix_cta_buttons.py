#!/usr/bin/env python3
"""
Fix CTA button styling across all HTML files
Remove inline styles that cause white-on-white text issues
"""

import os
import re
from pathlib import Path

# Find all HTML files
html_files = []

# Root directory HTML files
for file in Path('.').glob('*.html'):
    if file.name not in ['footer-template.html', 'product-template.html', 'projects-old.html']:
        html_files.append(str(file))

# Subdirectories
for subdir in ['products', 'countries', 'faqs', 'projects', 'blog', 'docs/technical-resources']:
    if Path(subdir).exists():
        for file in Path(subdir).glob('*.html'):
            html_files.append(str(file))

print(f"Found {len(html_files)} HTML files to check")

# Patterns to fix
patterns_to_fix = [
    # Pattern 1: btn btn-primary with white background inline style
    {
        'pattern': r'class="btn btn-primary"\s+style="background:\s*white;\s*color:\s*var\(--primary-color\);[^"]*"',
        'replacement': 'class="btn btn-primary"',
        'description': 'btn-primary with white background'
    },
    # Pattern 2: btn with white background inline style (no btn-primary)
    {
        'pattern': r'class="btn"\s+style="background:\s*white;\s*color:\s*var\(--primary-color\);?"',
        'replacement': 'class="btn btn-primary"',
        'description': 'btn with white background'
    },
    # Pattern 3: Reverse order - style before class
    {
        'pattern': r'style="background:\s*white;\s*color:\s*var\(--primary-color\);[^"]*"\s+class="btn btn-primary"',
        'replacement': 'class="btn btn-primary"',
        'description': 'btn-primary with white background (reverse order)'
    },
]

# Update each file
updated_count = 0
total_fixes = 0

for html_file in html_files:
    try:
        with open(html_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        file_fixes = 0
        
        # Apply all patterns
        for pattern_info in patterns_to_fix:
            matches = re.findall(pattern_info['pattern'], content, re.IGNORECASE)
            if matches:
                content = re.sub(pattern_info['pattern'], pattern_info['replacement'], content, flags=re.IGNORECASE)
                file_fixes += len(matches)
        
        # If content changed, write it back
        if content != original_content:
            with open(html_file, 'w', encoding='utf-8') as f:
                f.write(content)
            
            print(f"✅ Fixed {file_fixes} button(s) in: {html_file}")
            updated_count += 1
            total_fixes += file_fixes
    
    except Exception as e:
        print(f"❌ Error processing {html_file}: {e}")

print(f"\n🎉 Summary:")
print(f"   Files updated: {updated_count}")
print(f"   Total buttons fixed: {total_fixes}")
