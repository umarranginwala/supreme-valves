import json
import xml.etree.ElementTree as ET
from xml.dom import minidom
import os

def generate_feed():
    # Load products
    with open('data/products.json', 'r') as f:
        data = json.load(f)
    
    # Load config for company name and base URL
    # Assuming domain is supremevalves.in based on previous context, but let's check config.json
    base_url = "https://supremevalves.in" # Fallback
    
    products = data.get('products', [])
    
    # Create RSS element
    rss = ET.Element('rss', {
        'version': '2.0',
        'xmlns:g': 'http://base.google.com/ns/1.0'
    })
    
    channel = ET.SubElement(rss, 'channel')
    
    # Basic Channel Info
    ET.SubElement(channel, 'title').text = "Supreme Valves - Industrial Valves Product Feed"
    ET.SubElement(channel, 'link').text = base_url
    ET.SubElement(channel, 'description').text = "Official product feed for Supreme Valves India - Manufacturers of High Quality Industrial Valves."
    
    for product in products:
        item = ET.SubElement(channel, 'item')
        
        # Standard RSS tags
        ET.SubElement(item, 'g:id').text = product['id']
        ET.SubElement(item, 'title').text = product['name']
        ET.SubElement(item, 'description').text = product['description']
        ET.SubElement(item, 'link').text = f"{base_url}/products/{product['id']}.html"
        
        # Image link - handle relative paths
        image_path = product['image']
        if image_path.startswith('assets/'):
            image_url = f"{base_url}/{image_path}"
        else:
            image_url = f"{base_url}/assets/{image_path}"
        ET.SubElement(item, 'g:image_link').text = image_url
        
        # Google specific tags
        ET.SubElement(item, 'g:condition').text = "new"
        ET.SubElement(item, 'g:availability').text = "in_stock"
        
        # Price - Merchant Center requires price. Since it's B2B, we might need a placeholder or 0.00 INR
        # For industrial valves, prices are usually on request, but GMC needs a value.
        ET.SubElement(item, 'g:price').text = "0.00 INR" 
        
        ET.SubElement(item, 'g:brand').text = "Supreme Valves"
        
        # Category - Hardware > Plumbing > Plumbing Valves
        ET.SubElement(item, 'g:google_product_category').text = "Hardware > Plumbing > Plumbing Valves"
        ET.SubElement(item, 'g:product_type').text = product['category']
        
        # Shipping (optional but recommended)
        # shipping = ET.SubElement(item, 'g:shipping')
        # ET.SubElement(shipping, 'g:country').text = "IN"
        # ET.SubElement(shipping, 'g:service').text = "Standard"
        # ET.SubElement(shipping, 'g:price').text = "0.00 INR"

    # Save to file with pretty printing
    xml_str = ET.tostring(rss, encoding='utf-8')
    pretty_xml = minidom.parseString(xml_str).toprettyxml(indent="  ")
    
    with open('google_feed.xml', 'w', encoding='utf-8') as f:
        f.write(pretty_xml)
    
    print(f"Successfully generated google_feed.xml with {len(products)} products.")

if __name__ == "__main__":
    generate_feed()
