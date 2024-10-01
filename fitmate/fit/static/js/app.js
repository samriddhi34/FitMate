const texts = document.querySelectorAll('.text');
let index = 0;

function showText() {
    texts.forEach((text, i) => {
        text.style.display = 'none'; // Hide all text
    });
    texts[index].style.display = 'block'; // Show current text
    index = (index + 1) % texts.length; // Update index
}

setInterval(showText, 3000); // Change text every 3 seconds
showText(); // Initial call to display the first text
