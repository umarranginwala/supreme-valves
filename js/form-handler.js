/**
 * Supreme Valves India - Global Form Handler
 * Handles AJAX form submissions and redirects to thank-you page
 * Required for Google Customer Reviews integration
 */

document.addEventListener('DOMContentLoaded', function() {
    // Find all inquiry forms on the page
    const forms = document.querySelectorAll('form');
    
    forms.forEach(form => {
        // Handle forms that have an action pointing to contact.html (like on product pages)
        // or the main contact form on contact.html
        if (form.id === 'contact-form' || form.getAttribute('action')?.includes('contact.html')) {
            
            form.addEventListener('submit', async function(e) {
                // If it's a simple GET redirect form (like on product pages), 
                // we let it proceed to contact.html unless we want to handle it here.
                // However, for the best UX and GCR tracking, we want to handle the submission
                // and go straight to thank-you.html if possible.
                
                // If we are on contact.html, handle the Web3Forms submission
                if (window.location.pathname.includes('contact.html')) {
                    e.preventDefault();
                    
                    const formData = new FormData(this);
                    // Append required fields for Web3Forms if not present
                    if (!formData.has('access_key')) {
                        formData.append('access_key', 'YOUR_WEB3FORMS_ACCESS_KEY'); // User setup required
                    }
                    formData.append('subject', 'New Inquiry from Supreme Valves Website');
                    formData.append('from_name', 'Supreme Valves Website');
                    
                    const button = this.querySelector('button[type="submit"]');
                    const originalText = button.textContent;
                    button.textContent = 'Sending...';
                    button.disabled = true;
                    
                    try {
                        const response = await fetch('https://api.web3forms.com/submit', {
                            method: 'POST',
                            body: formData
                        });
                        
                        const data = await response.json();
                        
                        if (data.success) {
                            // Redirect to thank-you page with email parameter for Google Customer Reviews
                            const email = formData.get('email');
                            window.location.href = `thank-you.html?email=${encodeURIComponent(email)}`;
                        } else {
                            alert('Oops! Something went wrong. Please try again or email us directly at supremevalvesindia@gmail.com');
                        }
                    } catch (error) {
                        alert('Oops! Something went wrong. Please try again or email us directly at supremevalvesindia@gmail.com');
                    } finally {
                        button.textContent = originalText;
                        button.disabled = false;
                    }
                }
                // For product pages, the form usually just redirects to contact.html with params.
                // This is fine as the contact page will then handle the final submission.
            });
        }
    });
});
