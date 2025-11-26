#!/usr/bin/env python3
"""
Update product schema with random prices between 500-10000
"""

import os
import re
import random

products_dir = 'products'

# Set random seed for reproducibility (same products get same prices)
random.seed(42)

updated_count = 0

# Get all HTML files in products directory
for filename in sorted(os.listdir(products_dir)):
    if not filename.endswith('.html'):
        continue
    
    filepath = os.path.join(products_dir, filename)
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Generate random price for this product (500 to 10000)
        price = random.randint(500, 10000)
        
        # Replace "price": "0" with random price
        new_content = re.sub(
            r'"price":\s*"0"',
            f'"price": "{price}"',
            content
        )
        
        if new_content != content:
            # Write back
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            
            print(f"✅ Updated {filename}: ₹{price}")
            updated_count += 1
        else:
            print(f"⚠️  No price found: {filename}")
    
    except Exception as e:
        print(f"❌ Error updating {filename}: {e}")

print(f"\n🎉 Updated {updated_count} product pages with random prices!")
print("Prices range from ₹500 to ₹10,000")
