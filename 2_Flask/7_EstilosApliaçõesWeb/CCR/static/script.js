function carrossel(){
      const track = document.getElementById('artistsTrack');
      let page = 0; 

      function move(dir){
        const viewport = track.parentElement.getBoundingClientRect().width;
      
        const first = track.querySelector('.artist');
        if(!first) return;
        const style = getComputedStyle(track);
        const gap = parseFloat(style.gap || '0');
        const itemWidth = first.getBoundingClientRect().width;
        const perView = Math.max(1, Math.round((viewport + gap) / (itemWidth + gap)));

        const total = track.children.length;
        const maxPage = Math.ceil(total / perView) - 1;
        page = Math.min(maxPage, Math.max(0, page + dir));
        const offset = -(viewport + gap) * page;
        track.style.transform = `translateX(${offset}px)`;
      }

      document.querySelector('[data-action="prev"]').addEventListener('click', ()=> move(-1));
      document.querySelector('[data-action="next"]').addEventListener('click', ()=> move(1));
      window.addEventListener('resize', ()=> { track.style.transform = 'translateX(0)'; page = 0; });
    }

const menuHTML = document.getElementById('menu')
const footHTML = document.getElementById('foot')
const conteudoHTML = document.getElementById("conteudo")

addEventListener('DOMContentLoaded', () => {
  menuHTML.innerHTML = `<h2>Carregando menu...</h2>`
  let menu
  let foot
  if (document.body.id == 'login' || document.body.id=='cadastro'){
    menu = `
    <nav class="nav">
            <a class="brand" href="/" aria-label="Coda — Início">
                <span class="logo" aria-hidden="true"></span>
                <span>CODA</span>
            </a>
      </nav>
    `
    menuHTML.innerHTML = menu
    if (document.body.id == 'login'){
      conteudoHTML.innerHTML = `<h2>Carregando página de login...</h2>`
      fetch('/api/login')
      .then(response => {
        if(!response.ok){
          throw new Error("A resposta de rede não foi bem sucedida")
        }        
        return response.json()
      })
      .then(dados_forms => {

        let conteudo = `
        <main class="center" style="min-height: calc(100vh - 120px); padding: 20px;">
          <div class="card" style="max-width: 400px; width: 100%; padding: 32px; box-shadow: var(--shadow);">
              <h2 style="text-align:center; margin-bottom: 24px;">Entrar no Coda</h2>
              
              <form action="/logar" method="POST" style="display: grid; gap: 16px;"> `

        for (item of dados_forms){
          conteudo += `
                <!-- Email/Username -->
                <div>
                    <label for="${item.for}" class="muted" style="display:block; margin-bottom:6px;">${item.nome}</label>
                    <input type="text" id="${item.id}" name="${item.name}" placeholder="${item.placeholder}"
                        style="width:100%; padding:12px; border-radius:999px; border:1px solid var(--glass-border); background:var(--glass); color:var(--text); outline:none; transition: var(--transition);">
                </div>`

        }
        conteudo += `
        <!-- Remember Me -->
                <div style="display:flex; align-items:center; gap:10px;">
                    <input type="checkbox" id="remember" name="remember" value="remember">
                    <label for="remember" class="muted">Lembrar de mim</label>
                </div>
                
                <!-- Login Button -->
                <button type="submit" class="login-btn" id="login-btn" style="width:100%;">Entrar</button>
            </form>

                <!-- Links adicionais -->
                <div style="text-align:center; margin-top:16px;">
                    <a href="#" class="btn-link">Esqueceu a senha?</a> | 
                    <a href="mudarCadastro" class="btn-link">Criar conta</a>
                </div>
            </div>
        </main>
            `
        conteudoHTML.innerHTML = conteudo
      })
      .catch(error => {
        console.error('Erro ao buscar os dados do login', error)
        menuHTML.innerHTML = `
                <h2>Ocorreu um erro</h2>
                <p>Não foi possível carregar os dados. Verifique o console para mais detalhes</p>
                `
      })
    }
    else {
      conteudoHTML.innerHTML = `<h2>Carregando página de cadastro...</h2>`
      fetch('/api/cadastro')
      .then(response => {
        if (!response.ok){
          throw new Error('A resposta de rede não foi bem sucedida')
        }
        return response.json()
      })
      .then(dados_cadastro => {
      let conteudo = `
            <main class="center" style="min-height: calc(100vh - 120px); padding: 20px;">
              <div class="card" style="max-width: 450px; width: 100%; padding: 32px; box-shadow: var(--shadow);">
                  <h2 style="text-align:center; margin-bottom: 24px;">Crie sua conta no Coda</h2>
                  
                  <form action="/cadastrar" method="POST" style="display: grid; gap: 16px;">`
      for (item of dados_cadastro){
        conteudo += `
        <div>
            <label for="${item.for}" class="muted" style="display:block; margin-bottom:6px;">${item.nome}</label>
            <input type="${item.type}" id="${item.id}" name="${item.name}" placeholder="${item.placeholder}"
              style="width:100%; padding:12px; border-radius:999px; border:1px solid var(--glass-border); background:var(--glass); color:var(--text); outline:none; transition: var(--transition);">
        </div>
        `
      }  
      conteudo += `
                <!-- Botão de Cadastro -->
                <button type="submit" class="login-btn" style="width:100%;">Cadastrar</button>
            </form>

            <!-- Link para login -->
            <div style="text-align:center; margin-top:16px;">
                <span class="muted">Já possui uma conta? </span>
                <a href="/mudarLogin" class="btn-link">Entrar</a>
            </div>
        </div>
    </main>
      `
      conteudoHTML.innerHTML = conteudo
      })
      .catch(error => {
        console.error('Erro ao buscar dados da página cadastro', error)
        conteudoHTML.innerHTML = `
                <h2>Ocorreu um erro</h2>
                <p>Não foi possível carregar os dados. Verifique o console para mais detalhes</p>
                `
      })
    }
  }
  
  else {
  fetch('/api/menu')
  .then(response => {
    if (!response.ok){
      throw new Error('A resposta de rede não foi bem sucedida')
    }
  return response.json()
  })
  .then(dados_menu => {
    menu = `
    <nav class="nav">
      <a class="brand" href="/" aria-label="SomVerso — Início">
        <span class="logo" aria-hidden="true"></span>
        <span>CODA</span>
      </a>

      <form class="search" role="search">
        <input type="search" placeholder="Buscar artistas, músicas, festivais…" aria-label="Buscar" />
        <svg class="icon" width="22" height="22" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true"><path d="M21 21l-4.35-4.35M10.5 18a7.5 7.5 0 1 1 0-15 7.5 7.5 0 0 1 0 15Z" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>
      </form>


      <div class="right">
      <ul class="menu" aria-label="Navegação principal">
    `
    for(const item of dados_menu){
        menu += `
        <li>
            <a href="${item.rota}">${item.nome}</a>
            <div class="dropdown" role="menu" aria-label="Submenu ${item.nome}">
              <a href="#">${item.a}</a>
              <a href="#">${item.b}</a>
              <a href="#">${item.c}</a>
              <a href="#">${item.d}</a>
            </div>
        </li>
        `
    }
    menu += `</ul>
    <a href="/mudarLogin" style="text-decoration: none;">
          <button type="button" class="login-btn" aria-label="Entrar">Entrar</button>  
        </a>
        <button class="tema-btn" type="button" aria-label="Tema">Tema</button>
      </div>
    </nav>`
    menuHTML.innerHTML = menu
  })
  .catch(error => {
    console.error('Erro ao buscar os dados do menu', error)
    menuHTML.innerHTML = `
                <h2>Ocorreu um erro</h2>
                <p>Não foi possível carregar os dados. Verifique o console para mais detalhes</p>
                `
  })
  if(document.body.id == 'index'){
    conteudoHTML.innerHTML = `<h2>Carregando index...</h2>`
    Promise.all([
      fetch('/api/banner').then(response => {
        if (!response.ok){
          throw new Error('A resposta de rede não foi bem sucedida (dados banner)')
        }
        return response.json()}),
      fetch('/api/artistas').then(response => {
        if (!response.ok){
          throw new Error('A resposta de rede não foi bem sucedida (dados artistas)')
          
        }
        return response.json()}),
      fetch('/api/destaques').then(response =>{
        if (!response.ok){
          throw new Error('A resposta de rede não foi bem sucedida (dados destaques)')
          
        }
        return response.json()})
    ])
    .then(([dados_banners, dados_artistas, dados_destaques]) => {
      let pagina = `
      <section class="hero" aria-label="Em alta">
      <h1>Aplicação CSR</h1>
      <div class="hero-strip" >`

      for (item of dados_banners){
        pagina += `
          <a class="news-card" href="${item.url}" target="_blank">
            <span class="badge">${item.categoria}</span>
            <img class="thumb" src="${item.img}" alt="${item.alt}"/>
            <div class="title">${item.titulo}</div>
          </a>
        `
      }
      pagina += `</div></section>`
      pagina += `
      <section class="section" aria-labelledby="top-artistas">
      <div class="section-head">
        <h2 id="top-artistas">Top Artistas</h2>
        <div class="sub">Em alta nesta semana</div>
      </div>
      <div class="artists-wrap">
      <button class="arrow prev" aria-label="Anterior" data-action="prev">&#10094;</button>
      <div class="artists-viewport">
      <div class="artists-track" id="artistsTrack">`
      for (item of dados_artistas){
        pagina += `
        <a class="artist" href="#" aria-label="${item.nome}">
            <img src="${item.foto}" alt="${item.nome}" />
            <span class="overlay">${item.nome}</span>
        </a>
        `
      }
      pagina += `
      </div></div>
      <button class="arrow next" aria-label="Próximo" data-action="next">&#10095;</button>
      </div>
      </section>`

      pagina += `
      <section class="section" aria-label="Destaques">
      <div class="grid">`
      for(item of dados_destaques){
        pagina += `
        <article class="card">
          <img class="cover" src="${item.img}" alt="${item.alt}"/>
          <div class="body">
            <span class="chip">${item.categoria}</span>
            <h3 class="title-sm">${item.titulo}</h3>
          </div>
        </article>
        `
      }
      pagina += `
      </div>
      </section>`
      conteudoHTML.innerHTML = pagina
      carrossel()
    })
    .catch(error => {
      console.error("Erro ao buscar dados do index", error)
      conteudoHTML.innerHTML = `
                <h2>Ocorreu um erro</h2>
                <p>Não foi possível carregar os dados. Verifique o console para mais detalhes</p>
                `
    })
  }
  else {
    if(document.body.id == 'noticias'){
    conteudoHTML.innerHTML - `<h2>Carregando notícias...</h2>`
    fetch('/api/noticias')
    .then(response => {
      if(!response.ok){
        throw new Error('A resposta de rede não foi bem sucedida')
      }
      return response.json()})
    .then(dados_noticias => {
      reenderizar(dados_noticias, 'Notícias') 
    })
    .catch(error => {
      console.error('Erros ao buscar as notícias', error)
      conteudoHTML.innerHTML = `
                <h2>Ocorreu um erro</h2>
                <p>Não foi possível carregar os dados. Verifique o console para mais detalhes</p>
                `
    })
    }
    else if(document.body.id == 'eventos'){
      conteudoHTML.innerHTML - `<h2>Carregando eventos...</h2>`
      fetch('/api/eventos')
      .then(response => {
        if(!response.ok){
          throw new Error("A resposta de rede não foi bem sucedida")
        }
        return response.json()})
      .then(dados_eventos => {
        reenderizar(dados_eventos, 'Eventos')
      })
      .catch(error => {
        console.error('Erros ao buscar eventos', error)
        conteudoHTML.innerHTML = `
                <h2>Ocorreu um erro</h2>
                <p>Não foi possível carregar os dados. Verifique o console para mais detalhes</p>
                `
      })
    }
    else if(document.body.id == 'premiacoes'){
      conteudoHTML.innerHTML = `<h2>Carregando premiações...</h2>`
      fetch('/api/premiacoes')
      .then(response => {
        if(!response.ok){
          throw new Error('A resposta de rede não foi bem sucedida')
        }
        return response.json()})
      .then(dados_premiacoes => {
        reenderizar(dados_premiacoes, 'Premiações')
      })
      .catch(error => {
        console.error('Erro ao buscar premiações', error)
        conteudoHTML.innerHTML = `
                <h2>Ocorreu um erro</h2>
                <p>Não foi possível carregar os dados. Verifique o console para mais detalhes</p>
                `
      })
    }
  }
  }
  foot = `
  <div>
        <strong>Coda</strong> — Portal de música moderno. 
      </div>
      <div class="social" aria-label="Redes sociais">
        <span class="dot" title="Instagram"></span>
        <span class="dot" title="X/Twitter"></span>
      <span class="dot" title="YouTube"></span>
      </div>
  `
  footHTML.innerHTML = foot
})


function reenderizar (dados, pagina){
    let paginaConteudo = `
          <section class="section" aria-label="Destaques">
          <div class="grid">
        `
    for (item of dados){
      paginaConteudo += `
        <article class="card">
          <img class="cover" src="${item.img}" alt="" />
            <div class="body">
              <span class="chip chip--pink">${pagina}</span>
              <h3 class="title-sm">${item.titulo}</h3>
            </div>
        </article>
        `
    }

    paginaConteudo += `
      </div>
      </section>
      `
    conteudoHTML.innerHTML = paginaConteudo
  }


