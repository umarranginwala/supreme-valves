
import os
import re
import urllib.parse
from pathlib import Path

def check_links():
    root_dir = Path('/Users/umarranginwala/Downloads/supremevalves_site_v3')
    html_files = list(root_dir.glob('**/*.html'))
    
    broken_links = []
    
    for html_file in html_files:
        if 'node_modules' in str(html_file):
            continue
            
        with open(html_file, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
            
            # Find all local hrefs and srcs
            links = re.findall(r'(?:href|src)="([^"#:][^:"]*)"', content)
            
            for link in links:
                if link.startswith('http') or link.startswith('mailto:') or link.startswith('tel:') or link.startswith('data:'):
                    continue
                
                # Ignore template strings like ${...} or {...}
                if '${' in link or ('{' in link and '}' in link):
                    continue
                
                # Handle query params
                clean_link = link.split('?')[0]
                if not clean_link:
                    continue
                
                # Decode URL encoding (e.g., %20 to space)
                decoded_link = urllib.parse.unquote(clean_link)
                
                # Resolve path relative to the current html file
                link_path = (html_file.parent / decoded_link).resolve()
                
                # Check if it's within the project root
                try:
                    link_path.relative_to(root_dir)
                except ValueError:
                    # Link points outside root, might be intended but let's skip for now
                    continue
                
                if not link_path.exists():
                    broken_links.append({
                        'file': str(html_file.relative_to(root_dir)),
                        'link': link,
                        'resolved': str(link_path)
                    })
                    
    return broken_links

if __name__ == "__main__":
    broken = check_links()
    if broken:
        print(f"Found {len(broken)} broken links:")
        for b in broken:
            print(f"In {b['file']}: {b['link']} (points to non-existent {b['resolved']})")
    else:
        print("No broken internal links found!")
