# Google Merchant Center Setup Guide for Supreme Valves India

## Overview
This guide will help you get your products listed on Google Shopping tab to drive more traffic to your website.

## Prerequisites
- Google Search Console account (already set up)
- Google Merchant Center account (free)
- Product feed XML file (already created: `product-feed.xml`)

---

## Step 1: Create Google Merchant Center Account

1. Go to [Google Merchant Center](https://merchants.google.com/)
2. Sign in with the same Google account used for Search Console
3. Click **Get Started** and follow the setup wizard
4. Enter your business information:
   - Business name: **Supreme Valves India**
   - Country: **India**
   - Time zone: **Asia/Kolkata (IST)**

---

## Step 2: Verify and Claim Your Website

1. In Merchant Center, go to **Tools & Settings** → **Business Information**
2. Click **Website** tab
3. Enter your website URL: `https://www.supremevalves.in`
4. Choose verification method: **Google Search Console** (recommended)
5. Since you already have Search Console set up, it will automatically verify
6. Click **Claim URL** to claim ownership

---

## Step 3: Set Up Product Feed

### Option A: Upload Product Feed XML (Recommended for Start)

1. In Merchant Center, go to **Products** → **Feeds**
2. Click the **+** button to create a new feed
3. Select:
   - **Country of sale**: India
   - **Language**: English
   - **Destinations**: Surfaces across Google (includes Shopping tab)
   - **Feed name**: Supreme Valves Product Feed
4. Choose **Upload** as input method
5. Select **Scheduled fetch** and enter:
   ```
   https://www.supremevalves.in/product-feed.xml
   ```
6. Set fetch frequency: **Daily** (recommended)
7. Click **Create Feed**

### Option B: Google Sheets (Alternative)

1. Create a Google Sheet with product data
2. Link it to Merchant Center
3. Auto-sync enabled

---

## Step 4: Configure Shipping Settings

1. Go to **Tools & Settings** → **Shipping and Returns**
2. Click **Add Shipping Service**
3. Configure:
   - **Service name**: Standard Shipping
   - **Delivery time**: 5-7 business days (adjust as needed)
   - **Shipping cost**: Free or specify rates
4. Add shipping zones (India, International)
5. Save settings

---

## Step 5: Configure Tax Settings (if applicable)

1. Go to **Tools & Settings** → **Tax**
2. For India: GST is typically included in product prices
3. Select **Tax included in price** if applicable
4. Save settings

---

## Step 6: Link Search Console to Merchant Center

1. In Merchant Center, go to **Tools & Settings** → **Linked Accounts**
2. Find **Google Search Console**
3. Click **Link** next to your verified property
4. This enables the Shopping tab feature

---

## Step 7: Review and Fix Product Issues

1. Go to **Products** → **Diagnostics**
2. Review any errors or warnings:
   - **Missing required attributes** (price, availability, image)
   - **Image quality issues**
   - **Invalid URLs**
3. Fix issues in your product feed XML
4. Re-upload or wait for next scheduled fetch

---

## Step 8: Enable Free Product Listings

1. Go to **Growth** → **Manage Programs**
2. Find **Surfaces across Google** (Free listings)
3. Click **Get Started** or **Enable**
4. Accept terms and conditions
5. Your products will now appear on:
   - Google Shopping tab
   - Google Search results
   - Google Images
   - Google Lens

---

## Product Feed Requirements

Your `product-feed.xml` already includes these required fields:

### Required Fields
- ✅ `id` - Unique product identifier
- ✅ `title` - Product name (150 characters max)
- ✅ `description` - Product description (5000 characters max)
- ✅ `link` - Product page URL
- ✅ `image_link` - Main product image URL
- ✅ `price` - Product price with currency
- ✅ `availability` - in stock / out of stock / preorder
- ✅ `condition` - new / refurbished / used
- ✅ `brand` - Supreme Valves India

### Recommended Fields (Already Included)
- ✅ `product_type` - Product category hierarchy
- ✅ `google_product_category` - Google's product taxonomy (632 = Hardware)
- ✅ `mpn` - Manufacturer Part Number
- ✅ `material` - Product material
- ✅ `custom_labels` - For filtering and reporting

---

## Image Requirements

Ensure all product images meet these requirements:
- **Format**: JPEG, PNG, GIF, BMP, TIFF, WebP
- **Size**: Minimum 100x100 pixels, recommended 800x800 pixels or larger
- **Quality**: High resolution, clear product view
- **Background**: White or neutral background preferred
- **URL**: Must be crawlable (not blocked by robots.txt)
- **HTTPS**: Secure URLs required

### Current Images to Upload
Make sure these images are accessible:
- ✅ `vertical_nrv_ss_304.jpeg`
- ✅ `horizontal_nrv_ss_304.jpeg`
- ✅ `YSTRAINER_Brass.jpg`
- ✅ `YSTRAINER_Brass_Technical_drawing.jpg`

---

## Monitoring and Optimization

### Daily Tasks
1. Check **Products** → **Diagnostics** for errors
2. Monitor **Performance** dashboard for impressions and clicks
3. Review disapproved products and fix issues

### Weekly Tasks
1. Add new products to feed
2. Update prices and availability
3. Review product performance metrics
4. Optimize titles and descriptions based on search terms

### Monthly Tasks
1. Analyze top-performing products
2. Add more product images
3. Expand product catalog
4. Review and update shipping/tax settings

---

## Troubleshooting Common Issues

### Products Not Showing
- ✅ Verify feed is approved in Diagnostics
- ✅ Check that all required fields are present
- ✅ Ensure images are accessible (not 404)
- ✅ Wait 24-48 hours after feed approval

### Image Issues
- ✅ Use high-quality images (800x800px minimum)
- ✅ Ensure HTTPS URLs
- ✅ Check image file size (max 16MB)
- ✅ Verify images load correctly in browser

### Price/Availability Issues
- ✅ Match prices on website and feed
- ✅ Use correct currency code (INR)
- ✅ Update availability status regularly
- ✅ Include tax in price if applicable

---

## Feed Update Process

When you add new products:

1. **Update product-feed.xml** with new product entries
2. **Commit and push** to GitHub (auto-deploys to website)
3. **Wait for scheduled fetch** (daily) or manually fetch in Merchant Center
4. **Check Diagnostics** for any errors
5. **Monitor Performance** after 24-48 hours

---

## Additional Resources

- [Google Merchant Center Help](https://support.google.com/merchants/)
- [Product Data Specification](https://support.google.com/merchants/answer/7052112)
- [Free Product Listings Guide](https://support.google.com/merchants/answer/9199328)
- [Image Requirements](https://support.google.com/merchants/answer/6324350)

---

## Support

For technical issues with the feed or website:
- Check Search Console for crawl errors
- Verify product URLs are accessible
- Ensure robots.txt allows Googlebot

For Merchant Center account issues:
- Contact Google Merchant Center Support
- Check Merchant Center Help Center
- Review policy compliance

---

## Current Feed URL

Your product feed is accessible at:
```
https://www.supremevalves.in/product-feed.xml
```

This feed currently includes:
- NAB Ball Valve Screwed End Full Port
- NRV Horizontal & Vertical Type
- Brass Y-Type Strainer BSP
- Gate Valve
- Globe Valve
- Ball Valve
- Check Valve
- Butterfly Valve
- Safety Relief Valve
- Control Valve
- Knife Gate Valve

**Total Products in Feed**: 11 (expandable to all 100+ products)

---

## Next Steps

1. ✅ Product feed XML created
2. ✅ Sitemap updated with new products
3. ⏳ Create Google Merchant Center account
4. ⏳ Link Search Console to Merchant Center
5. ⏳ Upload product feed
6. ⏳ Configure shipping and tax
7. ⏳ Enable free product listings
8. ⏳ Monitor and optimize

---

**Last Updated**: December 31, 2025
**Contact**: Supreme Valves India - info@supremevalves.in
