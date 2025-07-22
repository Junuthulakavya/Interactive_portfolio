document.addEventListener("DOMContentLoaded", () => {
    // Resize the map
    if (typeof imageMapResize === 'function') {
        imageMapResize();
    }

    const areas = document.querySelectorAll("area");
    const sound = document.getElementById("click-sound");
    const loader = document.getElementById("loader");

    areas.forEach(area => {
        area.addEventListener("click", function(e) {
            e.preventDefault();

            if (sound) sound.play();
            loader.classList.remove("hidden");

            setTimeout(() => {
                window.location.href = this.href;
            }, 800); // Delay for loader effect
        });
    });

    // Hide loader on page load
    window.addEventListener("load", () => {
        setTimeout(() => {
            loader.classList.add("hidden");
        }, 500);
    });
});
