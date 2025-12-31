#!/usr/bin/env python3
"""
Generate complete product feed XML from all product HTML files
"""

import os
import re
import json
from pathlib import Path
from datetime import datetime

# Product directory
PRODUCTS_DIR = "products"
BASE_URL = "https://www.supremevalves.in"

def calculate_price(title, material, valve_type):
    """Calculate realistic price based on valve type, material, and features"""
    base_prices = {
        'ball valve': 4500,
        'gate valve': 5500,
        'globe valve': 6000,
        'check valve': 3500,
        'butterfly valve': 7000,
        'control valve': 12000,
        'safety valve': 9500,
        'relief valve': 9500,
        'plug valve': 5000,
        'needle valve': 3000,
        'diaphragm valve': 8000,
        'strainer': 3500,
        'steam trap': 4000,
        'sight glass': 2000,
        'knife gate': 5500,
        'foot valve': 4000
    }
    
    # Determine base price from valve type
    title_lower = title.lower()
    price = 5000  # default
    
    for valve_name, base_price in base_prices.items():
        if valve_name in title_lower:
            price = base_price
            break
    
    # Material multipliers
    material_multipliers = {
        'Stainless Steel': 1.8,
        'Forged Steel': 1.6,
        'Carbon Steel': 1.3,
        'Bronze': 1.4,
        'Brass': 1.2,
        'Cast Iron': 1.0
    }
    price *= material_multipliers.get(material, 1.0)
    
    # Feature-based adjustments
    if 'three piece' in title_lower or '3pc' in title_lower:
        price *= 1.3
    elif 'two piece' in title_lower or '2pc' in title_lower:
        price *= 1.15
    
    if 'actuator' in title_lower or 'motorized' in title_lower or 'pneumatic' in title_lower or 'electric' in title_lower:
        price *= 2.5
    
    if 'fire safe' in title_lower or 'fire-safe' in title_lower:
        price *= 1.4
    
    if 'cryogenic' in title_lower:
        price *= 1.8
    
    if 'trunnion' in title_lower:
        price *= 1.5
    
    if 'pressure seal' in title_lower:
        price *= 1.6
    
    if 'triple offset' in title_lower:
        price *= 1.7
    
    if 'ptfe lined' in title_lower or 'lined' in title_lower:
        price *= 1.4
    
    if 'jacketed' in title_lower:
        price *= 1.5
    
    if 'forged' in title_lower:
        price *= 1.4
    
    if 'nab' in title_lower:
        price *= 1.3
    
    if 'duplex' in title_lower:
        price *= 1.6
    
    if 'custom' in title_lower:
        price *= 1.5
    
    # Class/pressure rating adjustments
    if '300' in title_lower or 'class 300' in title_lower:
        price *= 1.3
    elif '150' in title_lower or 'class 150' in title_lower:
        price *= 1.1
    
    # Size adjustments (approximate)
    if '10 inch' in title_lower or '10inch' in title_lower:
        price *= 1.4
    elif 'dn150' in title_lower:
        price *= 1.2
    elif 'dn100' in title_lower:
        price *= 1.1
    
    # Round to nearest 100
    price = round(price / 100) * 100
    
    # Ensure minimum price
    if price < 800:
        price = 800
    
    return str(int(price))

def extract_product_data(html_file):
    """Extract product data from HTML file"""
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    product = {
        'id': Path(html_file).stem,
        'title': '',
        'description': '',
        'link': f"{BASE_URL}/products/{Path(html_file).name}",
        'image_link': f"{BASE_URL}/assets/Valves%20and%20Projects/hero_image.jpeg",
        'price': '5000',
        'availability': 'in stock',
        'condition': 'new',
        'brand': 'Supreme Valves India',
        'material': 'Cast Iron',
        'product_type': 'Industrial Valves'
    }
    
    # Extract title from <title> tag
    title_match = re.search(r'<title>([^<]+)</title>', content)
    if title_match:
        title = title_match.group(1)
        # Clean up title - remove " | Supreme Valves India" suffix
        title = re.sub(r'\s*\|\s*Supreme Valves India.*$', '', title)
        product['title'] = title.strip()
    
    # Extract description from meta description
    desc_match = re.search(r'<meta name="description" content="([^"]+)"', content)
    if desc_match:
        product['description'] = desc_match.group(1).strip()
    
    # Extract price from JSON-LD if available
    price_match = re.search(r'"price":\s*"(\d+)"', content)
    if price_match:
        product['price'] = price_match.group(1)
    
    # Extract image from JSON-LD if available
    image_match = re.search(r'"image":\s*"([^"]+)"', content)
    if image_match:
        product['image_link'] = image_match.group(1)
    
    # Determine material from title/description
    title_lower = product['title'].lower()
    desc_lower = product['description'].lower()
    
    if 'stainless steel' in title_lower or 'ss' in title_lower or 's.s' in title_lower:
        product['material'] = 'Stainless Steel'
    elif 'carbon steel' in title_lower or 'cs' in title_lower or 'c.s' in title_lower:
        product['material'] = 'Carbon Steel'
    elif 'cast iron' in title_lower or 'ci' in title_lower or 'c.i' in title_lower:
        product['material'] = 'Cast Iron'
    elif 'brass' in title_lower:
        product['material'] = 'Brass'
    elif 'bronze' in title_lower:
        product['material'] = 'Bronze'
    elif 'forged' in title_lower:
        product['material'] = 'Forged Steel'
    
    # Determine product type from title
    if 'ball valve' in title_lower:
        product['product_type'] = 'Ball Valves'
        product['google_product_category'] = '632'
    elif 'gate valve' in title_lower:
        product['product_type'] = 'Gate Valves'
        product['google_product_category'] = '632'
    elif 'globe valve' in title_lower:
        product['product_type'] = 'Globe Valves'
        product['google_product_category'] = '632'
    elif 'check valve' in title_lower or 'nrv' in title_lower:
        product['product_type'] = 'Check Valves'
        product['google_product_category'] = '632'
    elif 'butterfly valve' in title_lower:
        product['product_type'] = 'Butterfly Valves'
        product['google_product_category'] = '632'
    elif 'control valve' in title_lower:
        product['product_type'] = 'Control Valves'
        product['google_product_category'] = '632'
    elif 'safety' in title_lower or 'relief' in title_lower:
        product['product_type'] = 'Safety & Relief Valves'
        product['google_product_category'] = '632'
    elif 'strainer' in title_lower:
        product['product_type'] = 'Strainers'
        product['google_product_category'] = '632'
    elif 'plug valve' in title_lower:
        product['product_type'] = 'Plug Valves'
        product['google_product_category'] = '632'
    elif 'needle valve' in title_lower:
        product['product_type'] = 'Needle Valves'
        product['google_product_category'] = '632'
    elif 'diaphragm valve' in title_lower:
        product['product_type'] = 'Diaphragm Valves'
        product['google_product_category'] = '632'
    
    # Calculate intelligent price
    product['price'] = calculate_price(product['title'], product['material'], product['product_type'])
    
    return product

def generate_feed_xml(products):
    """Generate RSS 2.0 XML feed"""
    xml = '''<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0" xmlns:g="http://base.google.com/ns/1.0">
  <channel>
    <title>Supreme Valves India - Product Feed</title>
    <link>https://www.supremevalves.in</link>
    <description>Industrial Valves - Complete Product Catalog</description>
'''
    
    for product in products:
        xml += f'''    <item>
      <g:id>{product['id']}</g:id>
      <g:title><![CDATA[{product['title']}]]></g:title>
      <g:description><![CDATA[{product['description']}]]></g:description>
      <g:link>{product['link']}</g:link>
      <g:image_link>{product['image_link']}</g:image_link>
      <g:price>{product['price']} INR</g:price>
      <g:availability>{product['availability']}</g:availability>
      <g:condition>{product['condition']}</g:condition>
      <g:brand>{product['brand']}</g:brand>
      <g:product_type>{product['product_type']}</g:product_type>
      <g:google_product_category>{product.get('google_product_category', '632')}</g:google_product_category>
      <g:mpn>{product['id']}</g:mpn>
      <g:material>{product['material']}</g:material>
      <g:custom_label_0>Industrial Valves</g:custom_label_0>
      <g:custom_label_1>Made in India</g:custom_label_1>
    </item>
'''
    
    xml += '''  </channel>
</rss>'''
    
    return xml

def main():
    """Main function"""
    print("Scanning product directory...")
    
    products = []
    product_files = sorted(Path(PRODUCTS_DIR).glob('*.html'))
    
    print(f"Found {len(product_files)} product files")
    
    for html_file in product_files:
        print(f"Processing: {html_file.name}")
        try:
            product = extract_product_data(html_file)
            if product['title']:  # Only add if we found a title
                products.append(product)
        except Exception as e:
            print(f"  Error: {e}")
    
    print(f"\nExtracted {len(products)} products")
    
    # Generate XML
    xml_content = generate_feed_xml(products)
    
    # Write to file
    output_file = 'google_feed.xml'
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(xml_content)
    
    print(f"\nProduct feed generated: {output_file}")
    print(f"Total products in feed: {len(products)}")
    
    # Print summary by type
    types = {}
    for p in products:
        ptype = p['product_type']
        types[ptype] = types.get(ptype, 0) + 1
    
    print("\nProducts by type:")
    for ptype, count in sorted(types.items()):
        print(f"  {ptype}: {count}")

if __name__ == '__main__':
    main()
