document.querySelector("#searchMob").addEventListener("click", () => {
  document.querySelector(".mobNav").style.display = "none";
  document.querySelector(".mobSearchBar").style.display = "flex";
  document.querySelector(".mobSearchBar").style.opacity = "1";
});
document.querySelector("#backMob").addEventListener("click", () => {
  document.querySelector(".mobNav").style.display = "flex";
  document.querySelector(".mobSearchBar").style.opacity = "0";
  document.querySelector(".mobSearchBar").style.display = "none";
});