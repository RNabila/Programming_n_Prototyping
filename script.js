document.addEventListener('DOMContentLoaded', () => {
    const loadingScreen = document.getElementById('loading-screen');
    const quote = document.getElementById('quote');
    const name = document.getElementById('name');
    const mainContent = document.getElementById('main-content');

    // Fade in quote and name
    setTimeout(() => {
        quote.style.opacity = 1;
    }, 1000); // Fade in quote after 1 second

    setTimeout(() => {
        name.style.opacity = 1;
    }, 3000); // Fade in name after 3 seconds

    // Hide loading screen and show main content with a smooth transition
    setTimeout(() => {
        loadingScreen.style.transition = 'opacity 2s ease-in-out';
        loadingScreen.style.opacity = 0;

        setTimeout(() => {
            loadingScreen.style.display = 'none';
            mainContent.style.display = 'block';
            mainContent.style.opacity = 0;
            mainContent.style.transition = 'opacity 2s ease-in-out';
            mainContent.style.opacity = 1;
        }, 2000); // Wait for loading screen to fully fade out before showing main content
    }, 5000); // Start hiding the loading screen after 5 seconds
});

const audio = new Audio('{{ url_for('static', filename='quill-scratch.mp3') }}');
setTimeout(() => {
    audio.play();
}, 1000); // Play sound as the quote fades in
