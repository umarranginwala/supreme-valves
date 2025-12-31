/**
 * Supreme Valves - Navigation & UI Logic
 * Handles mobile menu, dropdowns, and other global UI interactions
 */

document.addEventListener('DOMContentLoaded', function() {
    const header = document.querySelector('header');
    const nav = document.querySelector('header nav');
    const container = document.querySelector('header .container');
    
    if (!header || !nav || !container) return;

    // 1. Create Mobile Menu Toggle (Hamburger) if it doesn't exist
    if (!document.querySelector('.menu-toggle')) {
        const menuToggle = document.createElement('div');
        menuToggle.className = 'menu-toggle';
        menuToggle.innerHTML = '<span></span><span></span><span></span>';
        container.appendChild(menuToggle);
        
        // 2. Create Overlay if it doesn't exist
        if (!document.querySelector('.nav-overlay')) {
            const overlay = document.createElement('div');
            overlay.className = 'nav-overlay';
            document.body.appendChild(overlay);
            
            // 3. Toggle Menu Logic
            function toggleMenu() {
                menuToggle.classList.toggle('active');
                nav.classList.toggle('active');
                overlay.classList.toggle('active');
                document.body.style.overflow = nav.classList.contains('active') ? 'hidden' : '';
            }

            menuToggle.addEventListener('click', toggleMenu);
            overlay.addEventListener('click', toggleMenu);
        }
    }

    // 4. Mobile Dropdown Logic
    const dropdowns = document.querySelectorAll('.dropdown');
    dropdowns.forEach(dropdown => {
        const btn = dropdown.querySelector('.dropbtn');
        if (btn) {
            btn.addEventListener('click', function(e) {
                if (window.innerWidth <= 1024) {
                    // Only prevent default if clicking the icon or if we want to toggle the menu instead of following the link
                    // Usually on mobile, first click opens dropdown, second follows link. 
                    // But here we'll toggle dropdown on mobile.
                    if (e.target.tagName === 'I' || !dropdown.classList.contains('active')) {
                        e.preventDefault();
                        dropdown.classList.toggle('active');
                    }
                }
            });
        }
    });

    // 5. Close menu on window resize if larger than 1024px
    window.addEventListener('resize', function() {
        const menuToggle = document.querySelector('.menu-toggle');
        const overlay = document.querySelector('.nav-overlay');
        if (window.innerWidth > 1024 && nav.classList.contains('active')) {
            menuToggle.classList.remove('active');
            nav.classList.remove('active');
            overlay.classList.remove('active');
            document.body.style.overflow = '';
        }
    });

    // 6. Highlight active menu item
    const currentPath = window.location.pathname;
    const navLinks = document.querySelectorAll('header nav ul li a');
    
    navLinks.forEach(link => {
        const href = link.getAttribute('href');
        if (!href) return;
        
        // Remove trailing slashes and normalize
        const normalizedPath = currentPath.replace(/\/$/, '').split('/').pop() || 'index.html';
        const normalizedHref = href.split('/').pop();
        
        if (normalizedPath === normalizedHref) {
            link.classList.add('active');
        } else if (currentPath.includes('/products/') && normalizedHref === 'products.html') {
            link.classList.add('active');
        } else if (currentPath.includes('/blog/') && normalizedHref === 'blog.html') {
            link.classList.add('active');
        } else if (currentPath.includes('/projects/') && normalizedHref === 'projects.html') {
            link.classList.add('active');
        }
    });
});
