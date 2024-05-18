// Profile Details Edit Functionality
document.querySelectorAll(".profileEditButton").forEach((editButton) => {
    editButton.addEventListener("click", function (e) {
        document.querySelector("#saveProfile").classList.remove("hide");

        this.parentElement.querySelectorAll("input").forEach((input) => {
            input.removeAttribute("readonly");
            input.focus();
        });
    });
});

//Post Delete Functionality
document.querySelectorAll(".postDeleteButton").forEach((deleteButton) => {
    deleteButton.addEventListener("click", function (e) {
        const postIdField = document.getElementById("postIdField");
        postIdField.value = this.dataset.postId;
        const deleteConfirmationContainer = document.querySelector(
            ".deleteConfirmationContainer"
        );
        deleteConfirmationContainer.classList.remove("hide");
        document.querySelector("#postIdNo").addEventListener("click", function (e) {
            postIdField.value = "";
            deleteConfirmationContainer.classList.add("hide");
        });
    });
});