// La Intersindical VDD - JavaScript

// Navigation
document.addEventListener('DOMContentLoaded', function() {
  const header = document.querySelector('header');
  const menuToggle = document.querySelector('.menu-toggle');
  const navLinks = document.querySelector('.nav-links');

  // Header scroll effect
  window.addEventListener('scroll', function() {
    if (window.scrollY > 100) {
      header.classList.add('scrolled');
    } else {
      header.classList.remove('scrolled');
    }
  });

  // Mobile menu toggle
  if (menuToggle) {
    menuToggle.addEventListener('click', function() {
      navLinks.classList.toggle('active');
    });
  }

  // Load latest news on index page
  const latestNewsContainer = document.getElementById('latest-news');
  if (latestNewsContainer) {
    loadLatestNews(latestNewsContainer);
  }

  // Load all news on noticias page
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
    console.error('Error loading news:', error);
    container.innerHTML = '<p>No hay noticias disponibles.</p>';
  }
}

async function loadAllNews(container) {
  try {
    const response = await fetch('noticias/noticias.json');
    const news = await response.json();
    renderNewsCards(container, news);
  } catch (error) {
    console.error('Error loading news:', error);
    container.innerHTML = '<p>No hay noticias disponibles.</p>';
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
        <a href="noticias/${item.slug}/index.html" class="read-more">Leer más →</a>
      </div>
    </article>
  `).join('');
}

function formatDate(dateString) {
  const options = { year: 'numeric', month: 'long', day: 'numeric' };
  return new Date(dateString).toLocaleDateString('es-ES', options);
}
