#!/usr/bin/env python3
"""
Generate country-specific landing pages for Supreme Valves India
"""

import json
import os

# Load countries data
with open('data/countries.json', 'r') as f:
    countries = json.load(f)

# Load products data
with open('data/products.json', 'r') as f:
    products_data = json.load(f)
    products = products_data['products']

# Group products by category
categories = {}
for product in products:
    category = product['category']
    if category not in categories:
        categories[category] = []
    categories[category].append(product)

# HTML template for country pages
def generate_country_page(country):
    country_name = country['name']
    country_id = country['id']
    cities = ', '.join(country['cities'])
    description = country['description']
    keywords = country['keywords']
    
    # Generate product sections by category
    product_sections = ""
    
    for category, category_products in categories.items():
        # Limit to 6 products per category for the country page
        featured_products = category_products[:6]
        
        product_cards = ""
        for product in featured_products:
            product_cards += f'''
            <div class="product-card-country">
                <a href="../products/{product['id']}.html">
                    <img src="../{product['image']}" alt="{product['name']}" loading="lazy">
                    <h4>{product['shortName']}</h4>
                </a>
            </div>'''
        
        product_sections += f'''
        <section class="country-product-section">
            <h2>{category} Manufacturer & Exporter in {country_name}</h2>
            <p>Supreme Valves India manufactures and exports high-quality {category.lower()} designed for safe, reliable, and long-lasting flow control across critical industries in {country_name} including oil & gas, chemical processing, water treatment, power generation, and pharmaceuticals. Our {category.lower()} meet international standards including API, ASME, BS, and ISO specifications.</p>
            <div class="country-products-grid">
                {product_cards}
            </div>
            <div class="view-all-link">
                <a href="../products.html" class="btn btn-secondary">View All {category} →</a>
            </div>
        </section>
        '''
    
    html_content = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Industrial Valve Manufacturer & Exporter in {country_name} | Supreme Valves India</title>
    <meta name="description" content="{description}">
    <meta name="keywords" content="{keywords}">
    <meta name="author" content="Supreme Valves India">
    <meta name="robots" content="index, follow">
    <link rel="canonical" href="https://www.supremevalves.in/countries/{country_id}.html">
    <link rel="icon" type="image/svg+xml" href="../assets/Supreme Valves.svg">
    
    <!-- Open Graph / Facebook -->
    <meta property="og:type" content="website">
    <meta property="og:url" content="https://www.supremevalves.in/countries/{country_id}.html">
    <meta property="og:title" content="Industrial Valve Manufacturer & Exporter in {country_name} | Supreme Valves India">
    <meta property="og:description" content="{description}">
    <meta property="og:image" content="https://www.supremevalves.in/assets/Valves%20and%20Projects/hero_image.jpeg">
    
    <!-- Fonts and Styles -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="../styles.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css">
    
    <style>
        .country-hero {{
            background: linear-gradient(135deg, var(--primary-color) 0%, var(--secondary-color) 100%);
            color: white;
            padding: 6rem 0 4rem 0;
            text-align: center;
        }}
        
        .country-hero h1 {{
            font-size: 2.5rem;
            margin-bottom: 1rem;
            font-weight: 800;
        }}
        
        .country-hero p {{
            font-size: 1.2rem;
            max-width: 800px;
            margin: 0 auto 2rem auto;
            line-height: 1.8;
        }}
        
        .country-cities {{
            background: rgba(255,255,255,0.1);
            padding: 1rem 2rem;
            border-radius: 50px;
            display: inline-block;
            margin-top: 1rem;
        }}
        
        .country-cities strong {{
            color: var(--accent-color);
        }}
        
        .country-product-section {{
            padding: 4rem 0;
            border-bottom: 1px solid #e0e0e0;
        }}
        
        .country-product-section:last-child {{
            border-bottom: none;
        }}
        
        .country-product-section h2 {{
            font-size: 2rem;
            color: var(--primary-color);
            margin-bottom: 1rem;
            font-weight: 700;
        }}
        
        .country-product-section > p {{
            font-size: 1.1rem;
            line-height: 1.8;
            color: var(--text-color);
            margin-bottom: 2rem;
            max-width: 900px;
        }}
        
        .country-products-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(180px, 1fr));
            gap: 2rem;
            margin: 2rem 0;
        }}
        
        .product-card-country {{
            background: white;
            border-radius: 12px;
            padding: 1.5rem;
            text-align: center;
            transition: all 0.3s ease;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        }}
        
        .product-card-country:hover {{
            transform: translateY(-5px);
            box-shadow: 0 8px 20px rgba(0,0,0,0.15);
        }}
        
        .product-card-country img {{
            width: 100%;
            height: 150px;
            object-fit: cover;
            border-radius: 8px;
            margin-bottom: 1rem;
        }}
        
        .product-card-country h4 {{
            font-size: 0.95rem;
            color: var(--primary-color);
            font-weight: 600;
            line-height: 1.4;
        }}
        
        .product-card-country a {{
            text-decoration: none;
            color: inherit;
        }}
        
        .view-all-link {{
            text-align: center;
            margin-top: 2rem;
        }}
        
        .country-cta {{
            background: linear-gradient(135deg, var(--accent-color) 0%, #ff6b35 100%);
            color: white;
            padding: 4rem 0;
            text-align: center;
            margin-top: 4rem;
        }}
        
        .country-cta h2 {{
            font-size: 2rem;
            margin-bottom: 1rem;
        }}
        
        .country-cta p {{
            font-size: 1.2rem;
            margin-bottom: 2rem;
        }}
    </style>
</head>
<body>
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
                        <div class="dropdown-content" id="products-dropdown">
                            <!-- Products will be dynamically loaded here -->
                        </div>
                    </li>
                    <li><a href="../industries.html">Industries</a></li>
                    <li><a href="../projects.html">Projects</a></li>
                    <li><a href="../resources.html">Resources</a></li>
                    <li><a href="../faqs.html">FAQs</a></li>
                    <li><a href="../contact.html">Contact Us</a></li>
                </ul>
            </nav>
        </div>
    </header>

    <main>
        <section class="country-hero">
            <div class="container">
                <h1>Industrial Valve Manufacturer & Exporter in {country_name}</h1>
                <p>{description}</p>
                <div class="country-cities">
                    <strong>Serving:</strong> {cities}
                </div>
            </div>
        </section>

        <div class="container">
            {product_sections}
        </div>
        
        <section class="country-cta">
            <div class="container">
                <h2>Ready to Source Quality Valves for {country_name}?</h2>
                <p>Contact Supreme Valves India for expert consultation and competitive quotes</p>
                <a href="../contact.html" class="btn btn-primary" style="background: white; color: var(--accent-color);">Get a Quote →</a>
            </div>
        </section>
    </main>

    <footer class="footer-new">
        <div class="container">
            <div class="footer-grid">
                <div class="footer-col footer-products-col">
                    <h4>Product Range</h4>
                    <ul id="footer-products-list" class="footer-products-multicolumn">
                        <!-- Products will be dynamically loaded here -->
                    </ul>
                </div>
                <div class="footer-col">
                    <h4>Quick Links</h4>
                    <ul>
                        <li><a href="../index.html">Home</a></li>
                        <li><a href="../about.html">About Us</a></li>
                        <li><a href="../products.html">Products</a></li>
                        <li><a href="../industries.html">Industries</a></li>
                        <li><a href="../projects.html">Projects</a></li>
                        <li><a href="../resources.html">Resources</a></li>
                        <li><a href="../contact.html">Contact Us</a></li>
                    </ul>
                </div>
            </div>
            
            <!-- Company Details Section -->
            <div class="footer-company-details">
                <div class="company-info-grid">
                    <div class="company-info-item">
                        <i class="fas fa-map-marker-alt"></i>
                        <div>
                            <h5>India Office</h5>
                            <p>Ranginwala Building, Relief Road<br>Ahmedabad - 380001, Gujarat, India</p>
                        </div>
                    </div>
                    <div class="company-info-item">
                        <i class="fas fa-globe"></i>
                        <div>
                            <h5>International Offices</h5>
                            <p>Singapore: sg@supremevalves.in<br>
                            Sydney, Australia: aus@supremevalves.in<br>
                            Mississauga, Canada: ca@supremevalves.in</p>
                        </div>
                    </div>
                </div>
            </div>
            
            <div class="footer-socials">
                <a href="https://www.facebook.com/p/Supreme-Enterprise-61566023002189/" target="_blank" aria-label="Facebook"><i class="fab fa-facebook-f"></i></a>
                <a href="https://www.instagram.com/supremevalvesindia/" target="_blank" aria-label="Instagram"><i class="fab fa-instagram"></i></a>
                <a href="https://www.linkedin.com/company/supreme-valves-india/posts/?feedView=all" target="_blank" aria-label="LinkedIn"><i class="fab fa-linkedin-in"></i></a>
                <a href="https://x.com/SupremeValves" target="_blank" aria-label="Twitter/X"><i class="fab fa-x-twitter"></i></a>
                <a href="https://www.youtube.com/@SupremeValves" target="_blank" aria-label="YouTube"><i class="fab fa-youtube"></i></a>
            </div>
            
            <div class="copyright">
                &copy; 2025 Supreme Valves India. All Rights Reserved.
            </div>
        </div>
    </footer>
    <script src="https://kit.fontawesome.com/a076d05399.js" crossorigin="anonymous"></script>
    <script src="../js/products.js"></script>
</body>
</html>'''
    
    return html_content

# Generate pages for all countries
os.makedirs('countries', exist_ok=True)

for country in countries:
    html_content = generate_country_page(country)
    filename = f"countries/{country['id']}.html"
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print(f"✅ Created: {filename}")

print(f"\n🎉 Generated {len(countries)} country pages!")
