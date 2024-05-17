const quill = new Quill("#editor", {
    placeholder: "Add a comment...",

    theme: "bubble",
});

const quillReply = new Quill("#replyEditor", {
    placeholder: "Reply...",

    theme: "bubble",
});

function save() {
    const commentContentElement = document.querySelector("#commentContent");
    const addCommentContent =
        document.querySelector("#editor").firstElementChild.innerHTML;

    if (addCommentContent === "<p>Type your Query here.</p>") {
        alert("Please enter your query/content.");
        return;
    } else if (addCommentContent === "<p><br></p>") {
        alert("Please add your comment...");
        return;
    }

    commentContentElement.value = addCommentContent;
    document
        .querySelector("#editCommentButton")
        .setAttribute("class", "visibleFlex");
    document
        .querySelector("#addCommentButton")
        .setAttribute("class", "visibleFlex");
    document.querySelector("#saveCommentButton").setAttribute("class", "hide");
    document.querySelector("#discardCommentButton").setAttribute("class", "hide");
    document.querySelector(".ql-editor").setAttribute("contenteditable", "false");
}

function edit() {
    document.querySelector("#addCommentButton").setAttribute("class", "hide");
    document.querySelector("#editCommentButton").setAttribute("class", "hide");
    document
        .querySelector("#saveCommentButton")
        .setAttribute("class", "visibleFlex");
    document
        .querySelector("#discardCommentButton")
        .setAttribute("class", "visibleFlex");
    document.querySelector(".ql-editor").setAttribute("contenteditable", "true");
}

function Reply() {
    const replyContentElement = document.querySelector("#replyComment");
    const replyEditorContent =
        document.querySelector("#replyEditor").firstChild.innerHTML;
    if (replyEditorContent === "<p><br></p>") {
        alert("Add reply...");
        return false;
    } else {
        const replyEditorContent =
            document.querySelector("#replyEditor").firstElementChild.innerHTML;

        const replyingTo =
            document.querySelector(".replyto").firstElementChild.textContent;

        document.querySelector("#replyTo").value = replyingTo;
        document.querySelector("#replyComment").value = replyEditorContent;
        return true;
    }

    replyContentElement.value = replyEditorContent;
}

function activateReply() {
    document.querySelectorAll(".replyToComment").forEach((replyButton) => {
        replyButton.addEventListener("click", function () {
            //Enabling reply container
            const replyFormContainer = document.querySelector("#replyFormContainer");
            replyFormContainer.setAttribute("class", "visibleBlock");
            const commentId = replyButton.getAttribute("data-comment-id");
            replyFormContainer.firstElementChild.setAttribute(
                "action",
                `/comment/reply/${commentId}`
            );
            document.querySelector(".replyto").firstElementChild.textContent =
                "@" + replyButton.getAttribute("data-reply-to");
            document.querySelector("#replyToPostId").value =
                replyButton.getAttribute("data-post-id");

            //scroll to that reply action
            replyFormContainer.scrollIntoView({
                behavior: "smooth"
            });
        });
    });
}
activateReply();

/// set side line height for replies

document.querySelectorAll(".repliesContainer").forEach((replyContainer) => {
    const repliesHeight =
        Math.round(replyContainer.querySelector(".replies").offsetHeight) + "px";
    replyContainer.querySelector(".sideLine").style.height = repliesHeight;
});

// Read More Functionality for Comments
const readMoreComment = () => {
    const readMoreBtns = document.querySelectorAll(".read-more-comment");

    readMoreBtns.forEach((btn) => {
        btn.addEventListener("click", function () {
            const content =
                this.parentElement.parentElement.querySelector(".commentContent");

            content.classList.toggle("expanded");

            if (content.classList.contains("expanded")) {
                this.textContent = "Read Less";
            } else {
                this.textContent = "Read More";
            }
        });
    });
};

function readMoreCommentHide() {
    const myDiv = document.querySelectorAll(".commentContent");
    myDiv.forEach((div) => {
        div.style.height = "auto";

        const height = div.offsetHeight;

        const parentDiv = div.parentElement;
        div.style.height = "100px";

        if (Math.round(height) > 100) {
            parentDiv
                .querySelector(".replyComment")
                .querySelector(".read-more-comment")
                .setAttribute("class", "read-more-comment");
        } else {
            parentDiv
                .querySelector(".replyComment")
                .querySelector(".read-more-comment")
                .classList.add("hide");
        }
    });
    readMoreComment();
}

readMoreCommentHide();

/*  Read More Function for Post  */
const readMorePost = () => {
    const readMoreBtns = document.querySelectorAll(".read-more");

    readMoreBtns.forEach((btn) => {
        btn.addEventListener("click", function () {
            const content = this.parentElement.parentElement
                .querySelector(".postContentContainer")
                .querySelector(".postContent");

            content.classList.toggle("expanded");

            if (content.classList.contains("expanded")) {
                this.textContent = "Read Less";
                this.parentElement.parentElement
                    .querySelector(".postContentContainer")
                    .querySelector(".sideLine").style.height =
                    Math.round(
                        this.parentElement.parentElement
                        .querySelector(".postContentContainer")
                        .querySelector(".postContent").offsetHeight
                    ) + "px";
            } else {
                this.textContent = "Read More";
                this.parentElement.parentElement
                    .querySelector(".postContentContainer")
                    .querySelector(".sideLine").style.height = "200px";
            }
        });
    });
};

function readMorePostHide() {
    const myDiv = document.querySelectorAll(".postContent");
    myDiv.forEach((div) => {
        div.style.height = "auto";

        const height = div.offsetHeight;

        const parentDiv = div.parentElement.parentElement;
        div.style.height = "200px";

        if (Math.round(height) > 200) {
            parentDiv.querySelector(".read-more").setAttribute("class", "read-more");
        } else {
            parentDiv.querySelector(".read-more").classList.add("hide");
        }
    });
    readMorePost();
}

readMorePostHide();
//  real-time likes dislikes functionality
var socket = io();

// Like the post
document.querySelectorAll(".likesImg").forEach((img) => {
    img.addEventListener("click", () => {
        const postId = img.dataset.postId; // Access data-post-id using dataset property
        socket.emit("like_update_count", {
            post_id: postId
        });
        img.classList.remove("visibleInline");
        img.classList.add("hide");
        img.parentElement
            .querySelector(".disLikesImg")
            .classList.add("visibleInline");
    });
});

socket.on("like_count_updated", function (data) {
    const postId = data.post_id;
    const count = data.count;
    document.querySelectorAll(".likesImg").forEach((img) => {
        // Update the count only if it matches the expected post ID (implement logic here)
        if (img.dataset.postId == postId) {
            img.parentElement.parentElement.parentElement.querySelector(
                ".postLikeCount"
            ).innerText = count + " likes";
        }
    });
});

//Dislike the post
document.querySelectorAll(".disLikesImg").forEach((img) => {
    img.addEventListener("click", () => {
        const postId = img.dataset.postId; // Access data-post-id using dataset property
        socket.emit("dislike_update_count", {
            post_id: postId
        });
        img.classList.remove("visibleInline");
        img.classList.add("hide");
        img.parentElement.querySelector(".likesImg").classList.add("visibleInline");
    });
});

socket.on("dislike_count_updated", function (data) {
    const postId = data.post_id;
    const count = data.count;
    document.querySelectorAll(".disLikesImg").forEach((img) => {
        // Update the count only if it matches the expected post ID (implement logic here)
        if (img.dataset.postId == postId) {
            img.parentElement.parentElement.parentElement.querySelector(
                ".postLikeCount"
            ).innerText = count + " likes";
        }
    });
});

/* Real Time Like Count Update of Comment */

var socket2 = io();

// Like the post
document.querySelectorAll(".commentsLikesImg").forEach((img) => {
    img.addEventListener("click", () => {
        const userId = img.dataset.userId; // Access data-user-id using dataset property
        const commentId = img.dataset.commentId; // Access data-comment-id using dataset property
        socket2.emit("like_update_comment_count", {
            user_id: userId,
            comment_id: commentId,
        });
        img.classList.remove("visibleInline");
        img.classList.add("hide");
        img.parentElement
            .querySelector(".commentsDisLikesImg")
            .classList.add("visibleInline");
    });
});

socket2.on("like_update_comment_count", function (data) {
    const commentId = data.comment_id;
    const count = data.count;
    document.querySelectorAll(".commentsLikesImg").forEach((img) => {
        // Update the count only if it matches the expected post ID (implement logic here)
        if (img.dataset.commentId == commentId) {
            img.parentElement.parentElement.parentElement.querySelector(
                ".replyCommentLike"
            ).firstElementChild.innerHTML = count + " likes";
        }
    });
});

//Dislike the post
document.querySelectorAll(".commentsDisLikesImg").forEach((img) => {
    img.addEventListener("click", () => {
        const userId = img.dataset.userId; // Access data-user-id using dataset property
        const commentId = img.dataset.commentId; // Access data-comment-id using dataset property
        socket2.emit("dislike_update_comment_count", {
            user_id: userId,
            comment_id: commentId,
        });
        img.classList.remove("visibleInline");
        img.classList.add("hide");
        img.parentElement
            .querySelector(".commentsLikesImg")
            .classList.add("visibleInline");
    });
});

socket2.on("dislike_update_comment_count", function (data) {
    const commentId = data.comment_id;
    const count = data.count;
    document.querySelectorAll(".commentsDisLikesImg").forEach((img) => {
        // Update the count only if it matches the expected post ID (implement logic here)
        if (img.dataset.commentId === commentId) {
            img.parentElement.parentElement.parentElement.querySelector(
                ".replyCommentLike"
            ).firstElementChild.innerHTML = count + " likes";
        }
    });
});