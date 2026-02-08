// Language switching functionality
const translations = {
    fr: {},
    en: {}
};

function switchLanguage(lang) {
    document.querySelectorAll('[data-fr]').forEach(element => {
        if (lang === 'fr') {
            element.textContent = element.getAttribute('data-fr');
        } else if (lang === 'en') {
            element.textContent = element.getAttribute('data-en');
        }
    });
    localStorage.setItem('language', lang);
}

// Initialize language
document.addEventListener('DOMContentLoaded', () => {
    const languageSelector = document.getElementById('language-selector');
    const savedLanguage = localStorage.getItem('language') || 'fr';

    if (languageSelector) {
        languageSelector.value = savedLanguage;
        switchLanguage(savedLanguage);

        languageSelector.addEventListener('change', (e) => {
            switchLanguage(e.target.value);
        });
    }

    // Hamburger menu functionality
    const hamburger = document.getElementById('hamburger');
    const menuOverlay = document.getElementById('menu-overlay');
    const closeMenu = document.getElementById('close-menu');

    if (hamburger && menuOverlay) {
        hamburger.addEventListener('click', () => {
            menuOverlay.classList.add('active');
        });
    }

    if (closeMenu && menuOverlay) {
        closeMenu.addEventListener('click', () => {
            menuOverlay.classList.remove('active');
        });
    }

    // Close menu when clicking outside
    if (menuOverlay) {
        menuOverlay.addEventListener('click', (e) => {
            if (e.target === menuOverlay) {
                menuOverlay.classList.remove('active');
            }
        });
    }
});