
import os
import re
from pathlib import Path

def fix_paths():
    root_dir = Path('/Users/umarranginwala/Downloads/supremevalves_site_v3')
    
    # Subdirectories to process
    subdirs = ['products', 'blog', 'faqs', 'countries', 'docs/technical-resources', 'projects']
    
    # Root level files that need ../ prefix in subdirs
    root_files = [
        'index.html', 'about.html', 'products.html', 'industries.html', 
        'projects.html', 'resources.html', 'faqs.html', 'blog.html', 
        'contact.html', 'styles.css', 'js/products.js', 'assets/Supreme Valves.svg',
        'ibr-certified-valve-exporter.html', 'globe-valve-exporters-india.html',
        'valve-exporter-middle-east.html', 'return-policy.html', 'thank-you.html',
        'ibr-certified-valve-manufacturer.html', 'js/form-handler.js'
    ]
    
    # Files that were renamed
    renames = {
        'globe-valve-manufacturers-india.html': 'globe-valve-exporters-india.html'
    }

    for subdir_name in subdirs:
        subdir_path = root_dir / subdir_name
        if not subdir_path.exists():
            continue
            
        depth = len(subdir_name.split('/'))
        prefix = '../' * depth
        
        for html_file in subdir_path.glob('*.html'): # Only direct html files in these subdirs
            with open(html_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original_content = content
            
            # 1. Fix renamed files
            for old, new in renames.items():
                content = content.replace(f'"{old}"', f'"{new}"')
                content = content.replace(f'"{prefix}{old}"', f'"{prefix}{new}"')
            
            # 2. Fix root-level links that are missing prefix
            for root_file in root_files:
                # This pattern matches root files that DON'T have a prefix or a protocol
                # e.g. href="index.html" -> href="../index.html"
                # but NOT href="../index.html" or href="https://..."
                pattern = rf'(href|src)="({re.escape(root_file)})"'
                replacement = rf'\1="{prefix}\2"'
                content = re.sub(pattern, replacement, content)
                
            # 3. Fix common folder links that are missing prefix
            # e.g. href="countries/uae.html" -> href="../countries/uae.html"
            common_folders = ['faqs/', 'blog/', 'countries/', 'docs/', 'products/', 'projects/', 'assets/']
            for folder in common_folders:
                # Match folder start but not if it already has ../ or is a full URL
                pattern = rf'(href|src)="({re.escape(folder)}[^"]*)"'
                # Check if it already has prefix
                def add_prefix(match):
                    attr = match.group(1)
                    path = match.group(2)
                    if path.startswith('../') or path.startswith('/') or '://' in path:
                        return f'{attr}="{path}"'
                    return f'{attr}="{prefix}{path}"'
                
                content = re.sub(pattern, add_prefix, content)

            if content != original_content:
                with open(html_file, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"Fixed paths in {html_file.relative_to(root_dir)}")

            if content != original_content:
                with open(html_file, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"Fixed paths in {html_file.relative_to(root_dir)}")

if __name__ == "__main__":
    fix_paths()
