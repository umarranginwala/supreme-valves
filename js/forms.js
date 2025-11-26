/**
 * Supreme Valves - Form Handler Module
 * Centralized form validation and submission
 */

class FormHandler {
    constructor() {
        this.forms = new Map();
        this.validators = {
            required: (value) => value.trim() !== '',
            email: (value) => /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(value),
            phone: (value) => /^[\d\s\-\+\(\)]+$/.test(value) && value.replace(/\D/g, '').length >= 10,
            minLength: (value, length) => value.length >= length,
            maxLength: (value, length) => value.length <= length
        };
    }

    /**
     * Initialize form
     */
    initForm(formId, options = {}) {
        const form = document.getElementById(formId);
        if (!form) return;

        const config = {
            onSubmit: options.onSubmit || this.defaultSubmit,
            validation: options.validation || {},
            realTimeValidation: options.realTimeValidation !== false
        };

        this.forms.set(formId, config);

        // Add submit event listener
        form.addEventListener('submit', (e) => this.handleSubmit(e, formId));

        // Add real-time validation
        if (config.realTimeValidation) {
            form.querySelectorAll('input, textarea, select').forEach(field => {
                field.addEventListener('blur', () => this.validateField(field, formId));
                field.addEventListener('input', Utils.debounce(() => {
                    this.validateField(field, formId);
                }, 500));
            });
        }
    }

    /**
     * Validate field
     */
    validateField(field, formId) {
        const config = this.forms.get(formId);
        if (!config) return true;

        const fieldName = field.name;
        const fieldValue = field.value;
        const rules = config.validation[fieldName] || {};

        let isValid = true;
        let errorMessage = '';

        // Check each validation rule
        for (const [rule, ruleValue] of Object.entries(rules)) {
            if (rule === 'required' && ruleValue) {
                if (!this.validators.required(fieldValue)) {
                    isValid = false;
                    errorMessage = `${this.getFieldLabel(field)} is required`;
                    break;
                }
            } else if (rule === 'email' && ruleValue) {
                if (fieldValue && !this.validators.email(fieldValue)) {
                    isValid = false;
                    errorMessage = 'Please enter a valid email address';
                    break;
                }
            } else if (rule === 'phone' && ruleValue) {
                if (fieldValue && !this.validators.phone(fieldValue)) {
                    isValid = false;
                    errorMessage = 'Please enter a valid phone number';
                    break;
                }
            } else if (rule === 'minLength') {
                if (fieldValue && !this.validators.minLength(fieldValue, ruleValue)) {
                    isValid = false;
                    errorMessage = `Minimum ${ruleValue} characters required`;
                    break;
                }
            }
        }

        // Update UI
        this.updateFieldUI(field, isValid, errorMessage);
        return isValid;
    }

    /**
     * Get field label
     */
    getFieldLabel(field) {
        const label = field.closest('.form-group')?.querySelector('label');
        return label ? label.textContent.replace('*', '').trim() : field.name;
    }

    /**
     * Update field UI
     */
    updateFieldUI(field, isValid, errorMessage) {
        // Remove existing error
        const existingError = field.parentElement.querySelector('.error-message');
        if (existingError) {
            existingError.remove();
        }

        // Update field styling
        if (isValid) {
            field.classList.remove('error');
            field.classList.add('valid');
        } else {
            field.classList.remove('valid');
            field.classList.add('error');

            // Add error message
            if (errorMessage) {
                const errorDiv = document.createElement('div');
                errorDiv.className = 'error-message';
                errorDiv.textContent = errorMessage;
                errorDiv.style.cssText = 'color: #e74c3c; font-size: 0.875rem; margin-top: 0.25rem;';
                field.parentElement.appendChild(errorDiv);
            }
        }
    }

    /**
     * Validate entire form
     */
    validateForm(formId) {
        const form = document.getElementById(formId);
        if (!form) return false;

        let isValid = true;
        const fields = form.querySelectorAll('input, textarea, select');

        fields.forEach(field => {
            if (!this.validateField(field, formId)) {
                isValid = false;
            }
        });

        return isValid;
    }

    /**
     * Handle form submission
     */
    async handleSubmit(e, formId) {
        e.preventDefault();

        const config = this.forms.get(formId);
        if (!config) return;

        // Validate form
        if (!this.validateForm(formId)) {
            Utils.showNotification('Please fix the errors in the form', 'error');
            return;
        }

        // Get form data
        const form = e.target;
        const formData = new FormData(form);
        const data = Object.fromEntries(formData.entries());

        // Show loading state
        const submitBtn = form.querySelector('button[type="submit"]');
        const originalText = submitBtn.textContent;
        submitBtn.disabled = true;
        submitBtn.textContent = 'Submitting...';

        try {
            // Call custom submit handler
            await config.onSubmit(data, form);
            
            // Success
            Utils.showNotification('Form submitted successfully!', 'success');
            form.reset();
            
            // Remove validation classes
            form.querySelectorAll('.valid, .error').forEach(field => {
                field.classList.remove('valid', 'error');
            });
        } catch (error) {
            console.error('Form submission error:', error);
            Utils.showNotification('An error occurred. Please try again.', 'error');
        } finally {
            // Reset button
            submitBtn.disabled = false;
            submitBtn.textContent = originalText;
        }
    }

    /**
     * Default submit handler (redirect to contact page)
     */
    defaultSubmit(data, form) {
        return new Promise((resolve) => {
            // Build query string
            const params = new URLSearchParams(data);
            window.location.href = `contact.html?${params.toString()}`;
            resolve();
        });
    }

    /**
     * Custom submit handler for AJAX
     */
    ajaxSubmit(endpoint) {
        return async (data) => {
            const response = await fetch(endpoint, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(data)
            });

            if (!response.ok) {
                throw new Error('Network response was not ok');
            }

            return await response.json();
        };
    }
}

// Create global instance
window.formHandler = new FormHandler();

// Auto-initialize common forms
document.addEventListener('DOMContentLoaded', () => {
    // Initialize quote request forms
    document.querySelectorAll('form[action*="contact.html"]').forEach(form => {
        if (form.id) {
            window.formHandler.initForm(form.id, {
                validation: {
                    name: { required: true, minLength: 2 },
                    email: { required: true, email: true },
                    phone: { phone: true },
                    message: { required: true, minLength: 10 }
                }
            });
        }
    });
});
