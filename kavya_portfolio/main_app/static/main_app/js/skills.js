document.addEventListener("DOMContentLoaded", () => {
    // Animate all skill bars after slight delay
    const bars = document.querySelectorAll(".bar");

    bars.forEach(bar => {
        const originalWidth = getComputedStyle(bar).width;
        bar.style.width = "0"; // Reset width initially
        setTimeout(() => {
            bar.style.width = originalWidth;
        }, 300);
    });
});
