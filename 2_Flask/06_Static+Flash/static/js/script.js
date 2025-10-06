// Verificação do lado do usuário

var username = document.getElementById("username") //Busca o elemento pelo seu id no html
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

addEventListener('submit', ()=> { //Executa quando houver um submit no forms
   verificaCampos() //Define qual será a mensagem
})

document.addEventListener('DOMContentLoaded', () => {      //Executa quando a página carrega ou recarrega
    const mensagemSalva = localStorage.getItem('message'); //Pega a message arazenda no localStorage
    if (mensagemSalva) {
        document.getElementById('message').textContent = mensagemSalva; //Atualiza a mensagem no HTML
    }
})

//Quando o flask executa o render_template, as modificações JS são excluídas.
//Uma maneira de resolver o problema é armazenando o item no localStorage e 
//depois executar uma função para exibir o elemento, após a execução do render_template do flask
