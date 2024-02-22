const closeButton = document.querySelector(".btn-close");
const alertElement = document.querySelector(".alert");

if (closeButton && alertElement) {
  closeButton.addEventListener("click", () => {
    alertElement.style.display = "none";
  });
}

const elem = document.querySelector(".main-carousel");
let flkty = new Flickity(elem, {
  accessibility: true,
  cellAlign: "left",
  draggable: ">1",
  wrapAround: true,
  pageDots: false,
  autoPlay: true,
  pauseAutoPlayOnHover: false,
});
