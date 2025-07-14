var username = document.getElementById("username")
var email = document.getElementById("email")
var password = document.getElementById("password")
var message = document.getElementById('message')
var botao = document.getElementById('submit')
var form = document.getElementById('form')



function verificaCampos (){
    if (!username.value || !email.value || !password.value){
        message.innerText = 'Todos os campos são obrigatórios!'
        return
    }
    else if (!email.includes('@gmail.com') && !email.includes('@yahoo.com') && !email.includes('@hotmail.com') || email.startsWith('@')){
        message.textContent = 'Email inválido'
        return
    }
    else{
        message.textContent = ''
        return
    }
}

//addEventListener('submit', ()=> {
   //verificaCampos()
//})

botao.addEventListener("click", (e)=>{
    //e.preventDefault()
    verificaCampos()
    return message.innerHtml = 'teste'
})

//botao.addEventListener('submit', ()=>{
  //  verificaCampos()
//})