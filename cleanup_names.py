import json
import re
import os

def clean_text(text):
    if not isinstance(text, str):
        return text
    
    # Common broken patterns from PDF extraction
    replacements = [
        (r'V\s+AL\s+VE', 'VALVE'),
        (r'V\s+A\s+L\s+V\s+E', 'VALVE'),
        (r'B\s+O\s+S\s+S', 'BOSS'),
        (r'BOSS\s+BOSS', 'BOSS'),
        (r'VALVE\s+,\s+S', 'VALVES'),
        (r'VALVE\s+S\b', 'VALVES'),
        (r'T\s+ANKER', 'TANKER'),
        (r'M\s+e\s+t\s+a\s+l\s*/\s*B\s+r\s+o\s+n\s+z\s+e', 'Metal/Bronze'),
        (r'B\s+r\s+o\s+n\s+z\s+e', 'Bronze'),
        (r'G\s+U\s+N\s+M\s+E\s+T\s+A\s+L', 'GUN METAL'),
        (r'Pegular', 'Regular'),
        (r'C\s+H\s+E\s+C\s+K', 'CHECK'),
        (r'L\s+I\s+F\s+T', 'LIFT'),
        (r'\s+,\s+', ', '), # Fix spaces around commas
        (r'\s{2,}', ' '),   # Collapse multiple spaces
    ]
    
    cleaned = text
    for pattern, repl in replacements:
        cleaned = re.sub(pattern, repl, cleaned, flags=re.IGNORECASE)
    
    return cleaned.strip()

def process_products_json():
    filepath = 'data/products.json'
    if not os.path.exists(filepath):
        print(f"File not found: {filepath}")
        return

    with open(filepath, 'r') as f:
        data = json.load(f)

    if 'products' in data:
        for product in data['products']:
            product['name'] = clean_text(product['name'])
            product['shortName'] = clean_text(product.get('shortName', ''))
            product['description'] = clean_text(product.get('description', ''))
            
            # Also fix ID if needed, but changing ID might break links. 
            # Ideally we keep IDs stable, but "boss-boss" is annoying.
            # For now, let's keep IDs as is to avoid breaking existing generated pages unless we rename them too.

    with open(filepath, 'w') as f:
        json.dump(data, f, indent=2)
    print(f"Cleaned {filepath}")

def process_js_file():
    filepath = 'js/products-data.js'
    if not os.path.exists(filepath):
        print(f"File not found: {filepath}")
        return

    with open(filepath, 'r') as f:
        content = f.read()

    # Apply same regex replacements to the whole content string
    # This is safer than parsing partial JS as JSON
    replacements = [
        (r'V\s+AL\s+VE', 'VALVE'),
        (r'V\s+A\s+L\s+V\s+E', 'VALVE'),
        (r'B\s+O\s+S\s+S', 'BOSS'),
        (r'BOSS\s+BOSS', 'BOSS'),
        (r'VALVE\s+,\s+S', 'VALVES'),
        (r'VALVE\s+S\b', 'VALVES'),
        (r'T\s+ANKER', 'TANKER'),
        (r'M\s+e\s+t\s+a\s+l\s*/\s*B\s+r\s+o\s+n\s+z\s+e', 'Metal/Bronze'),
        (r'B\s+r\s+o\s+n\s+z\s+e', 'Bronze'),
        (r'G\s+U\s+N\s+M\s+E\s+T\s+A\s+L', 'GUN METAL'),
        (r'Pegular', 'Regular'),
        (r'C\s+H\s+E\s+C\s+K', 'CHECK'),
        (r'L\s+I\s+F\s+T', 'LIFT'),
    ]

    cleaned = content
    for pattern, repl in replacements:
        cleaned = re.sub(pattern, repl, cleaned, flags=re.IGNORECASE)
    
    # Also fix multiple spaces that might have resulted
    cleaned = re.sub(r'name":\s*"([^"]+)"', lambda m: 'name": "' + re.sub(r'\s{2,}', ' ', m.group(1)) + '"', cleaned)

    with open(filepath, 'w') as f:
        f.write(cleaned)
    print(f"Cleaned {filepath}")

if __name__ == "__main__":
    process_products_json()
    process_js_file()
