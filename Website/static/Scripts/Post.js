const quill = new Quill("#editor", {
  modules: {
    toolbar: true,
  },
  theme: "snow",
});

function isImgElement(element) {
  return element instanceof Image;
}
// Saving the content pre-submission
function save() {
  const editorContentElement = document.querySelector("#editorContent");
  document.querySelector("#editor").firstElementChild.querySelectorAll('img').forEach((eachContent)=>{

  const image = eachContent

    if (isImgElement(image) && image) {
      image.setAttribute("alt", "Post Image"); 
    }
  
  })
  const editorContent =
    document.querySelector("#editor").firstElementChild.innerHTML;

  if (editorContent === "<p>Type your Query here.</p>") {
    alert("Please enter your query/content.");
    return;
  }
  editorContentElement.value = editorContent;
  document
    .querySelector("#editFormButton")
    .setAttribute("class", "visibleFlex");
  document.querySelector("#submitButton").setAttribute("class", "visibleFlex");
  document.querySelector("#saveFormButton").setAttribute("class", "hide");
  document.querySelector("#discardFormButton").setAttribute("class", "hide");
  document.querySelector(".ql-editor").setAttribute("contenteditable", "false");
}
function edit() {
  document.querySelector("#submitButton").setAttribute("class", "hide");
  document.querySelector("#editFormButton").setAttribute("class", "hide");
  document
    .querySelector("#saveFormButton")
    .setAttribute("class", "visibleFlex");
  document
    .querySelector("#discardFormButton")
    .setAttribute("class", "visibleFlex");
  document.querySelector(".ql-editor").setAttribute("contenteditable", "true");
}
