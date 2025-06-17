// Tracks the current index for each slideshow group
const slideIndices = {};

// Initialize slides on page load
window.addEventListener("load", () => {
  showSlides(1, 'capsule');
  showSlides(1, 'test');
});

// Navigate between slides
function plusSlides(n, id) {
  showSlides((slideIndices[id] || 1) + n, id);
}

// Jump to specific slide
function currentSlide(n, id) {
  showSlides(n, id);
}

// Show the nth slide for a given group
function showSlides(n, id) {
  const slides = document.querySelectorAll(`.slides.${id}`);
  const dots = document.querySelectorAll(`.${id}-dot`);

  if (slides.length === 0) return;

  if (n > slides.length) n = 1;
  if (n < 1) n = slides.length;
  slideIndices[id] = n;

  slides.forEach(slide => slide.style.display = "none");
  dots.forEach(dot => dot.classList.remove("active"));

  slides[n - 1].style.display = "block";
  if (dots[n - 1]) dots[n - 1].classList.add("active");
}
