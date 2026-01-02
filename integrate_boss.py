import json
import os
import re

def slugify(text):
    return re.sub(r'[^a-z0-9]+', '-', text.lower()).strip('-')

def integrate_boss_products():
    with open('boss_products.json', 'r') as f:
        boss_products = json.load(f)
    
    with open('data/products.json', 'r') as f:
        site_data = json.load(f)
    
    existing_ids = {p['id'] for p in site_data['products']}
    
    new_products_count = 0
    for bp in boss_products:
        # Create a unique ID
        base_id = bp['id']
        if base_id in existing_ids:
            # Check if it's actually the same product or just same name
            # For BOSS products, we'll prefix if needed or just use the BOSS ID
            pass
        
        # Format for data/products.json
        new_p = {
            "id": bp['id'],
            "name": bp['name'],
            "shortName": bp['name'].replace("BOSS ", ""),
            "category": "BOSS Industrial Valves",
            "image": "assets/Valves and Projects/hero_image.jpeg", # Placeholder for now
            "description": bp['description'],
            "applications": bp.get('suitability', '').split(' & ') if bp.get('suitability') else ["Industrial Systems"],
            "featured": False
        }
        
        if new_p['id'] not in existing_ids:
            site_data['products'].append(new_p)
            existing_ids.add(new_p['id'])
            new_products_count += 1

    with open('data/products.json', 'w') as f:
        json.dump(site_data, f, indent=2)
    
    print(f"Integrated {new_products_count} new products into data/products.json")

def update_js_data():
    with open('boss_products.json', 'r') as f:
        boss_products = json.load(f)
    
    # Read existing js/products-data.js
    with open('js/products-data.js', 'r') as f:
        js_content = f.read()
    
    # We'll add a new category "boss-valves"
    new_category_json = {
        "name": "BOSS Industrial Valves",
        "icon": "fa-award",
        "description": "Premium industrial valves and boiler mountings",
        "products": []
    }
    
    for bp in boss_products:
        new_category_json['products'].append({
            "name": bp['name'],
            "url": f"products/{bp['id']}.html",
            "tags": ["boss", "industrial", "premium"]
        })
    
    # Find the place to insert in productCategories
    # We'll use a regex to insert it before the closing brace of productCategories
    match = re.search(r'const productCategories = \{(.*?)\};', js_content, re.S)
    if match:
        categories_inner = match.group(1)
        # Check if boss-valves already exists
        if '"boss-valves"' not in categories_inner:
            new_cat_str = f',\n    "boss-valves": {json.dumps(new_category_json, indent=4)}'
            # Insert before the last closing brace
            updated_inner = categories_inner.rstrip() + new_cat_str
            new_js_content = js_content.replace(categories_inner, updated_inner)
            
            with open('js/products-data.js', 'w') as f:
                f.write(new_js_content)
            print("Updated js/products-data.js with boss-valves category")

if __name__ == "__main__":
    integrate_boss_products()
    update_js_data()
