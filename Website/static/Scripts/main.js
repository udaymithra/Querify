const popUp = document.querySelector(".errorPopUp");
const message = popUp.dataset.message;
const category = popUp.dataset.category;

if (category == "False") {
    popUp.style.top = "15%";
    popUp.style.display = "flex";
    document.querySelector(".errorMessage").innerHTML = message;
} else if (category == "True") {
    popUp.style.top = "15%";
    popUp.style.background = "#C6EBC5";
    popUp.style.display = "flex";
    document.querySelector(".errorMessage").innerHTML = message;
    document.querySelector(".errorMessage").style.color = "#76885B";
}
document.querySelector(".closeLogo").addEventListener("click", () => {
    popUp.style.display = "none";
});