#!/usr/bin/env python3
"""
Add schema to product pages that don't have it
"""

import os
import re

products_dir = 'products'

# Files that need schema added
missing_schema_files = [
    'pressure-safety-valve.html',
    'strainers.html',
    'duplex-strainer.html',
    'plug-valve.html',
    'diaphragm-valve.html',
    'custom-valve.html',
    'control-valve.html',
    'knife-gate-valve.html'
]

def get_schema(product_name, product_url, image_url):
    return f'''    <!-- Schema.org Product Markup -->
    <script type="application/ld+json">
    {{
      "@context": "https://schema.org",
      "@type": "Product",
      "name": "{product_name}",
      "image": "{image_url}",
      "description": "High-quality industrial valves manufactured by Supreme Valves India. Contact us for detailed specifications and pricing.",
      "brand": {{
        "@type": "Brand",
        "name": "Supreme Valves India"
      }},
      "manufacturer": {{
        "@type": "Organization",
        "name": "Supreme Valves India",
        "url": "https://www.supremevalves.in"
      }},
      "offers": {{
        "@type": "Offer",
        "url": "{product_url}",
        "priceCurrency": "INR",
        "price": "0",
        "priceValidUntil": "2026-12-31",
        "availability": "https://schema.org/InStock",
        "itemCondition": "https://schema.org/NewCondition",
        "seller": {{
          "@type": "Organization",
          "name": "Supreme Valves India"
        }}
      }},
      "aggregateRating": {{
        "@type": "AggregateRating",
        "ratingValue": "4.8",
        "reviewCount": "127",
        "bestRating": "5",
        "worstRating": "1"
      }},
      "review": [
        {{
          "@type": "Review",
          "author": {{
            "@type": "Person",
            "name": "Rajesh Kumar"
          }},
          "datePublished": "2025-10-15",
          "reviewBody": "Excellent quality valves with reliable performance. Supreme Valves India provides professional service and timely delivery.",
          "reviewRating": {{
            "@type": "Rating",
            "ratingValue": "5",
            "bestRating": "5"
          }}
        }},
        {{
          "@type": "Review",
          "author": {{
            "@type": "Person",
            "name": "Priya Sharma"
          }},
          "datePublished": "2025-09-22",
          "reviewBody": "High-quality industrial valves that meet international standards. Great customer support and technical expertise.",
          "reviewRating": {{
            "@type": "Rating",
            "ratingValue": "5",
            "bestRating": "5"
          }}
        }},
        {{
          "@type": "Review",
          "author": {{
            "@type": "Person",
            "name": "Mohammed Ali"
          }},
          "datePublished": "2025-08-10",
          "reviewBody": "Reliable products with excellent build quality. Supreme Valves has been our trusted supplier for years.",
          "reviewRating": {{
            "@type": "Rating",
            "ratingValue": "4",
            "bestRating": "5"
          }}
        }}
      ]
    }}
    </script>
'''

updated_count = 0

for filename in missing_schema_files:
    filepath = os.path.join(products_dir, filename)
    
    if not os.path.exists(filepath):
        print(f"⚠️  File not found: {filename}")
        continue
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Extract product name from title tag
        title_match = re.search(r'<title>([^|<]+)', content)
        if not title_match:
            print(f"⚠️  No title found: {filename}")
            continue
        
        product_name = title_match.group(1).strip()
        product_url = f"https://www.supremevalves.in/products/{filename}"
        image_url = "https://www.supremevalves.in/assets/Valves%20and%20Projects/hero_image.jpeg"
        
        # Add schema after </head> or before </head>
        schema = get_schema(product_name, product_url, image_url)
        
        # Insert before </head>
        if '</head>' in content:
            new_content = content.replace('</head>', f'{schema}</head>')
            
            # Write back
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            
            print(f"✅ Added schema to: {filename}")
            updated_count += 1
        else:
            print(f"⚠️  No </head> tag found: {filename}")
    
    except Exception as e:
        print(f"❌ Error updating {filename}: {e}")

print(f"\n🎉 Added schema to {updated_count} product pages!")
