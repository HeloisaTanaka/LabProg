var username = document.getElementById("username")
var email = document.getElementById("email")
var password = document.getElementById("password")
var message = document.getElementById('message')


function verificaCampos (){
    if (!username.value || !email.value || !password.value){
        var mensagem = 'Todos os campos são obrigatórios' 
    }
    else if (!email.value.includes('@gmail.com') && !email.value.includes('@yahoo.com') && !email.value.includes('@hotmail.com') || email.value.startsWith('@')){
        var mensagem = 'Email inválido'  
    }
    else{
       var mensagem = 'Cadastro realizado com sucesso'
        
    }
    localStorage.setItem('message', mensagem)
}

addEventListener('submit', ()=> {
   verificaCampos()
})

document.addEventListener('DOMContentLoaded', () => {
    const mensagemSalva = localStorage.getItem('message');
    if (mensagemSalva) {
        document.getElementById('message').textContent = mensagemSalva;
    }
})

