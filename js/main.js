// La Intersindical VDD - JavaScript

// Navegació
document.addEventListener('DOMContentLoaded', function() {
  const header = document.querySelector('header');
  const menuToggle = document.querySelector('.menu-toggle');
  const navLinks = document.querySelector('.nav-links');

  // Efecte de scroll de l'encapçalament
  window.addEventListener('scroll', function() {
    if (window.scrollY > 100) {
      header.classList.add('scrolled');
    } else {
      header.classList.remove('scrolled');
    }
  });

  // Alternar menú mòbil
  if (menuToggle) {
    menuToggle.addEventListener('click', function() {
      navLinks.classList.toggle('active');
    });
  }

  // Carregar les últimes notícies a la pàgina d'inici
  const latestNewsContainer = document.getElementById('latest-news');
  if (latestNewsContainer) {
    loadLatestNews(latestNewsContainer);
  }

  // Carregar totes les notícies a la pàgina de notícies
  const allNewsContainer = document.getElementById('all-news');
  if (allNewsContainer) {
    loadAllNews(allNewsContainer);
  }
});

async function loadLatestNews(container) {
  try {
    const response = await fetch('noticias/noticias.json');
    const news = await response.json();
    const latest = news.slice(0, 3);
    renderNewsCards(container, latest);
  } catch (error) {
    console.error('Error carregant notícies:', error);
    container.innerHTML = '<p>No hi ha notícies disponibles.</p>';
  }
}

async function loadAllNews(container) {
  try {
    const response = await fetch('noticias/noticias.json');
    const news = await response.json();
    renderNewsCards(container, news);
  } catch (error) {
    console.error('Error carregant notícies:', error);
    container.innerHTML = '<p>No hi ha notícies disponibles.</p>';
  }
}

function renderNewsCards(container, news) {
  container.innerHTML = news.map(item => `
    <article class="news-card">
      <img src="${item.image || 'img/placeholder.jpg'}" alt="${item.title}">
      <div class="news-card-content">
        <span class="news-card-date">${formatDate(item.date)}</span>
        <h3 class="news-card-title">${item.title}</h3>
        <p class="news-card-excerpt">${item.excerpt}</p>
        <a href="noticias/${item.slug}/index.html" class="read-more">Llegir més →</a>
      </div>
    </article>
  `).join('');
}

function formatDate(dateString) {
  const options = { year: 'numeric', month: 'long', day: 'numeric' };
  return new Date(dateString).toLocaleDateString('ca-ES', options);
}
