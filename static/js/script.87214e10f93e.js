const closeButton = document.querySelector(".btn-close");
const alertElement = document.querySelector(".alert");
const carouselElem = document.querySelector(".main-carousel");
const arrow = document.getElementById("arrow");

// Arrow to the top of the page
arrow.style.display = "none";

const scrollFunction = () => {
  if (document.body.scrollTop > 50 || document.documentElement.scrollTop > 50) {
    arrow.style.display = "block";
  } else {
    arrow.style.display = "none";
  }
};

window.onscroll = () => {
  scrollFunction();
};

// Working form alert button without Bootstrap JS
if (closeButton && alertElement) {
  closeButton.addEventListener("click", () => {
    alertElement.style.display = "none";
  });
}

// Lighthouse audit low score fix
document.addEventListener("DOMContentLoaded", function () {
  let flkty = new Flickity(carouselElem, {
    wrapAround: true,
    pageDots: false,
    autoPlay: true,
    pauseAutoPlayOnHover: false,
    setGallerySize: false,
  });

  carouselElem.style.visibility = "visible";
});
