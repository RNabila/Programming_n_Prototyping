document.addEventListener('DOMContentLoaded', () => {
    const loadingScreen = document.getElementById('loading-screen');
    const quote = document.getElementById('quote');
    const name = document.getElementById('name');
    const mainContent = document.getElementById('main-content');

    // Fade in quote and name
    setTimeout(() => {
        quote.style.opacity = 1;
    }, 2000);

    setTimeout(() => {
        name.style.opacity = 1;
    }, 4000);

    // Hide loading screen and show main content
    setTimeout(() => {
        loadingScreen.style.opacity = 0;
        loadingScreen.style.pointerEvents = 'none';
        mainContent.style.display = 'block';
    }, 6000);
});
