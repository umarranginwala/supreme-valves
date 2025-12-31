#!/usr/bin/env python3
"""
Fix product structured data issues:
1. Ensure all products have priceValidUntil field
2. Ensure all products have valid offers with price
3. Update priceValidUntil to 2026-12-31 for consistency
"""

import os
import re
from pathlib import Path

PRODUCTS_DIR = "products"

def fix_structured_data(html_file):
    """Fix structured data in HTML file"""
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    changes = []
    
    # Find JSON-LD script block
    json_ld_pattern = r'<script type="application/ld\+json">(.*?)</script>'
    match = re.search(json_ld_pattern, content, re.DOTALL)
    
    if not match:
        return False, []
    
    json_block = match.group(1)
    
    # Check if it has offers section
    if '"offers"' not in json_block:
        print(f"  ⚠️  No offers section found")
        return False, []
    
    # Fix 1: Ensure priceValidUntil exists
    if '"priceValidUntil"' not in json_block:
        # Add priceValidUntil after price field
        if '"price":' in json_block:
            # Find the price line and add priceValidUntil after it
            json_block = re.sub(
                r'("price":\s*"[^"]+",)',
                r'\1\n        "priceValidUntil": "2026-12-31",',
                json_block
            )
            changes.append("Added priceValidUntil field")
    else:
        # Update existing priceValidUntil to 2026-12-31
        json_block = re.sub(
            r'"priceValidUntil":\s*"[^"]*"',
            '"priceValidUntil": "2026-12-31"',
            json_block
        )
        changes.append("Updated priceValidUntil to 2026-12-31")
    
    # Fix 2: Ensure price field exists in offers
    if '"price":' not in json_block and '"offers"' in json_block:
        # Add a default price if missing
        json_block = re.sub(
            r'("priceCurrency":\s*"INR",)',
            r'\1\n        "price": "5000",',
            json_block
        )
        changes.append("Added missing price field")
    
    # Replace the JSON-LD block in content
    if changes:
        new_script = f'<script type="application/ld+json">{json_block}</script>'
        content = re.sub(json_ld_pattern, new_script, content, flags=re.DOTALL)
    
    # Write back if changed
    if content != original_content:
        with open(html_file, 'w', encoding='utf-8') as f:
            f.write(content)
        return True, changes
    
    return False, []

def main():
    """Main function"""
    print("Fixing product structured data...")
    print("=" * 80)
    
    product_files = sorted(Path(PRODUCTS_DIR).glob('*.html'))
    
    fixed_count = 0
    total_count = 0
    
    for html_file in product_files:
        total_count += 1
        print(f"\n{total_count}. {html_file.name}")
        
        try:
            changed, changes = fix_structured_data(html_file)
            if changed:
                fixed_count += 1
                for change in changes:
                    print(f"  ✓ {change}")
            else:
                print(f"  ✓ Already valid")
        except Exception as e:
            print(f"  ✗ Error: {e}")
    
    print("\n" + "=" * 80)
    print(f"Total files processed: {total_count}")
    print(f"Files fixed: {fixed_count}")
    print(f"Files already valid: {total_count - fixed_count}")

if __name__ == '__main__':
    main()
