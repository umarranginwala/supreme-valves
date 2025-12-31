
import os
import re
from pathlib import Path

def inject_scripts():
    root_dir = Path('/Users/umarranginwala/Downloads/supremevalves_site_v3')
    
    # All directories to process including root
    dirs_to_process = ['', 'products', 'blog', 'faqs', 'countries', 'docs/technical-resources', 'projects']
    
    scripts_to_add = [
        'js/products-data.js',
        'js/product-search.js',
        'js/products.js',
        'js/form-handler.js',
        'js/navigation.js'
    ]

    for dir_name in dirs_to_process:
        dir_path = root_dir / dir_name
        if not dir_path.exists():
            continue
            
        depth = len(dir_name.split('/')) if dir_name else 0
        prefix = '../' * depth if depth > 0 else ''
        
        # Only process .html files directly in these directories (not recursively to avoid node_modules etc)
        for html_file in dir_path.glob('*.html'):
            with open(html_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original_content = content
            
            # Find the closing </body> tag
            if '</body>' not in content:
                continue
            
            # 1. Remove any existing script tags for these specific JS files and FontAwesome
            all_scripts_to_clean = scripts_to_add + ['https://kit.fontawesome.com/a076d05399.js', 'js/products-optimized.js']
            for script in all_scripts_to_clean:
                script_filename = script.split('/')[-1]
                # Match tags with src containing the filename, handling various path prefixes
                pattern = rf'<script[^>]*src="[^"]*{re.escape(script_filename)}"[^>]*></script>'
                content = re.sub(pattern, '', content)
            
            # Clean up FontAwesome specifically if it has different versions/patterns
            content = re.sub(rf'<script[^>]*src="[^"]*fontawesome[^"]*"[^>]*></script>', '', content)

            # 2. Prepare the clean block of scripts
            new_scripts = [
                '    <script src="https://kit.fontawesome.com/a076d05399.js" crossorigin="anonymous"></script>'
            ]
            for script in scripts_to_add:
                new_scripts.append(f'    <script src="{prefix}{script}"></script>')
            
            script_block = '\n'.join(new_scripts) + '\n</body>'
            
            # 3. Clean up extra newlines before </body> left by re.sub and inject the block
            content = re.sub(r'\n\s*\n</body>', '\n</body>', content)
            content = content.replace('</body>', script_block)

            if content != original_content:
                with open(html_file, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"Cleaned and injected scripts into {html_file.relative_to(root_dir)}")

if __name__ == "__main__":
    inject_scripts()
