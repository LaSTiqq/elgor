const closeButton = document.querySelector(".btn-close");
const alertElement = document.querySelector(".alert");

if (closeButton && alertElement) {
  closeButton.addEventListener("click", () => {
    alertElement.style.display = "none";
  });
}

const elem = document.querySelector(".main-carousel");

document.addEventListener("DOMContentLoaded", function () {
  let flkty = new Flickity(elem, {
    cellAlign: "left",
    wrapAround: true,
    pageDots: false,
    autoPlay: true,
    pauseAutoPlayOnHover: false,
  });

  elem.style.visibility = "visible";
  flkty.reloadCells();
});
