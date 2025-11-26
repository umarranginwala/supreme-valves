# Supreme Valves - Modular Architecture Documentation

## Overview
This document describes the modular, optimized architecture implemented for the Supreme Valves website.

## Architecture Principles

### 1. **Separation of Concerns**
- Components are separated into logical modules
- Each module has a single responsibility
- Clear interfaces between modules

### 2. **DRY (Don't Repeat Yourself)**
- Reusable components for header, footer, navigation
- Centralized configuration
- Shared utility functions

### 3. **Performance First**
- Lazy loading for images and components
- Caching strategies (sessionStorage, localStorage)
- Code splitting and async loading
- Resource hints and prefetching

### 4. **Maintainability**
- Clear file structure
- Comprehensive documentation
- Consistent naming conventions
- Modular code that's easy to update

---

## File Structure

```
supremevalves_site_v3/
├── js/
│   ├── components.js          # Reusable UI components (header, footer, widgets)
│   ├── products-optimized.js  # Product management with caching
│   ├── utils.js               # Utility functions
│   ├── forms.js               # Form validation and handling
│   ├── performance.js         # Performance optimizations
│   └── products.js            # Legacy (to be replaced)
├── data/
│   ├── config.json            # Centralized configuration
│   └── products.json          # Product data
├── assets/
│   └── ...
└── products/
    └── *.html                 # Product pages
```

---

## Module Documentation

### 1. Components Module (`js/components.js`)

**Purpose:** Manage reusable UI components

**Key Features:**
- Dynamic header rendering with active page detection
- Dynamic footer with company info and social links
- WhatsApp widget with product-specific messages
- Automatic path resolution for subdirectories

**Usage:**
```javascript
// Initialize all components
await componentLoader.init({
    activePage: 'products',
    productName: 'Gate Valve'
});

// Or initialize individually
await componentLoader.renderHeader('home');
await componentLoader.renderFooter();
await componentLoader.renderWhatsAppWidget('Ball Valve');
```

**Configuration:**
Components read from `data/config.json` for:
- Navigation items
- Quick links
- Social media links
- Company information

---

### 2. Products Module (`js/products-optimized.js`)

**Purpose:** Manage product data with performance optimization

**Key Features:**
- Lazy loading with IntersectionObserver
- SessionStorage caching
- Category filtering
- Automatic dropdown and footer population

**Usage:**
```javascript
// Load products (cached automatically)
await productManager.loadProducts();

// Get products
const all = productManager.getAllProducts();
const featured = productManager.getFeaturedProducts(6);
const byCategory = productManager.getProductsByCategory('Control Valves');

// Render products with lazy loading
productManager.renderProducts('container-id', products, { lazyLoad: true });

// Auto-initialize
productManager.init();
```

**Caching Strategy:**
- First load: Fetch from API
- Subsequent loads: Use sessionStorage cache
- Cache invalidation: On page refresh or manual clear

---

### 3. Utils Module (`js/utils.js`)

**Purpose:** Provide reusable utility functions

**Available Functions:**

**Performance:**
- `debounce(func, wait)` - Debounce function calls
- `throttle(func, limit)` - Throttle function calls

**Validation:**
- `isValidEmail(email)` - Email validation
- `isValidPhone(phone)` - Phone validation

**UI:**
- `showNotification(message, type, duration)` - Show toast notifications
- `smoothScrollTo(elementId)` - Smooth scroll to element
- `copyToClipboard(text)` - Copy text to clipboard

**Storage:**
- `storage.set(key, value, expiryMinutes)` - Set with expiry
- `storage.get(key)` - Get with expiry check
- `storage.remove(key)` - Remove item

**Device:**
- `getDeviceType()` - Get device type (mobile/tablet/desktop)
- `isInViewport(element)` - Check if element is visible

**Usage:**
```javascript
// Debounce search input
const search = Utils.debounce((query) => {
    // Search logic
}, 300);

// Show notification
Utils.showNotification('Success!', 'success', 3000);

// Storage with expiry
Utils.storage.set('user_prefs', data, 60); // 60 minutes
const prefs = Utils.storage.get('user_prefs');
```

---

### 4. Forms Module (`js/forms.js`)

**Purpose:** Handle form validation and submission

**Key Features:**
- Real-time validation
- Custom validation rules
- Error message display
- AJAX submission support
- Loading states

**Usage:**
```javascript
// Initialize form with validation
formHandler.initForm('quote-form', {
    validation: {
        name: { required: true, minLength: 2 },
        email: { required: true, email: true },
        phone: { phone: true },
        message: { required: true, minLength: 10 }
    },
    onSubmit: async (data) => {
        // Custom submit logic
        console.log('Form data:', data);
    }
});

// Validate programmatically
const isValid = formHandler.validateForm('quote-form');
```

**Validation Rules:**
- `required` - Field must not be empty
- `email` - Valid email format
- `phone` - Valid phone format
- `minLength` - Minimum character length
- `maxLength` - Maximum character length

---

### 5. Performance Module (`js/performance.js`)

**Purpose:** Optimize page load and runtime performance

**Key Features:**
- Resource preloading
- Image lazy loading
- Service Worker setup
- Performance monitoring
- DNS prefetching
- Font optimization

**Automatic Optimizations:**
- Lazy loads all images
- Preloads critical resources
- Monitors Core Web Vitals (LCP, FID, CLS)
- Caches API responses
- Defers non-critical JavaScript

**Usage:**
```javascript
// Auto-initializes on page load
// Manual initialization if needed:
Performance.init();

// Prefetch next page
Performance.prefetchPage('/products/ball-valve.html');

// Cache API response
Performance.cacheAPIResponse('products', data, 60);
const cached = Performance.getCachedAPIResponse('products');
```

**Performance Metrics Logged:**
- Page Load Time
- Connect Time
- Render Time
- Largest Contentful Paint (LCP)
- First Input Delay (FID)
- Cumulative Layout Shift (CLS)

---

## Configuration (`data/config.json`)

**Purpose:** Centralized configuration for site-wide settings

**Structure:**
```json
{
  "company": {
    "name": "Supreme Valves India",
    "whatsapp": "919773278770",
    "address": { ... }
  },
  "navigation": [ ... ],
  "quickLinks": [ ... ],
  "socialMedia": [ ... ]
}
```

**Benefits:**
- Single source of truth
- Easy updates (change once, apply everywhere)
- No hardcoded values in components
- Version control friendly

---

## Implementation Guide

### For New Pages

1. **Add data-page attribute to body:**
```html
<body data-page="products" data-product="Gate Valve">
```

2. **Include required scripts:**
```html
<script src="js/utils.js"></script>
<script src="js/components.js"></script>
<script src="js/products-optimized.js"></script>
<script src="js/forms.js"></script>
<script src="js/performance.js"></script>
```

3. **Components auto-initialize:**
- Header, footer, and WhatsApp widget render automatically
- Products load and populate dropdowns automatically
- Forms validate automatically

### For Product Pages

1. **Use lazy loading for images:**
```html
<img data-src="image.jpg" alt="Product" class="lazy-load">
```

2. **Initialize product-specific features:**
```javascript
document.addEventListener('DOMContentLoaded', async () => {
    await productManager.loadProducts();
    // Custom logic here
});
```

### For Forms

1. **Add form ID:**
```html
<form id="quote-form" action="contact.html">
```

2. **Form auto-validates** based on field names and types

---

## Performance Optimizations

### 1. **Caching Strategy**
- **SessionStorage:** Products, config (session-based)
- **LocalStorage:** User preferences (with expiry)
- **Service Worker:** Offline support (future)

### 2. **Lazy Loading**
- Images load only when visible
- IntersectionObserver for modern browsers
- Fallback for older browsers

### 3. **Code Splitting**
- Separate modules for different features
- Load only what's needed
- Async/defer for non-critical scripts

### 4. **Resource Hints**
- DNS prefetch for external domains
- Preload for critical resources
- Prefetch for next pages

---

## Migration Path

### Phase 1: ✅ Complete
- Created modular components
- Implemented caching
- Added performance monitoring
- Created utility functions

### Phase 2: In Progress
- Replace old products.js with products-optimized.js
- Update all pages to use component system
- Implement service worker

### Phase 3: Future
- Add build process (webpack/rollup)
- Minify and bundle JavaScript
- Implement CSS modules
- Add automated testing

---

## Best Practices

### 1. **Always Use Components**
```javascript
// ✅ Good
await componentLoader.renderHeader('products');

// ❌ Bad
// Hardcoding header HTML in every page
```

### 2. **Cache API Calls**
```javascript
// ✅ Good
await productManager.loadProducts(); // Uses cache

// ❌ Bad
fetch('data/products.json'); // No caching
```

### 3. **Use Utility Functions**
```javascript
// ✅ Good
Utils.showNotification('Success!', 'success');

// ❌ Bad
alert('Success!'); // Poor UX
```

### 4. **Validate Forms**
```javascript
// ✅ Good
formHandler.initForm('my-form', { validation: {...} });

// ❌ Bad
// Manual validation in every form
```

---

## Troubleshooting

### Components Not Loading
1. Check console for errors
2. Verify `data/config.json` exists
3. Ensure correct path resolution

### Images Not Lazy Loading
1. Check if IntersectionObserver is supported
2. Verify `data-src` attribute is set
3. Check console for observer errors

### Forms Not Validating
1. Ensure form has an ID
2. Check validation rules are correct
3. Verify field names match validation config

### Cache Issues
1. Clear sessionStorage: `sessionStorage.clear()`
2. Hard refresh: Ctrl+Shift+R (Cmd+Shift+R on Mac)
3. Check cache expiry times

---

## Performance Metrics

### Target Metrics
- **Page Load Time:** < 3 seconds
- **First Contentful Paint:** < 1.5 seconds
- **Largest Contentful Paint:** < 2.5 seconds
- **First Input Delay:** < 100ms
- **Cumulative Layout Shift:** < 0.1

### Monitoring
- Check browser console for performance logs
- Use Lighthouse for audits
- Monitor Core Web Vitals in Search Console

---

## Future Enhancements

1. **Build System**
   - Webpack/Rollup for bundling
   - Minification and tree-shaking
   - Source maps for debugging

2. **Testing**
   - Unit tests for modules
   - Integration tests for components
   - E2E tests for critical flows

3. **Advanced Features**
   - Progressive Web App (PWA)
   - Offline support
   - Push notifications
   - Advanced analytics

4. **Developer Experience**
   - Hot module replacement
   - TypeScript for type safety
   - ESLint for code quality
   - Prettier for formatting

---

## Support

For questions or issues with the modular architecture:
1. Check this documentation
2. Review module source code (well-commented)
3. Check browser console for errors
4. Test in incognito mode to rule out cache issues

---

**Last Updated:** November 26, 2025
**Version:** 1.0.0
**Maintained by:** Supreme Valves Development Team
