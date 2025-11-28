document.addEventListener('DOMContentLoaded', () => {
    console.log('ThinkUverse Loaded');

    // Simple parallax effect for the orb
    const orb = document.querySelector('.orb');
    if (orb) {
        document.addEventListener('mousemove', (e) => {
            const x = e.clientX / window.innerWidth;
            const y = e.clientY / window.innerHeight;
            orb.style.transform = `translate(-50%, -50%) translate(${x * 30}px, ${y * 30}px)`;
        });
    }
});
