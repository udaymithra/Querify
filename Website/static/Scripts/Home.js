/*---------------------Real-time like count update--------------------*/
var socket = io();


// Like the post 
document.querySelectorAll('.likesImg').forEach((img)=>{

  img.addEventListener('click',()=>{

    const postId = img.dataset.postId;  // Access data-post-id using dataset property
    socket.emit('like_update_count', { post_id: postId });
    img.classList.remove('visibleInline')
    img.classList.add('hide')
    img.parentElement.querySelector('.disLikesImg').classList.add('visibleInline')
  })
})


socket.on('like_count_updated', function(data) {
    const postId = data.post_id;
    const count = data.count;
    document.querySelectorAll('.likesImg').forEach((img)=>{


    // Update the count only if it matches the expected post ID (implement logic here)
    if (img.dataset.postId==postId) {
       img.parentElement.parentElement.parentElement.querySelector('.postLikeCount').innerText = count + ' likes';
    }
})});

//Dislike the post 
document.querySelectorAll('.disLikesImg').forEach((img)=>{

img.addEventListener('click',()=>{

  const postId = img.dataset.postId;  // Access data-post-id using dataset property
  socket.emit('dislike_update_count', { post_id: postId });
  img.classList.remove('visibleInline')
  img.classList.add('hide')
  img.parentElement.querySelector('.likesImg').classList.add('visibleInline')

})
})


socket.on('dislike_count_updated', function(data) {
  const postId = data.post_id;
  const count = data.count;
  document.querySelectorAll('.disLikesImg').forEach((img)=>{


  // Update the count only if it matches the expected post ID (implement logic here)
  if (img.dataset.postId==postId) {
     img.parentElement.parentElement.parentElement.querySelector('.postLikeCount').innerText = count + ' likes';
  }
})});

/*---------------------------------------------------------------------------*/


/*-------------------------------Comment Logic------------------------------*/
const commentImages = document.querySelectorAll('.commentImg');  // Select all images with class 'comment-image'

commentImages.forEach(image => {
    image.addEventListener('click', function() {
        const postId =image.dataset.postId  // Extract postId from image ID
        window.location.href = `/comment/${postId}`;  // Redirect with postId
    });
});

/*--------------------------------------------------------------------------*/
const readMoreFunction = () =>{
  const readMoreBtns = document.querySelectorAll('.read-more');

readMoreBtns.forEach(btn => {
    btn.addEventListener('click', function() {

        const content = this.parentElement.parentElement.querySelector('.postContentContainer').querySelector('.postContent');
       
        content.classList.toggle('expanded');
       
        if (content.classList.contains('expanded')) {
            this.textContent = 'Read Less';
            this.parentElement.parentElement.querySelector('.postContentContainer').querySelector('.sideLine').style.height=Math.round(this.parentElement.parentElement.querySelector('.postContentContainer').querySelector('.postContent').offsetHeight)+'px'
           
        } else {
            this.textContent = 'Read More';
            this.parentElement.parentElement.querySelector('.postContentContainer').querySelector('.sideLine').style.height='200px'
        }
    });
});
}
function readMoreHide(){

  const myDiv = document.querySelectorAll(".postContent");
  myDiv.forEach((div)=>{
  div.style.height='auto'
  
  const height = div.offsetHeight;;

  const parentDiv=div.parentElement.parentElement;
  div.style.height='200px'
  
  if(Math.round(height)>200){
   
    parentDiv.querySelector('.read-more').setAttribute('class', 'read-more');
    
  }
  else{
    parentDiv.querySelector('.read-more').classList.add('hide');
   
  }
 

})
 readMoreFunction()

}


readMoreHide()

