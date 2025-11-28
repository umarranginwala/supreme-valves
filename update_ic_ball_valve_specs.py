#!/usr/bin/env python3
"""
Update IC Ball Valve product pages with detailed technical specifications
"""

import os
import re

def update_ic_ball_valve_3pc_screw_end():
    """Update IC Ball Valve 3PC Screw End with technical specs"""
    
    filepath = 'products/ic-ball-valve-3pc-screw-end.html'
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find and replace the Features & Benefits section with Technical Specifications
    old_section = re.search(r'<!-- Features & Benefits -->.*?</section>', content, re.DOTALL)
    
    if old_section:
        new_section = '''<!-- Technical Specifications -->
        <section style="margin-bottom: 4rem;">
            <h2 style="color: var(--primary-color); margin-bottom: 2rem; border-bottom: 3px solid var(--accent-color); padding-bottom: 0.5rem;">Technical Specifications</h2>
            
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 2rem; margin-bottom: 3rem;">
                <div>
                    <h3 style="color: var(--secondary-color); margin-bottom: 1rem;">Design Standards</h3>
                    <table style="width: 100%; border-collapse: collapse;">
                        <tr style="background: var(--lighter-gray);">
                            <td style="padding: 0.75rem; border: 1px solid #ddd; font-weight: 600;">Design & Manufacturing</td>
                            <td style="padding: 0.75rem; border: 1px solid #ddd;">BS 5351 / API 602</td>
                        </tr>
                        <tr>
                            <td style="padding: 0.75rem; border: 1px solid #ddd; font-weight: 600;">Testing & Inspection</td>
                            <td style="padding: 0.75rem; border: 1px solid #ddd;">API 598 / BS 5146</td>
                        </tr>
                        <tr style="background: var(--lighter-gray);">
                            <td style="padding: 0.75rem; border: 1px solid #ddd; font-weight: 600;">End Connections</td>
                            <td style="padding: 0.75rem; border: 1px solid #ddd;">BSP / NPT / Socket Weld</td>
                        </tr>
                        <tr>
                            <td style="padding: 0.75rem; border: 1px solid #ddd; font-weight: 600;">Socket Weld End to</td>
                            <td style="padding: 0.75rem; border: 1px solid #ddd;">ANSI B 16.11</td>
                        </tr>
                    </table>
                </div>

                <div>
                    <h3 style="color: var(--secondary-color); margin-bottom: 1rem;">Pressure Ratings (Class 150)</h3>
                    <table style="width: 100%; border-collapse: collapse;">
                        <tr style="background: var(--lighter-gray);">
                            <td style="padding: 0.75rem; border: 1px solid #ddd; font-weight: 600;">Body Hydro Test</td>
                            <td style="padding: 0.75rem; border: 1px solid #ddd;">425 PSI</td>
                        </tr>
                        <tr>
                            <td style="padding: 0.75rem; border: 1px solid #ddd; font-weight: 600;">Seat Test</td>
                            <td style="padding: 0.75rem; border: 1px solid #ddd;">300 PSI</td>
                        </tr>
                        <tr style="background: var(--lighter-gray);">
                            <td style="padding: 0.75rem; border: 1px solid #ddd; font-weight: 600;">Air Test - Seat</td>
                            <td style="padding: 0.75rem; border: 1px solid #ddd;">80 PSI</td>
                        </tr>
                        <tr>
                            <td style="padding: 0.75rem; border: 1px solid #ddd; font-weight: 600;">Max Temperature</td>
                            <td style="padding: 0.75rem; border: 1px solid #ddd;">180°C</td>
                        </tr>
                    </table>
                </div>
            </div>

            <!-- Dimensions Table -->
            <h3 style="color: var(--secondary-color); margin-bottom: 1rem;">Dimensions (mm)</h3>
            <div style="overflow-x: auto;">
                <table style="width: 100%; border-collapse: collapse; margin-bottom: 2rem;">
                    <thead>
                        <tr style="background: var(--primary-color); color: white;">
                            <th style="padding: 1rem; border: 1px solid #ddd;">Size (Inch)</th>
                            <th style="padding: 1rem; border: 1px solid #ddd;">Size (MM)</th>
                            <th style="padding: 1rem; border: 1px solid #ddd;">A</th>
                            <th style="padding: 1rem; border: 1px solid #ddd;">ØB</th>
                            <th style="padding: 1rem; border: 1px solid #ddd;">L</th>
                            <th style="padding: 1rem; border: 1px solid #ddd;">Socket Weld Hole</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr style="background: var(--lighter-gray);">
                            <td style="padding: 0.75rem; border: 1px solid #ddd; text-align: center;">1/2"</td>
                            <td style="padding: 0.75rem; border: 1px solid #ddd; text-align: center;">15</td>
                            <td style="padding: 0.75rem; border: 1px solid #ddd; text-align: center;">77</td>
                            <td style="padding: 0.75rem; border: 1px solid #ddd; text-align: center;">13</td>
                            <td style="padding: 0.75rem; border: 1px solid #ddd; text-align: center;">115</td>
                            <td style="padding: 0.75rem; border: 1px solid #ddd; text-align: center;">22</td>
                        </tr>
                        <tr>
                            <td style="padding: 0.75rem; border: 1px solid #ddd; text-align: center;">3/4"</td>
                            <td style="padding: 0.75rem; border: 1px solid #ddd; text-align: center;">20</td>
                            <td style="padding: 0.75rem; border: 1px solid #ddd; text-align: center;">81</td>
                            <td style="padding: 0.75rem; border: 1px solid #ddd; text-align: center;">19</td>
                            <td style="padding: 0.75rem; border: 1px solid #ddd; text-align: center;">135</td>
                            <td style="padding: 0.75rem; border: 1px solid #ddd; text-align: center;">26.5</td>
                        </tr>
                        <tr style="background: var(--lighter-gray);">
                            <td style="padding: 0.75rem; border: 1px solid #ddd; text-align: center;">1"</td>
                            <td style="padding: 0.75rem; border: 1px solid #ddd; text-align: center;">25</td>
                            <td style="padding: 0.75rem; border: 1px solid #ddd; text-align: center;">90</td>
                            <td style="padding: 0.75rem; border: 1px solid #ddd; text-align: center;">25</td>
                            <td style="padding: 0.75rem; border: 1px solid #ddd; text-align: center;">134</td>
                            <td style="padding: 0.75rem; border: 1px solid #ddd; text-align: center;">34.1</td>
                        </tr>
                        <tr>
                            <td style="padding: 0.75rem; border: 1px solid #ddd; text-align: center;">1-1/4"</td>
                            <td style="padding: 0.75rem; border: 1px solid #ddd; text-align: center;">32</td>
                            <td style="padding: 0.75rem; border: 1px solid #ddd; text-align: center;">99</td>
                            <td style="padding: 0.75rem; border: 1px solid #ddd; text-align: center;">32</td>
                            <td style="padding: 0.75rem; border: 1px solid #ddd; text-align: center;">165</td>
                            <td style="padding: 0.75rem; border: 1px solid #ddd; text-align: center;">43</td>
                        </tr>
                        <tr style="background: var(--lighter-gray);">
                            <td style="padding: 0.75rem; border: 1px solid #ddd; text-align: center;">1-1/2"</td>
                            <td style="padding: 0.75rem; border: 1px solid #ddd; text-align: center;">40</td>
                            <td style="padding: 0.75rem; border: 1px solid #ddd; text-align: center;">113</td>
                            <td style="padding: 0.75rem; border: 1px solid #ddd; text-align: center;">38</td>
                            <td style="padding: 0.75rem; border: 1px solid #ddd; text-align: center;">170</td>
                            <td style="padding: 0.75rem; border: 1px solid #ddd; text-align: center;">49</td>
                        </tr>
                        <tr>
                            <td style="padding: 0.75rem; border: 1px solid #ddd; text-align: center;">2"</td>
                            <td style="padding: 0.75rem; border: 1px solid #ddd; text-align: center;">50</td>
                            <td style="padding: 0.75rem; border: 1px solid #ddd; text-align: center;">132</td>
                            <td style="padding: 0.75rem; border: 1px solid #ddd; text-align: center;">50</td>
                            <td style="padding: 0.75rem; border: 1px solid #ddd; text-align: center;">170</td>
                            <td style="padding: 0.75rem; border: 1px solid #ddd; text-align: center;">61</td>
                        </tr>
                        <tr style="background: var(--lighter-gray);">
                            <td style="padding: 0.75rem; border: 1px solid #ddd; text-align: center;">2-1/2"</td>
                            <td style="padding: 0.75rem; border: 1px solid #ddd; text-align: center;">65</td>
                            <td style="padding: 0.75rem; border: 1px solid #ddd; text-align: center;">136</td>
                            <td style="padding: 0.75rem; border: 1px solid #ddd; text-align: center;">63</td>
                            <td style="padding: 0.75rem; border: 1px solid #ddd; text-align: center;">300</td>
                            <td style="padding: 0.75rem; border: 1px solid #ddd; text-align: center;">76</td>
                        </tr>
                        <tr>
                            <td style="padding: 0.75rem; border: 1px solid #ddd; text-align: center;">3"</td>
                            <td style="padding: 0.75rem; border: 1px solid #ddd; text-align: center;">80</td>
                            <td style="padding: 0.75rem; border: 1px solid #ddd; text-align: center;">160</td>
                            <td style="padding: 0.75rem; border: 1px solid #ddd; text-align: center;">75</td>
                            <td style="padding: 0.75rem; border: 1px solid #ddd; text-align: center;">310</td>
                            <td style="padding: 0.75rem; border: 1px solid #ddd; text-align: center;">89</td>
                        </tr>
                    </tbody>
                </table>
            </div>

            <!-- Parts List -->
            <h3 style="color: var(--secondary-color); margin-bottom: 1rem;">Parts List & Materials</h3>
            <div style="overflow-x: auto;">
                <table style="width: 100%; border-collapse: collapse;">
                    <thead>
                        <tr style="background: var(--primary-color); color: white;">
                            <th style="padding: 1rem; border: 1px solid #ddd;">S.N.</th>
                            <th style="padding: 1rem; border: 1px solid #ddd;">Parts Name</th>
                            <th style="padding: 1rem; border: 1px solid #ddd;">Material</th>
                            <th style="padding: 1rem; border: 1px solid #ddd;">Qty</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr style="background: var(--lighter-gray);">
                            <td style="padding: 0.75rem; border: 1px solid #ddd; text-align: center;">01</td>
                            <td style="padding: 0.75rem; border: 1px solid #ddd;">Body</td>
                            <td style="padding: 0.75rem; border: 1px solid #ddd;">ASTM A 351 Gr. CF8/CF8M/CF3/CF3M</td>
                            <td style="padding: 0.75rem; border: 1px solid #ddd; text-align: center;">1</td>
                        </tr>
                        <tr>
                            <td style="padding: 0.75rem; border: 1px solid #ddd; text-align: center;">02</td>
                            <td style="padding: 0.75rem; border: 1px solid #ddd;">Body Connecter</td>
                            <td style="padding: 0.75rem; border: 1px solid #ddd;">ASTM A 351 Gr. CF8/CF8M/CF3/CF3M</td>
                            <td style="padding: 0.75rem; border: 1px solid #ddd; text-align: center;">2</td>
                        </tr>
                        <tr style="background: var(--lighter-gray);">
                            <td style="padding: 0.75rem; border: 1px solid #ddd; text-align: center;">03</td>
                            <td style="padding: 0.75rem; border: 1px solid #ddd;">Ball</td>
                            <td style="padding: 0.75rem; border: 1px solid #ddd;">AISI 304/316/304L/316L</td>
                            <td style="padding: 0.75rem; border: 1px solid #ddd; text-align: center;">1</td>
                        </tr>
                        <tr>
                            <td style="padding: 0.75rem; border: 1px solid #ddd; text-align: center;">04</td>
                            <td style="padding: 0.75rem; border: 1px solid #ddd;">Stem</td>
                            <td style="padding: 0.75rem; border: 1px solid #ddd;">AISI 304/316/304L/316L</td>
                            <td style="padding: 0.75rem; border: 1px solid #ddd; text-align: center;">1</td>
                        </tr>
                        <tr style="background: var(--lighter-gray);">
                            <td style="padding: 0.75rem; border: 1px solid #ddd; text-align: center;">05</td>
                            <td style="padding: 0.75rem; border: 1px solid #ddd;">Gland Nut</td>
                            <td style="padding: 0.75rem; border: 1px solid #ddd;">AISI 304/316/304L/316L</td>
                            <td style="padding: 0.75rem; border: 1px solid #ddd; text-align: center;">1</td>
                        </tr>
                        <tr>
                            <td style="padding: 0.75rem; border: 1px solid #ddd; text-align: center;">06</td>
                            <td style="padding: 0.75rem; border: 1px solid #ddd;">Gland Bush</td>
                            <td style="padding: 0.75rem; border: 1px solid #ddd;">AISI 202/304/316/304L/316L</td>
                            <td style="padding: 0.75rem; border: 1px solid #ddd; text-align: center;">1</td>
                        </tr>
                        <tr style="background: var(--lighter-gray);">
                            <td style="padding: 0.75rem; border: 1px solid #ddd; text-align: center;">07</td>
                            <td style="padding: 0.75rem; border: 1px solid #ddd;">Lock Nut</td>
                            <td style="padding: 0.75rem; border: 1px solid #ddd;">AISI 304/316/304L/316L</td>
                            <td style="padding: 0.75rem; border: 1px solid #ddd; text-align: center;">1</td>
                        </tr>
                        <tr>
                            <td style="padding: 0.75rem; border: 1px solid #ddd; text-align: center;">08</td>
                            <td style="padding: 0.75rem; border: 1px solid #ddd;">Seat Ring</td>
                            <td style="padding: 0.75rem; border: 1px solid #ddd;">PTFE/GFT</td>
                            <td style="padding: 0.75rem; border: 1px solid #ddd; text-align: center;">1</td>
                        </tr>
                        <tr style="background: var(--lighter-gray);">
                            <td style="padding: 0.75rem; border: 1px solid #ddd; text-align: center;">09</td>
                            <td style="padding: 0.75rem; border: 1px solid #ddd;">Stem Seal</td>
                            <td style="padding: 0.75rem; border: 1px solid #ddd;">PTFE/GFT</td>
                            <td style="padding: 0.75rem; border: 1px solid #ddd; text-align: center;">2</td>
                        </tr>
                        <tr>
                            <td style="padding: 0.75rem; border: 1px solid #ddd; text-align: center;">10</td>
                            <td style="padding: 0.75rem; border: 1px solid #ddd;">Body Sealant Ring</td>
                            <td style="padding: 0.75rem; border: 1px solid #ddd;">PTFE/GFT</td>
                            <td style="padding: 0.75rem; border: 1px solid #ddd; text-align: center;">2</td>
                        </tr>
                        <tr style="background: var(--lighter-gray);">
                            <td style="padding: 0.75rem; border: 1px solid #ddd; text-align: center;">11</td>
                            <td style="padding: 0.75rem; border: 1px solid #ddd;">Lever</td>
                            <td style="padding: 0.75rem; border: 1px solid #ddd;">M.S./S.S.-202/304/316</td>
                            <td style="padding: 0.75rem; border: 1px solid #ddd; text-align: center;">1</td>
                        </tr>
                        <tr>
                            <td style="padding: 0.75rem; border: 1px solid #ddd; text-align: center;">12</td>
                            <td style="padding: 0.75rem; border: 1px solid #ddd;">Nuts & Bolt</td>
                            <td style="padding: 0.75rem; border: 1px solid #ddd;">M.S./S.S.-202/304/316</td>
                            <td style="padding: 0.75rem; border: 1px solid #ddd; text-align: center;">-</td>
                        </tr>
                    </tbody>
                </table>
            </div>

            <div style="background: var(--lighter-gray); padding: 1.5rem; border-radius: 8px; margin-top: 2rem;">
                <h4 style="color: var(--primary-color); margin-bottom: 1rem;">Notes:</h4>
                <ul style="margin-left: 1.5rem; line-height: 1.8;">
                    <li>All dimensions are in mm</li>
                    <li>Tolerance ± 3 mm</li>
                    <li>Above 2" valves: Round body design</li>
                    <li>Below 2" valves: Square body design</li>
                    <li>65 mm and above: Lever material will be M.S.</li>
                </ul>
            </div>
        </section>

        <!-- Applications -->
        <section style="background: var(--lighter-gray); padding: 3rem; border-radius: 12px; margin-bottom: 4rem;">
            <h2 style="color: var(--primary-color); margin-bottom: 2rem; text-align: center;">Applications</h2>
            <div style="display: grid; grid-template-columns: repeat(5, 1fr); gap: 2rem; text-align: center;">
                <div>
                    <i class="fas fa-burn" style="font-size: 3rem; color: var(--accent-color); margin-bottom: 1rem;"></i>
                    <p style="font-weight: 600;">STEAM</p>
                </div>
                <div>
                    <i class="fas fa-tint" style="font-size: 3rem; color: var(--accent-color); margin-bottom: 1rem;"></i>
                    <p style="font-weight: 600;">WATER</p>
                </div>
                <div>
                    <i class="fas fa-oil-can" style="font-size: 3rem; color: var(--accent-color); margin-bottom: 1rem;"></i>
                    <p style="font-weight: 600;">OIL</p>
                </div>
                <div>
                    <i class="fas fa-wind" style="font-size: 3rem; color: var(--accent-color); margin-bottom: 1rem;"></i>
                    <p style="font-weight: 600;">AIR</p>
                </div>
                <div>
                    <i class="fas fa-cloud" style="font-size: 3rem; color: var(--accent-color); margin-bottom: 1rem;"></i>
                    <p style="font-weight: 600;">GASES</p>
                </div>
            </div>
        </section>'''
        
        content = content[:old_section.start()] + new_section + content[old_section.end():]
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✅ Updated: {filepath}")
    else:
        print(f"⚠️  Could not find section to replace in {filepath}")

# Run the update
update_ic_ball_valve_3pc_screw_end()
print("\n🎉 IC Ball Valve 3PC Screw End updated with technical specifications!")
print("\nThis is a template script. Due to the large amount of data,")
print("I'll create individual updates for each product page.")
