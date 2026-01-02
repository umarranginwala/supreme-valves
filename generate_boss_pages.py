import json
import os
import re

def create_boss_html_pages():
    with open('boss_products.json', 'r') as f:
        boss_products = json.load(f)
    
    os.makedirs('products', exist_ok=True)
    
    for bp in boss_products:
        product_id = bp['id']
        product_name = bp['name']
        description = bp['description']
        
        # Format Testing
        testing_rows = ""
        for test in bp.get('testing', []):
            testing_rows += f"""
                        <tr style="border-bottom: 1px solid var(--border-color);">
                            <td style="padding: 1rem 1.5rem; font-weight: 600; background: var(--lighter-gray);">{test}</td>
                            <td style="padding: 1rem 1.5rem;">Verified as per BOSS Standards</td>
                        </tr>"""
        
        # Format Materials
        materials_list = ""
        for mat in bp.get('materials', []):
            materials_list += f"<li>{mat}</li>"
            
        # Format Dimensions
        dimension_rows = ""
        for dim in bp.get('dimensions', []):
            dimension_rows += f"<li>{dim}</li>"

        html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{product_name} | BOSS Industrial Valves | Supreme Valves India</title>
    <meta name="description" content="{description}">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="../styles.css">
    <link rel="stylesheet" href="../css/product-search.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css">
</head>
<body data-product-id="{product_id}">
    
    <header>
        <div class="container">
            <div class="logo">
                <a href="../index.html"><img src="../assets/Supreme Valves.svg" alt="Supreme Valves India Logo"></a>
            </div>
            <nav>
                <ul>
                    <li><a href="../index.html">Home</a></li>
                    <li><a href="../about.html">About Us</a></li>
                    <li class="dropdown">
                        <a href="../products.html" class="dropbtn">Products <i class="fas fa-chevron-down"></i></a>
                        <div class="dropdown-content" id="products-dropdown"></div>
                    </li>
                    <li><a href="../industries.html">Industries</a></li>
                    <li><a href="../projects.html">Projects</a></li>
                    <li><a href="../contact.html">Contact Us</a></li>
                </ul>
            </nav>
        </div>
    </header>

    <main class="container" style="padding-top: 3rem;">
        
        <nav style="font-size: 0.9rem; color: var(--text-light); margin-bottom: 2rem;">
            <a href="../index.html" style="color: var(--accent-color);">Home</a> / 
            <a href="../products.html" style="color: var(--accent-color);">Products</a> / 
            <span>{product_name}</span>
        </nav>

        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 3rem; margin-bottom: 4rem;">
            <div>
                <img src="../assets/Valves and Projects/hero_image.jpeg" alt="{product_name}" style="width: 100%; border-radius: 12px; box-shadow: var(--shadow-lg);">
            </div>
            <div>
                <span style="display: inline-block; padding: 0.5rem 1rem; background: var(--lighter-gray); color: var(--accent-color); border-radius: 6px; font-size: 0.85rem; font-weight: 600; margin-bottom: 1rem;">BOSS Industrial Valves</span>
                <h1 style="font-size: 2.5rem; color: var(--primary-color); margin-bottom: 1rem;">{product_name}</h1>
                <p style="font-size: 1.15rem; line-height: 1.8; color: var(--text-color); margin-bottom: 2rem;">{description}</p>
                
                <div style="background: var(--lighter-gray); padding: 1.5rem; border-radius: 12px; margin-bottom: 2rem;">
                    <h3 style="font-size: 1.1rem; color: var(--primary-color); margin-bottom: 1rem;">Suitability</h3>
                    <p>{bp.get('suitability', 'General Industrial Applications')}</p>
                </div>

                <div style="display: flex; gap: 1rem;">
                    <a href="../contact.html" class="btn btn-primary">Request Quote</a>
                    <a href="https://api.whatsapp.com/send/?phone=919773278770&text=Inquiry%20about%20{product_name.replace(' ', '%20')}" target="_blank" class="btn btn-secondary">
                        <i class="fab fa-whatsapp"></i> WhatsApp Inquiry
                    </a>
                </div>
            </div>
        </div>

        <section style="margin-bottom: 4rem;">
            <h2 class="section-title">Technical Specifications & Testing</h2>
            <div style="background: var(--white-color); border: 1px solid var(--border-color); border-radius: 12px; overflow: hidden;">
                <table style="width: 100%; border-collapse: collapse;">
                    <tbody>
                        {testing_rows}
                    </tbody>
                </table>
            </div>
        </section>

        <section style="margin-bottom: 4rem;">
            <h2 class="section-title">Materials of Construction (MOC)</h2>
            <div style="background: var(--lighter-gray); padding: 2rem; border-radius: 12px;">
                <ul style="column-count: 2; list-style-type: disc; padding-left: 1.5rem;">
                    {materials_list}
                </ul>
            </div>
        </section>

        <section style="margin-bottom: 4rem;">
            <h2 class="section-title">Dimensions & Sizes</h2>
            <div style="background: var(--lighter-gray); padding: 2rem; border-radius: 12px;">
                <ul style="list-style-type: none; padding: 0;">
                    {dimension_rows}
                </ul>
            </div>
        </section>

        <section style="margin-bottom: 4rem;">
            <h2 class="section-title">Request Detailed Quotation</h2>
            <div style="background: var(--lighter-gray); padding: 3rem; border-radius: 12px; max-width: 800px; margin: 0 auto;">
                <form action="../contact.html" method="get" style="display: grid; gap: 1.5rem;">
                    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1.5rem;">
                        <div>
                            <label style="display: block; margin-bottom: 0.5rem; font-weight: 600;">Name *</label>
                            <input type="text" name="name" required style="width: 100%; padding: 0.75rem; border: 1px solid var(--border-color); border-radius: 6px;">
                        </div>
                        <div>
                            <label style="display: block; margin-bottom: 0.5rem; font-weight: 600;">Email *</label>
                            <input type="email" name="email" required style="width: 100%; padding: 0.75rem; border: 1px solid var(--border-color); border-radius: 6px;">
                        </div>
                    </div>
                    <div>
                        <label style="display: block; margin-bottom: 0.5rem; font-weight: 600;">Message *</label>
                        <textarea name="message" required rows="5" style="width: 100%; padding: 0.75rem; border: 1px solid var(--border-color); border-radius: 6px; resize: vertical;">I am interested in {product_name}. Please provide a quote.</textarea>
                    </div>
                    <button type="submit" class="btn btn-primary">Submit Inquiry</button>
                </form>
            </div>
        </section>

    </main>

    <footer class="footer-new">
        <div class="container">
            <div class="footer-grid">
                <div class="footer-col footer-products-col">
                    <h4>Product Range</h4>
                    <ul id="footer-products-list" class="footer-products-multicolumn"></ul>
                </div>
                <div class="footer-col">
                    <h4>Quick Links</h4>
                    <ul>
                        <li><a href="../index.html">Home</a></li>
                        <li><a href="../about.html">About Us</a></li>
                        <li><a href="../products.html">Products</a></li>
                        <li><a href="../contact.html">Contact Us</a></li>
                    </ul>
                </div>
            </div>
            <div class="footer-bottom">
                <p>&copy; 2025 Supreme Valves India. All Rights Reserved.</p>
            </div>
        </div>
    </footer>

    <script src="../js/products-data.js"></script>
    <script src="../js/product-search.js"></script>
    <script src="../js/products.js"></script>
    <script src="../js/navigation.js"></script>
</body>
</html>"""
        
        file_path = f"products/{product_id}.html"
        with open(file_path, 'w') as f_out:
            f_out.write(html_content)
    
    print(f"Generated {len(boss_products)} HTML pages in products/ directory")

if __name__ == "__main__":
    create_boss_html_pages()
