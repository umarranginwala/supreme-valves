#!/usr/bin/env python3
"""
Update product images to use properly URL-encoded paths
"""

import os
import re

# Product directory
products_dir = 'products'

# Files to update
files_to_update = [
    'gate-valve.html', 'knife-edge-gate-valve.html', 'blow-down-valve.html',
    'check-valve.html', 'piston-valve.html', 'dual-plate-check-valve.html',
    'safety-relief-valve.html', 'single-piece-ball-valve.html', 'two-piece-ball-valve.html',
    'three-piece-ball-valve.html', 'butterfly-valve.html', 'lift-check-valve.html',
    'ball-valve-actuator.html', 'flush-bottom-valve.html', 'globe-valve.html',
    'moisture-separator.html', 'pressure-reducing-valve.html', 'non-slam-check-valve.html',
    'ball-valve.html', 'three-way-ball-valve.html', 'wafer-check-valve.html',
    'motorized-control-valve.html', 'steam-trap-thermodynamic.html', 'needle-valve.html',
    'basket-strainer.html', 'sight-glass.html', 'swing-check-valve.html'
]

# Old and new image paths
old_path = '../assets/Valves and Projects/hero_image.jpeg'
new_path = '../assets/Valves%20and%20Projects/hero_image.jpeg'

old_schema_path = 'https://www.supremevalves.in/assets/Valves and Projects/hero_image.jpeg'
new_schema_path = 'https://www.supremevalves.in/assets/Valves%20and%20Projects/hero_image.jpeg'

updated_count = 0

for filename in files_to_update:
    filepath = os.path.join(products_dir, filename)
    
    if not os.path.exists(filepath):
        print(f"⚠️  File not found: {filepath}")
        continue
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace both occurrences
        original_content = content
        content = content.replace(old_path, new_path)
        content = content.replace(old_schema_path, new_schema_path)
        
        if content != original_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✅ Updated: {filename}")
            updated_count += 1
        else:
            print(f"⏭️  No changes needed: {filename}")
    
    except Exception as e:
        print(f"❌ Error updating {filename}: {e}")

print(f"\n🎉 Updated {updated_count} files successfully!")
