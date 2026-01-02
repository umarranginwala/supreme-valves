import json
import re

def parse_boss_content(file_path):
    with open(file_path, "r") as f:
        content = f.read()

    pages = content.split("--- PAGE BREAK ---")
    products = []

    for page in pages:
        if not page.strip():
            continue
            
        lines = [l.strip() for l in page.split('\n') if l.strip()]
        if not lines:
            continue
            
        title = ""
        # Improved title detection
        for i, line in enumerate(lines):
            if "BOSS" in line.upper() and len(line) > 5:
                title = line
                break
        
        if not title and len(lines) > 0:
            title = lines[0]

        # Normalize page text for better regex matching (remove spaces in common keywords)
        norm_page = re.sub(r'M\s*A\s*T\s*E\s*R\s*I\s*A\s*L\s*S', 'MATERIALS', page, flags=re.I)
        norm_page = re.sub(r'D\s*I\s*M\s*E\s*N\s*S\s*I\s*O\s*N\s*S', 'DIMENSIONS', norm_page, flags=re.I)
        norm_page = re.sub(r'T\s*E\s*S\s*T\s*E\s*D\s*&\s*S\s*U\s*I\s*T\s*A\s*B\s*I\s*L\s*I\s*T\s*Y', 'TESTED & SUITABILITY', norm_page, flags=re.I)
        norm_page = re.sub(r'D\s*E\s*S\s*C\s*R\s*I\s*P\s*T\s*I\s*O\s*N', 'DESCRIPTION', norm_page, flags=re.I)

        # Extract Description
        description = ""
        desc_match = re.search(r"DESCRIPTION\s+(.*?)(?=TESTED|DIMENSIONS|MATERIALS|---|$)", norm_page, re.S | re.I)
        if desc_match:
            description = desc_match.group(1).strip().replace('\n', ' ')

        # Extract Testing & Suitability
        testing = []
        suitability = ""
        test_match = re.search(r"TESTED\s+&\s+SUITABILITY\s+(.*?)(?=DIMENSIONS|MATERIALS|---|$)", norm_page, re.S | re.I)
        if not test_match:
             test_match = re.search(r"TEST\s+&\s+SUITABILITY\s+(.*?)(?=DIMENSIONS|MATERIALS|---|$)", norm_page, re.S | re.I)
        
        if test_match:
            test_content = test_match.group(1).strip()
            for line in test_content.split('\n'):
                if "SUITABLE" in line.upper():
                    suitability = line.split(":", 1)[1].strip() if ":" in line else line
                elif line.strip():
                    testing.append(line.strip())

        # Extract Materials (MOC)
        materials = []
        mat_match = re.search(r"MATERIALS\s+(.*?)(?=DIMENSIONS|DESCRIPTION|TESTED|---|$)", norm_page, re.S | re.I)
        if mat_match:
            mat_lines = mat_match.group(1).strip().split('\n')
            for line in mat_lines:
                line = line.strip()
                if line and not any(kw in line.upper() for kw in ["P. NO.", "NAME OF PARTS", "SPECIFICATION"]):
                    # Clean up some common noise
                    if not re.match(r'^[0-9\s]+$', line): # Not just numbers
                        materials.append(line)

        # Extract Dimensions
        dimensions = []
        dim_match = re.search(r"DIMENSIONS\s+(.*?)(?=MATERIALS|DESCRIPTION|TESTED|---|$)", norm_page, re.S | re.I)
        if dim_match:
            dim_lines = dim_match.group(1).strip().split('\n')
            for line in dim_lines:
                if any(char.isdigit() for char in line):
                    dimensions.append(line.strip())

        if title == "BOSS VALVES" and description:
            # Try to get a better title from description
            desc_lines = description.split("  ")
            if desc_lines:
                title = f"BOSS {desc_lines[0]}"

        if title:
            # Generate ID
            product_id = re.sub(r'[^a-z0-9]+', '-', title.lower()).strip('-')
            
            # Additional cleanup for materials
            cleaned_materials = []
            for m in materials:
                if not any(x in m.upper() for x in ["WE HAVE NO SISTER CONCERN", "ANYWHERE IN INDIA", "BOSS VALVES", "MOUNTINGS"]):
                    cleaned_materials.append(m)

            products.append({
                "id": product_id,
                "name": title,
                "description": description,
                "testing": testing,
                "suitability": suitability,
                "materials": cleaned_materials,
                "dimensions": dimensions,
                "category": "BOSS Industrial Valves"
            })

    return products

if __name__ == "__main__":
    products = parse_boss_content("boss_content.txt")
    with open("boss_products.json", "w") as f:
        json.dump(products, f, indent=2)
    print(f"Parsed {len(products)} products to boss_products.json")
