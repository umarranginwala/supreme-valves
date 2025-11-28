#!/usr/bin/env python3
"""
Replace 'manufacturer' with 'exporter' across all website files
Handles various cases: Manufacturer, manufacturer, MANUFACTURER
"""

import os
import re
from pathlib import Path

def replace_in_file(file_path):
    """Replace manufacturer with exporter in a file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Replace all variations
        # Manufacturer -> Exporter
        content = re.sub(r'\bManufacturer\b', 'Exporter', content)
        # manufacturer -> exporter
        content = re.sub(r'\bmanufacturer\b', 'exporter', content)
        # MANUFACTURER -> EXPORTER
        content = re.sub(r'\bMANUFACTURER\b', 'EXPORTER', content)
        # Manufacturers -> Exporters
        content = re.sub(r'\bManufacturers\b', 'Exporters', content)
        # manufacturers -> exporters
        content = re.sub(r'\bmanufacturers\b', 'exporters', content)
        # MANUFACTURERS -> EXPORTERS
        content = re.sub(r'\bMANUFACTURERS\b', 'EXPORTERS', content)
        # Manufacturing -> Exporting (for "Design & Manufacturing")
        content = re.sub(r'\bManufacturing\b', 'Exporting', content)
        # manufacturing -> exporting
        content = re.sub(r'\bmanufacturing\b', 'exporting', content)
        
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
        return False
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return False

# File types to process
file_patterns = [
    '*.html',
    '*.json',
    '*.xml',
    '*.txt',
    '*.md'
]

# Directories to search
search_dirs = [
    '.',
    'products',
    'countries',
    'faqs',
    'projects',
    'blog',
    'docs/technical-resources',
    'data'
]

updated_files = []
total_files = 0

for search_dir in search_dirs:
    if not Path(search_dir).exists():
        continue
    
    for pattern in file_patterns:
        for file_path in Path(search_dir).glob(pattern):
            # Skip certain files
            if file_path.name in ['package.json', 'package-lock.json', 'node_modules']:
                continue
            
            total_files += 1
            if replace_in_file(file_path):
                updated_files.append(str(file_path))
                print(f"✅ Updated: {file_path}")

print(f"\n🎉 Summary:")
print(f"   Files scanned: {total_files}")
print(f"   Files updated: {len(updated_files)}")
print(f"\n📝 Replacements made:")
print(f"   Manufacturer → Exporter")
print(f"   manufacturer → exporter")
print(f"   Manufacturers → Exporters")
print(f"   manufacturers → exporters")
print(f"   Manufacturing → Exporting")
