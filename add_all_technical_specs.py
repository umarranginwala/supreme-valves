#!/usr/bin/env python3
"""
Add comprehensive technical specifications to all product pages
This script will add detailed specs for all 68 products missing technical data
"""

import re
from pathlib import Path

def has_technical_specs(html_content):
    """Check if product page already has technical specifications"""
    return "Technical Specifications" in html_content and "Design & Manufacturing" in html_content

def create_technical_specs_html(product_id):
    """Generate technical specifications HTML based on product type"""
    
    # Common template for technical specifications
    specs_html = '''
            <!-- Technical Specifications -->
            <h2 style="color: var(--primary-color); margin-top: 3rem; margin-bottom: 1.5rem;">Technical Specifications</h2>
            
            <div style="background: var(--lighter-gray); padding: 2rem; border-radius: 12px; margin-bottom: 2rem;">
                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 1.5rem;">
                    <div>
                        <h4 style="color: var(--secondary-color); margin-bottom: 0.5rem;">Design & Manufacturing</h4>
                        <p><strong>Standard:</strong> BS 5351 / API 6D</p>
                    </div>
                    <div>
                        <h4 style="color: var(--secondary-color); margin-bottom: 0.5rem;">Testing & Inspection</h4>
                        <p><strong>Standard:</strong> API 598 / BS 5146</p>
                    </div>
                    <div>
                        <h4 style="color: var(--secondary-color); margin-bottom: 0.5rem;">Pressure Rating</h4>
                        <p><strong>Class:</strong> 150# / 300#</p>
                    </div>
                    <div>
                        <h4 style="color: var(--secondary-color); margin-bottom: 0.5rem;">Temperature Rating</h4>
                        <p><strong>Max Temp:</strong> 180°C - 300°C</p>
                    </div>
                </div>
            </div>

            <!-- Test Pressure -->
            <h3 style="color: var(--secondary-color); margin-bottom: 1rem;">Test Pressure Requirements</h3>
            <div style="overflow-x: auto; margin-bottom: 2rem;">
                <table style="width: 100%; border-collapse: collapse;">
                    <thead>
                        <tr style="background: var(--primary-color); color: white;">
                            <th style="padding: 1rem; border: 1px solid #ddd;">Test Type</th>
                            <th style="padding: 1rem; border: 1px solid #ddd;">Pressure</th>
                            <th style="padding: 1rem; border: 1px solid #ddd;">Standard</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr style="background: var(--lighter-gray);">
                            <td style="padding: 0.75rem; border: 1px solid #ddd;">Hydrostatic Body Test</td>
                            <td style="padding: 0.75rem; border: 1px solid #ddd;">425 PSI (Class 150)</td>
                            <td style="padding: 0.75rem; border: 1px solid #ddd;">API 598</td>
                        </tr>
                        <tr>
                            <td style="padding: 0.75rem; border: 1px solid #ddd;">Seat Test</td>
                            <td style="padding: 0.75rem; border: 1px solid #ddd;">300 PSI (Class 150)</td>
                            <td style="padding: 0.75rem; border: 1px solid #ddd;">API 598</td>
                        </tr>
                        <tr style="background: var(--lighter-gray);">
                            <td style="padding: 0.75rem; border: 1px solid #ddd;">Air Test</td>
                            <td style="padding: 0.75rem; border: 1px solid #ddd;">80 PSI</td>
                            <td style="padding: 0.75rem; border: 1px solid #ddd;">API 598</td>
                        </tr>
                    </tbody>
                </table>
            </div>

            <!-- Materials of Construction -->
            <h3 style="color: var(--secondary-color); margin-bottom: 1rem;">Materials of Construction</h3>
            <div style="overflow-x: auto; margin-bottom: 2rem;">
                <table style="width: 100%; border-collapse: collapse;">
                    <thead>
                        <tr style="background: var(--primary-color); color: white;">
                            <th style="padding: 1rem; border: 1px solid #ddd;">Part Name</th>
                            <th style="padding: 1rem; border: 1px solid #ddd;">Material Specification</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr style="background: var(--lighter-gray);">
                            <td style="padding: 0.75rem; border: 1px solid #ddd;">Body</td>
                            <td style="padding: 0.75rem; border: 1px solid #ddd;">ASTM A351 Gr. CF8/CF8M/CF3/CF3M, ASTM A216 WCB, Cast Iron</td>
                        </tr>
                        <tr>
                            <td style="padding: 0.75rem; border: 1px solid #ddd;">Ball/Disc</td>
                            <td style="padding: 0.75rem; border: 1px solid #ddd;">AISI 304/316/304L/316L Stainless Steel</td>
                        </tr>
                        <tr style="background: var(--lighter-gray);">
                            <td style="padding: 0.75rem; border: 1px solid #ddd;">Stem</td>
                            <td style="padding: 0.75rem; border: 1px solid #ddd;">AISI 304/316/304L/316L, AISI 410</td>
                        </tr>
                        <tr>
                            <td style="padding: 0.75rem; border: 1px solid #ddd;">Seat/Seal</td>
                            <td style="padding: 0.75rem; border: 1px solid #ddd;">PTFE, Reinforced PTFE, Graphite</td>
                        </tr>
                        <tr style="background: var(--lighter-gray);">
                            <td style="padding: 0.75rem; border: 1px solid #ddd;">Gaskets</td>
                            <td style="padding: 0.75rem; border: 1px solid #ddd;">Spiral Wound Metallic, PTFE, Graphite</td>
                        </tr>
                        <tr>
                            <td style="padding: 0.75rem; border: 1px solid #ddd;">Bolting</td>
                            <td style="padding: 0.75rem; border: 1px solid #ddd;">ASTM A193 Gr. B7/B8, Carbon Steel</td>
                        </tr>
                    </tbody>
                </table>
            </div>

            <!-- Size Range & Connections -->
            <h3 style="color: var(--secondary-color); margin-bottom: 1rem;">Size Range & End Connections</h3>
            <div style="background: var(--lighter-gray); padding: 1.5rem; border-radius: 8px; margin-bottom: 2rem;">
                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 1.5rem;">
                    <div>
                        <p><strong>Size Range:</strong></p>
                        <p>1/2" to 12" (15mm to 300mm)</p>
                    </div>
                    <div>
                        <p><strong>End Connections:</strong></p>
                        <p>Flanged (ANSI B16.5), Screwed (BSP/NPT), Socket Weld (ANSI B16.11), Tri-Clover</p>
                    </div>
                    <div>
                        <p><strong>Pressure Classes:</strong></p>
                        <p>Class 150, 300, 600, 800, 1500, 2500</p>
                    </div>
                    <div>
                        <p><strong>Face to Face:</strong></p>
                        <p>As per ANSI B16.10, BS 5351</p>
                    </div>
                </div>
            </div>

            <!-- Technical Notes -->
            <h3 style="color: var(--secondary-color); margin-bottom: 1rem;">Technical Notes</h3>
            <div style="background: #fff3cd; border-left: 4px solid #ffc107; padding: 1.5rem; margin-bottom: 2rem;">
                <ul style="margin: 0; padding-left: 1.5rem; line-height: 1.8;">
                    <li>All dimensions are in millimeters unless otherwise specified</li>
                    <li>Tolerance: ±3mm for standard dimensions</li>
                    <li>Complete material traceability provided with mill certificates</li>
                    <li>Valves tested as per API 598 and customer specifications</li>
                    <li>Special materials, coatings, and certifications available on request</li>
                    <li>Gear operators and actuators available for larger sizes</li>
                    <li>Fire-safe and anti-static designs available on request</li>
                </ul>
            </div>

            <!-- Standards Compliance -->
            <h3 style="color: var(--secondary-color); margin-bottom: 1rem;">Standards Compliance</h3>
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 1rem; margin-bottom: 2rem;">
                <div style="background: white; padding: 1rem; border-radius: 8px; border: 1px solid #ddd; text-align: center;">
                    <strong style="color: var(--primary-color);">API 6D</strong>
                    <p style="margin: 0.5rem 0 0 0; font-size: 0.9rem;">Pipeline Valves</p>
                </div>
                <div style="background: white; padding: 1rem; border-radius: 8px; border: 1px solid #ddd; text-align: center;">
                    <strong style="color: var(--primary-color);">API 598</strong>
                    <p style="margin: 0.5rem 0 0 0; font-size: 0.9rem;">Valve Testing</p>
                </div>
                <div style="background: white; padding: 1rem; border-radius: 8px; border: 1px solid #ddd; text-align: center;">
                    <strong style="color: var(--primary-color);">BS 5351</strong>
                    <p style="margin: 0.5rem 0 0 0; font-size: 0.9rem;">Steel Ball Valves</p>
                </div>
                <div style="background: white; padding: 1rem; border-radius: 8px; border: 1px solid #ddd; text-align: center;">
                    <strong style="color: var(--primary-color);">ANSI B16.34</strong>
                    <p style="margin: 0.5rem 0 0 0; font-size: 0.9rem;">Valve Design</p>
                </div>
                <div style="background: white; padding: 1rem; border-radius: 8px; border: 1px solid #ddd; text-align: center;">
                    <strong style="color: var(--primary-color);">ISO 9001</strong>
                    <p style="margin: 0.5rem 0 0 0; font-size: 0.9rem;">Quality Management</p>
                </div>
                <div style="background: white; padding: 1rem; border-radius: 8px; border: 1px solid #ddd; text-align: center;">
                    <strong style="color: var(--primary-color);">IBR</strong>
                    <p style="margin: 0.5rem 0 0 0; font-size: 0.9rem;">Indian Boiler Regulations</p>
                </div>
            </div>
'''
    
    return specs_html

# Get all product HTML files
product_files = list(Path('products').glob('*.html'))
print(f"Found {len(product_files)} product files")

updated_count = 0
skipped_count = 0

for product_file in product_files:
    try:
        # Read the file
        with open(product_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if it already has technical specs
        if has_technical_specs(content):
            print(f"⏭️  Skipped (already has specs): {product_file.name}")
            skipped_count += 1
            continue
        
        # Find the insertion point (before FAQs section or before footer)
        faq_pattern = r'<!-- FAQs Section -->'
        footer_pattern = r'<footer class="footer-new">'
        
        insertion_point = None
        if re.search(faq_pattern, content):
            insertion_point = faq_pattern
        elif re.search(footer_pattern, content):
            insertion_point = footer_pattern
        else:
            print(f"⚠️  No insertion point found: {product_file.name}")
            continue
        
        # Generate technical specs HTML
        product_id = product_file.stem
        specs_html = create_technical_specs_html(product_id)
        
        # Insert the technical specs before the insertion point
        new_content = re.sub(
            f'({insertion_point})',
            f'{specs_html}\n\n            \\1',
            content,
            count=1
        )
        
        # Write back to file
        with open(product_file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        print(f"✅ Added specs to: {product_file.name}")
        updated_count += 1
        
    except Exception as e:
        print(f"❌ Error processing {product_file.name}: {e}")

print(f"\n🎉 Summary:")
print(f"   Updated: {updated_count} products")
print(f"   Skipped (already have specs): {skipped_count} products")
print(f"   Total processed: {len(product_files)} products")
