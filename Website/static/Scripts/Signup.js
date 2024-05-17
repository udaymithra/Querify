
const eyeOpen=document.querySelectorAll('.eyeOpen')
const eyeClose=document.querySelectorAll('.eyeClose')

//Show Password
eyeOpen.forEach((openedEye)=>{
  openedEye.addEventListener("click",function(e){

     this.classList.add('hide')
     this.parentElement.querySelector('input[type=password]').setAttribute('type','text')
     this.parentElement.querySelector('.eyeClose').classList.remove('hide')
    
    })})   

//Hide Password

eyeClose.forEach((closedEye)=>{

  closedEye.addEventListener("click",function(e){

this.classList.add('hide')
this.parentElement.querySelector('input[type=text]').setAttribute('type','password')
this.parentElement.querySelector('.eyeOpen').classList.remove('hide')
})})