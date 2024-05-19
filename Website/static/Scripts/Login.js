// Show & Hide Password Functionality
const eyeOpen=document.querySelector('#eyeOpen')
const eyeClose=document.querySelector('#eyeClose')

//Show Password
eyeOpen.addEventListener("click",function(e){

  this.classList.add('hide')
  this.parentElement.querySelector('input[type=password]').setAttribute('type','text')
  eyeClose.classList.remove('hide')

})

//Hide Password
eyeClose.addEventListener("click",function(e){

this.classList.add('hide')
this.parentElement.querySelector('input[type=text]').setAttribute('type','password')
eyeOpen.classList.remove('hide')

})
