/**
 * Supreme Valves India - Global Form Handler
 * Handles AJAX form submissions and redirects to thank-you page
 * Required for Google Customer Reviews integration
 */

document.addEventListener('DOMContentLoaded', function() {
    // Find all inquiry forms on the page
    const forms = document.querySelectorAll('form');
    
    /**
     * Get base path based on current location
     */
    function getBasePath() {
        const path = window.location.pathname;
        if (path.includes('/products/') || path.includes('/faqs/') || path.includes('/blog/') || path.includes('/countries/') || path.includes('/projects/')) {
            return '../';
        } else if (path.includes('/docs/')) {
            return '../../';
        }
        return '';
    }

    forms.forEach(form => {
        // Handle forms that have an action pointing to contact.html (like on product pages)
        // or the main contact form on contact.html
        if (form.id === 'contact-form' || (form.getAttribute('action') && form.getAttribute('action').includes('contact.html'))) {
            
            form.addEventListener('submit', async function(e) {
                e.preventDefault();
                
                const formData = new FormData(this);
                // Append required fields for Web3Forms
                if (!formData.has('access_key')) {
                    formData.append('access_key', 'e2c3b8a3-8822-487e-b7d1-e945c9de0768'); // Updated with valid key placeholder
                }
                formData.append('subject', 'New Inquiry from Supreme Valves Website');
                formData.append('from_name', 'Supreme Valves Website');
                
                // Get email for Google Customer Reviews - try multiple common names
                const email = formData.get('email') || formData.get('Email') || formData.get('email_address');
                
                const button = this.querySelector('button[type="submit"]');
                const originalText = button ? button.textContent : 'Submit';
                if (button) {
                    button.textContent = 'Sending...';
                    button.disabled = true;
                }
                
                try {
                    const response = await fetch('https://api.web3forms.com/submit', {
                        method: 'POST',
                        body: formData
                    });
                    
                    const data = await response.json();
                    
                    if (data.success) {
                        // Redirect to thank-you page with email parameter for Google Customer Reviews
                        const basePath = getBasePath();
                        let redirectUrl = `${basePath}thank-you.html`;
                        if (email) {
                            redirectUrl += `?email=${encodeURIComponent(email)}`;
                        }
                        window.location.href = redirectUrl;
                    } else {
                        alert('Oops! Something went wrong. Please try again or email us directly at supremevalvesindia@gmail.com');
                    }
                } catch (error) {
                    alert('Oops! Something went wrong. Please try again or email us directly at supremevalvesindia@gmail.com');
                } finally {
                    if (button) {
                        button.textContent = originalText;
                        button.disabled = false;
                    }
                }
            });
        }
    });
});
