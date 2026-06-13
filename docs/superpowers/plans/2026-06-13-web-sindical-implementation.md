# Web La Intersindical VDD - Plan de Implementación

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Crear una web estática para información sindical con sistema de generación automática de noticias desde PDFs.

**Architecture:** HTML estático + CSS + JavaScript vanilla. Script Python para convertir PDFs a HTML. Datos de noticias en JSON.

**Tech Stack:** HTML5, CSS3, JavaScript, Python, pdfplumber, beautifulsoup4

---

## File Structure

```
la_intersindical_vdd/
├── index.html
├── noticias.html
├── noticia.html
├── documentos.html
├── contacto.html
├── css/
│   └── style.css
├── js/
│   └── main.js
├── img/
│   └── logo.png
├── noticias/
│   ├── noticias.json
│   └── ejemplo-noticia/
│       ├── index.html
│       └── img/
├── documentos/
│   └── documentos.json
├── pdfs/
├── requirements.txt
└── generar.py
```

---

### Task 1: Project Setup

**Files:**
- Create: `requirements.txt`
- Create: `css/style.css`
- Create: `js/main.js`
- Create: `img/` (directory)

- [ ] **Step 1: Create requirements.txt**

```
pdfplumber>=0.10.0
beautifulsoup4>=4.12.0
```

- [ ] **Step 2: Create directory structure**

```bash
mkdir css js img noticias documentos pdfs
```

- [ ] **Step 3: Create empty CSS file**

```css
/* La Intersindical VDD - Estilos */
```

- [ ] **Step 4: Create empty JS file**

```javascript
// La Intersindical VDD - JavaScript
```

- [ ] **Step 5: Commit**

```bash
git add requirements.txt css/ js/ img/ noticias/ documentos/ pdfs/
git commit -m "feat: initial project structure"
```

---

### Task 2: Base CSS Styles

**Files:**
- Create: `css/style.css`

- [ ] **Step 1: Create CSS variables and reset**

```css
:root {
  --primary: #e5352c;
  --secondary: #1a1a1a;
  --bg-light: #ffffff;
  --text: #333333;
  --text-light: #666666;
  --border: #e0e0e0;
}

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  font-family: 'Poppins', sans-serif;
  color: var(--text);
  background-color: var(--bg-light);
  line-height: 1.6;
}
```

- [ ] **Step 2: Add typography styles**

```css
h1, h2, h3, h4, h5, h6 {
  font-weight: 700;
  line-height: 1.2;
  margin-bottom: 1rem;
}

h1 { font-size: 2.5rem; }
h2 { font-size: 2rem; }
h3 { font-size: 1.5rem; }

p {
  margin-bottom: 1rem;
}

a {
  color: var(--primary);
  text-decoration: none;
  transition: color 0.3s ease;
}

a:hover {
  color: #c42d24;
}
```

- [ ] **Step 3: Add container and layout styles**

```css
.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 1rem;
}

.section {
  padding: 4rem 0;
}

.section-dark {
  background-color: var(--secondary);
  color: var(--bg-light);
}
```

- [ ] **Step 4: Commit**

```bash
git add css/style.css
git commit -m "feat: add base CSS styles and variables"
```

---

### Task 3: Header and Navigation Styles

**Files:**
- Modify: `css/style.css`

- [ ] **Step 1: Add header styles**

```css
header {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  background: transparent;
  z-index: 1000;
  transition: background 0.3s ease, box-shadow 0.3s ease;
}

header.scrolled {
  background: var(--bg-light);
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}

nav {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1rem 0;
}

.logo img {
  height: 40px;
}

.nav-links {
  display: flex;
  list-style: none;
  gap: 2rem;
}

.nav-links a {
  color: var(--bg-light);
  font-weight: 500;
  transition: color 0.3s ease;
}

header.scrolled .nav-links a {
  color: var(--text);
}

.nav-links a:hover {
  color: var(--primary);
}
```

- [ ] **Step 2: Add mobile menu button styles**

```css
.menu-toggle {
  display: none;
  background: none;
  border: none;
  font-size: 1.5rem;
  color: var(--bg-light);
  cursor: pointer;
}

header.scrolled .menu-toggle {
  color: var(--text);
}

@media (max-width: 768px) {
  .menu-toggle {
    display: block;
  }

  .nav-links {
    position: fixed;
    top: 60px;
    left: 0;
    right: 0;
    background: var(--bg-light);
    flex-direction: column;
    align-items: center;
    padding: 2rem;
    gap: 1rem;
    transform: translateY(-100%);
    opacity: 0;
    transition: transform 0.3s ease, opacity 0.3s ease;
    pointer-events: none;
  }

  .nav-links.active {
    transform: translateY(0);
    opacity: 1;
    pointer-events: all;
  }

  .nav-links a {
    color: var(--text);
  }
}
```

- [ ] **Step 3: Commit**

```bash
git add css/style.css
git commit -m "feat: add header and navigation styles"
```

---

### Task 4: Hero Section Styles

**Files:**
- Modify: `css/style.css`

- [ ] **Step 1: Add hero styles**

```css
.hero {
  position: relative;
  height: 100vh;
  min-height: 500px;
  display: flex;
  align-items: center;
  justify-content: center;
  text-align: center;
  color: var(--bg-light);
  background-size: cover;
  background-position: center;
  background-attachment: fixed;
}

.hero::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: linear-gradient(180deg, rgba(10, 8, 8, 0.77), rgba(10, 8, 8, 0.77));
}

.hero-content {
  position: relative;
  z-index: 1;
  max-width: 800px;
  padding: 0 1rem;
}

.hero h1 {
  font-size: 3rem;
  margin-bottom: 1.5rem;
}

.hero-buttons {
  display: flex;
  gap: 1rem;
  justify-content: center;
  flex-wrap: wrap;
}
```

- [ ] **Step 2: Add button styles**

```css
.btn {
  display: inline-block;
  padding: 0.75rem 2rem;
  font-weight: 600;
  text-align: center;
  border-radius: 4px;
  transition: all 0.3s ease;
  cursor: pointer;
  border: none;
}

.btn-primary {
  background: var(--primary);
  color: var(--bg-light);
}

.btn-primary:hover {
  background: #c42d24;
  color: var(--bg-light);
}

.btn-secondary {
  background: transparent;
  color: var(--bg-light);
  border: 2px solid var(--bg-light);
}

.btn-secondary:hover {
  background: var(--bg-light);
  color: var(--text);
}
```

- [ ] **Step 3: Commit**

```bash
git add css/style.css
git commit -m "feat: add hero section and button styles"
```

---

### Task 5: News Cards and Footer Styles

**Files:**
- Modify: `css/style.css`

- [ ] **Step 1: Add news card styles**

```css
.news-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 2rem;
}

.news-card {
  background: var(--bg-light);
  border-radius: 8px;
  overflow: hidden;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.news-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.15);
}

.news-card img {
  width: 100%;
  height: 200px;
  object-fit: cover;
}

.news-card-content {
  padding: 1.5rem;
}

.news-card-date {
  font-size: 0.875rem;
  color: var(--text-light);
  margin-bottom: 0.5rem;
}

.news-card-title {
  font-size: 1.25rem;
  margin-bottom: 0.5rem;
}

.news-card-excerpt {
  color: var(--text-light);
  margin-bottom: 1rem;
}

.read-more {
  color: var(--primary);
  font-weight: 600;
}
```

- [ ] **Step 2: Add footer styles**

```css
footer {
  background: var(--secondary);
  color: var(--bg-light);
  padding: 4rem 0 2rem;
}

.footer-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 2rem;
  margin-bottom: 3rem;
}

.footer-column h3 {
  font-size: 1.125rem;
  margin-bottom: 1.5rem;
}

.footer-column ul {
  list-style: none;
}

.footer-column li {
  margin-bottom: 0.75rem;
}

.footer-column a {
  color: var(--bg-light);
  opacity: 0.8;
  transition: opacity 0.3s ease;
}

.footer-column a:hover {
  opacity: 1;
  color: var(--bg-light);
}

.footer-bottom {
  border-top: 1px solid rgba(255, 255, 255, 0.1);
  padding-top: 2rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.social-links {
  display: flex;
  gap: 1rem;
}

.social-links a {
  color: var(--bg-light);
  font-size: 1.25rem;
}

@media (max-width: 768px) {
  .footer-grid {
    grid-template-columns: 1fr;
    text-align: center;
  }

  .footer-bottom {
    flex-direction: column;
    gap: 1rem;
  }
}
```

- [ ] **Step 3: Commit**

```bash
git add css/style.css
git commit -m "feat: add news cards and footer styles"
```

---

### Task 6: Create index.html

**Files:**
- Create: `index.html`

- [ ] **Step 1: Create HTML structure**

```html
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>La Intersindical VDD</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="css/style.css">
</head>
<body>
  <header>
    <nav class="container">
      <a href="index.html" class="logo">
        <img src="img/logo.png" alt="La Intersindical VDD">
      </a>
      <button class="menu-toggle" aria-label="Menú">☰</button>
      <ul class="nav-links">
        <li><a href="index.html">Inicio</a></li>
        <li><a href="noticias.html">Noticias</a></li>
        <li><a href="documentos.html">Documentos</a></li>
        <li><a href="contacto.html">Contacto</a></li>
      </ul>
    </nav>
  </header>

  <main>
    <section class="hero" style="background-image: url('img/hero-bg.jpg')">
      <div class="hero-content">
        <h1>La Intersindical VDD</h1>
        <p>Información sindical, laboral y de actualidad</p>
        <div class="hero-buttons">
          <a href="noticias.html" class="btn btn-primary">Últimas Noticias</a>
          <a href="contacto.html" class="btn btn-secondary">Contacto</a>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <h2>Últimas Noticias</h2>
        <div id="latest-news" class="news-grid">
          <!-- Se carga dinámicamente -->
        </div>
      </div>
    </section>
  </main>

  <footer>
    <div class="container">
      <div class="footer-grid">
        <div class="footer-column">
          <h3>La Intersindical VDD</h3>
          <p>Sindicato dedicado a la defensa de los derechos laborales y sociales.</p>
        </div>
        <div class="footer-column">
          <h3>Navegación</h3>
          <ul>
            <li><a href="index.html">Inicio</a></li>
            <li><a href="noticias.html">Noticias</a></li>
            <li><a href="documentos.html">Documentos</a></li>
            <li><a href="contacto.html">Contacto</a></li>
          </ul>
        </div>
        <div class="footer-column">
          <h3>Contacto</h3>
          <ul>
            <li>Email: info@intersindicalvdd.org</li>
            <li>Tel: 93 123 45 67</li>
          </ul>
        </div>
        <div class="footer-column">
          <h3>Síguenos</h3>
          <div class="social-links">
            <a href="#" aria-label="Facebook">FB</a>
            <a href="#" aria-label="Twitter">TW</a>
            <a href="#" aria-label="Instagram">IG</a>
          </div>
        </div>
      </div>
      <div class="footer-bottom">
        <p>&copy; 2026 La Intersindical VDD. Todos los derechos reservados.</p>
      </div>
    </div>
  </footer>

  <script src="js/main.js"></script>
</body>
</html>
```

- [ ] **Step 2: Commit**

```bash
git add index.html
git commit -m "feat: create index.html with hero and latest news section"
```

---

### Task 7: Create JavaScript

**Files:**
- Create: `js/main.js`

- [ ] **Step 1: Create main.js with navigation and news loading**

```javascript
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
```

- [ ] **Step 2: Commit**

```bash
git add js/main.js
git commit -m "feat: add JavaScript for navigation and news loading"
```

---

### Task 8: Create noticias.html

**Files:**
- Create: `noticias.html`

- [ ] **Step 1: Create noticias.html**

```html
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Noticias - La Intersindical VDD</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="css/style.css">
</head>
<body>
  <header class="scrolled">
    <nav class="container">
      <a href="index.html" class="logo">
        <img src="img/logo.png" alt="La Intersindical VDD">
      </a>
      <button class="menu-toggle" aria-label="Menú">☰</button>
      <ul class="nav-links">
        <li><a href="index.html">Inicio</a></li>
        <li><a href="noticias.html">Noticias</a></li>
        <li><a href="documentos.html">Documentos</a></li>
        <li><a href="contacto.html">Contacto</a></li>
      </ul>
    </nav>
  </header>

  <main style="padding-top: 80px;">
    <section class="section">
      <div class="container">
        <h1>Noticias</h1>
        <div id="all-news" class="news-grid">
          <!-- Se carga dinámicamente -->
        </div>
      </div>
    </section>
  </main>

  <footer>
    <div class="container">
      <div class="footer-grid">
        <div class="footer-column">
          <h3>La Intersindical VDD</h3>
          <p>Sindicato dedicado a la defensa de los derechos laborales y sociales.</p>
        </div>
        <div class="footer-column">
          <h3>Navegación</h3>
          <ul>
            <li><a href="index.html">Inicio</a></li>
            <li><a href="noticias.html">Noticias</a></li>
            <li><a href="documentos.html">Documentos</a></li>
            <li><a href="contacto.html">Contacto</a></li>
          </ul>
        </div>
        <div class="footer-column">
          <h3>Contacto</h3>
          <ul>
            <li>Email: info@intersindicalvdd.org</li>
            <li>Tel: 93 123 45 67</li>
          </ul>
        </div>
        <div class="footer-column">
          <h3>Síguenos</h3>
          <div class="social-links">
            <a href="#" aria-label="Facebook">FB</a>
            <a href="#" aria-label="Twitter">TW</a>
            <a href="#" aria-label="Instagram">IG</a>
          </div>
        </div>
      </div>
      <div class="footer-bottom">
        <p>&copy; 2026 La Intersindical VDD. Todos los derechos reservados.</p>
      </div>
    </div>
  </footer>

  <script src="js/main.js"></script>
</body>
</html>
```

- [ ] **Step 2: Commit**

```bash
git add noticias.html
git commit -m "feat: create noticias.html page"
```

---

### Task 9: Create Article Template

**Files:**
- Create: `noticia.html`

- [ ] **Step 1: Create noticia.html template**

```html
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Noticia - La Intersindical VDD</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="../css/style.css">
  <style>
    .article-header {
      padding: 6rem 0 2rem;
      background: var(--secondary);
      color: var(--bg-light);
      text-align: center;
    }
    .article-meta {
      margin-bottom: 1rem;
      opacity: 0.8;
    }
    .article-content {
      max-width: 800px;
      margin: 0 auto;
      padding: 3rem 1rem;
    }
    .article-content img {
      width: 100%;
      height: auto;
      border-radius: 8px;
      margin: 1.5rem 0;
    }
    .back-link {
      display: inline-block;
      margin-bottom: 2rem;
      color: var(--primary);
    }
  </style>
</head>
<body>
  <header class="scrolled">
    <nav class="container">
      <a href="../index.html" class="logo">
        <img src="../img/logo.png" alt="La Intersindical VDD">
      </a>
      <button class="menu-toggle" aria-label="Menú">☰</button>
      <ul class="nav-links">
        <li><a href="../index.html">Inicio</a></li>
        <li><a href="../noticias.html">Noticias</a></li>
        <li><a href="../documentos.html">Documentos</a></li>
        <li><a href="../contacto.html">Contacto</a></li>
      </ul>
    </nav>
  </header>

  <main>
    <div class="article-header">
      <div class="container">
        <h1 id="article-title">Título de la Noticia</h1>
        <div class="article-meta">
          <span id="article-date">Fecha</span>
        </div>
      </div>
    </div>

    <article class="article-content">
      <a href="../noticias.html" class="back-link">← Volver a noticias</a>
      <div id="article-body">
        <!-- Contenido del artículo -->
      </div>
    </article>
  </main>

  <footer>
    <div class="container">
      <div class="footer-bottom">
        <p>&copy; 2026 La Intersindical VDD. Todos los derechos reservados.</p>
      </div>
    </div>
  </footer>

  <script>
    // Cargar artículo individual
    document.addEventListener('DOMContentLoaded', function() {
      const articleBody = document.getElementById('article-body');
      const articleTitle = document.getElementById('article-title');
      const articleDate = document.getElementById('article-date');

      // Obtener datos del artículo desde attributes o JSON
      const title = articleBody.getAttribute('data-title') || 'Noticia';
      const date = articleBody.getAttribute('data-date') || '';
      const content = articleBody.getAttribute('data-content') || '';

      articleTitle.textContent = title;
      articleDate.textContent = date ? new Date(date).toLocaleDateString('es-ES', { year: 'numeric', month: 'long', day: 'numeric' }) : '';
    });
  </script>
  <script src="../js/main.js"></script>
</body>
</html>
```

- [ ] **Step 2: Commit**

```bash
git add noticia.html
git commit -m "feat: create article template page"
```

---

### Task 10: Create documentos.html

**Files:**
- Create: `documentos.html`

- [ ] **Step 1: Create documentos.html**

```html
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Documentos - La Intersindical VDD</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="css/style.css">
  <style>
    .document-list {
      list-style: none;
    }
    .document-item {
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 1.5rem;
      background: var(--bg-light);
      border: 1px solid var(--border);
      border-radius: 8px;
      margin-bottom: 1rem;
      transition: box-shadow 0.3s ease;
    }
    .document-item:hover {
      box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
    }
    .document-info h3 {
      margin-bottom: 0.25rem;
      font-size: 1.125rem;
    }
    .document-info p {
      margin: 0;
      color: var(--text-light);
      font-size: 0.875rem;
    }
    .btn-download {
      background: var(--primary);
      color: var(--bg-light);
      padding: 0.5rem 1.5rem;
      border-radius: 4px;
      font-weight: 500;
    }
    .btn-download:hover {
      background: #c42d24;
      color: var(--bg-light);
    }
  </style>
</head>
<body>
  <header class="scrolled">
    <nav class="container">
      <a href="index.html" class="logo">
        <img src="img/logo.png" alt="La Intersindical VDD">
      </a>
      <button class="menu-toggle" aria-label="Menú">☰</button>
      <ul class="nav-links">
        <li><a href="index.html">Inicio</a></li>
        <li><a href="noticias.html">Noticias</a></li>
        <li><a href="documentos.html">Documentos</a></li>
        <li><a href="contacto.html">Contacto</a></li>
      </ul>
    </nav>
  </header>

  <main style="padding-top: 80px;">
    <section class="section">
      <div class="container">
        <h1>Documentos</h1>
        <p>Descarga nuestros documentos oficiales, convenios y guías laborales.</p>
        <ul id="document-list" class="document-list">
          <!-- Se carga dinámicamente -->
        </ul>
      </div>
    </section>
  </main>

  <footer>
    <div class="container">
      <div class="footer-grid">
        <div class="footer-column">
          <h3>La Intersindical VDD</h3>
          <p>Sindicato dedicado a la defensa de los derechos laborales y sociales.</p>
        </div>
        <div class="footer-column">
          <h3>Navegación</h3>
          <ul>
            <li><a href="index.html">Inicio</a></li>
            <li><a href="noticias.html">Noticias</a></li>
            <li><a href="documentos.html">Documentos</a></li>
            <li><a href="contacto.html">Contacto</a></li>
          </ul>
        </div>
        <div class="footer-column">
          <h3>Contacto</h3>
          <ul>
            <li>Email: info@intersindicalvdd.org</li>
            <li>Tel: 93 123 45 67</li>
          </ul>
        </div>
        <div class="footer-column">
          <h3>Síguenos</h3>
          <div class="social-links">
            <a href="#" aria-label="Facebook">FB</a>
            <a href="#" aria-label="Twitter">TW</a>
            <a href="#" aria-label="Instagram">IG</a>
          </div>
        </div>
      </div>
      <div class="footer-bottom">
        <p>&copy; 2026 La Intersindical VDD. Todos los derechos reservados.</p>
      </div>
    </div>
  </footer>

  <script src="js/main.js"></script>
  <script>
    document.addEventListener('DOMContentLoaded', async function() {
      const documentList = document.getElementById('document-list');
      try {
        const response = await fetch('documentos/documentos.json');
        const documents = await response.json();
        documentList.innerHTML = documents.map(doc => `
          <li class="document-item">
            <div class="document-info">
              <h3>${doc.title}</h3>
              <p>${doc.description} - ${formatDate(doc.date)}</p>
            </div>
            <a href="documentos/${doc.file}" class="btn-download" download>Descargar</a>
          </li>
        `).join('');
      } catch (error) {
        documentList.innerHTML = '<p>No hay documentos disponibles.</p>';
      }

      function formatDate(dateString) {
        const options = { year: 'numeric', month: 'long', day: 'numeric' };
        return new Date(dateString).toLocaleDateString('es-ES', options);
      }
    });
  </script>
</body>
</html>
```

- [ ] **Step 2: Commit**

```bash
git add documentos.html
git commit -m "feat: create documentos.html page"
```

---

### Task 11: Create contacto.html

**Files:**
- Create: `contacto.html`

- [ ] **Step 1: Create contacto.html**

```html
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Contacto - La Intersindical VDD</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="css/style.css">
  <style>
    .contact-grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 3rem;
    }
    .contact-info h2 {
      margin-bottom: 1.5rem;
    }
    .contact-info p {
      margin-bottom: 1rem;
    }
    .contact-info ul {
      list-style: none;
      margin-bottom: 2rem;
    }
    .contact-info li {
      margin-bottom: 0.75rem;
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }
    .contact-form h2 {
      margin-bottom: 1.5rem;
    }
    .form-group {
      margin-bottom: 1.5rem;
    }
    .form-group label {
      display: block;
      margin-bottom: 0.5rem;
      font-weight: 500;
    }
    .form-group input,
    .form-group textarea {
      width: 100%;
      padding: 0.75rem;
      border: 1px solid var(--border);
      border-radius: 4px;
      font-family: inherit;
      font-size: 1rem;
    }
    .form-group textarea {
      min-height: 150px;
      resize: vertical;
    }
    .map-container {
      margin-top: 3rem;
      border-radius: 8px;
      overflow: hidden;
      height: 300px;
    }
    .map-container iframe {
      width: 100%;
      height: 100%;
      border: 0;
    }
    @media (max-width: 768px) {
      .contact-grid {
        grid-template-columns: 1fr;
      }
    }
  </style>
</head>
<body>
  <header class="scrolled">
    <nav class="container">
      <a href="index.html" class="logo">
        <img src="img/logo.png" alt="La Intersindical VDD">
      </a>
      <button class="menu-toggle" aria-label="Menú">☰</button>
      <ul class="nav-links">
        <li><a href="index.html">Inicio</a></li>
        <li><a href="noticias.html">Noticias</a></li>
        <li><a href="documentos.html">Documentos</a></li>
        <li><a href="contacto.html">Contacto</a></li>
      </ul>
    </nav>
  </header>

  <main style="padding-top: 80px;">
    <section class="section">
      <div class="container">
        <h1>Contacto</h1>
        <div class="contact-grid">
          <div class="contact-info">
            <h2>Información de contacto</h2>
            <p>Estamos aquí para ayudarte. No dudes en contactarnos para cualquier consulta sobre derechos laborales, afiliación o cualquier otra cuestión sindical.</p>
            <ul>
              <li>📧 info@intersindicalvdd.org</li>
              <li>📞 93 123 45 67</li>
              <li>📍 Carrer de l'Exempleo, 123<br>08001 Barcelona</li>
              <li>🕐 Lunes a Viernes: 9:00 - 18:00</li>
            </ul>
          </div>
          <div class="contact-form">
            <h2>Envíanos un mensaje</h2>
            <form id="contact-form">
              <div class="form-group">
                <label for="name">Nombre</label>
                <input type="text" id="name" name="name" required>
              </div>
              <div class="form-group">
                <label for="email">Email</label>
                <input type="email" id="email" name="email" required>
              </div>
              <div class="form-group">
                <label for="message">Mensaje</label>
                <textarea id="message" name="message" required></textarea>
              </div>
              <button type="submit" class="btn btn-primary">Enviar mensaje</button>
            </form>
          </div>
        </div>
        <div class="map-container">
          <iframe src="https://www.openstreetmap.org/export/embed.html?bbox=-0.1276,51.5034,-0.1076,51.5234&layer=mapnik" allowfullscreen></iframe>
        </div>
      </div>
    </section>
  </main>

  <footer>
    <div class="container">
      <div class="footer-grid">
        <div class="footer-column">
          <h3>La Intersindical VDD</h3>
          <p>Sindicato dedicado a la defensa de los derechos laborales y sociales.</p>
        </div>
        <div class="footer-column">
          <h3>Navegación</h3>
          <ul>
            <li><a href="index.html">Inicio</a></li>
            <li><a href="noticias.html">Noticias</a></li>
            <li><a href="documentos.html">Documentos</a></li>
            <li><a href="contacto.html">Contacto</a></li>
          </ul>
        </div>
        <div class="footer-column">
          <h3>Contacto</h3>
          <ul>
            <li>Email: info@intersindicalvdd.org</li>
            <li>Tel: 93 123 45 67</li>
          </ul>
        </div>
        <div class="footer-column">
          <h3>Síguenos</h3>
          <div class="social-links">
            <a href="#" aria-label="Facebook">FB</a>
            <a href="#" aria-label="Twitter">TW</a>
            <a href="#" aria-label="Instagram">IG</a>
          </div>
        </div>
      </div>
      <div class="footer-bottom">
        <p>&copy; 2026 La Intersindical VDD. Todos los derechos reservados.</p>
      </div>
    </div>
  </footer>

  <script src="js/main.js"></script>
  <script>
    document.getElementById('contact-form').addEventListener('submit', function(e) {
      e.preventDefault();
      alert('Mensaje enviado. Nos pondremos en contacto contigo pronto.');
      this.reset();
    });
  </script>
</body>
</html>
```

- [ ] **Step 2: Commit**

```bash
git add contacto.html
git commit -m "feat: create contacto.html page"
```

---

### Task 12: Create Example News Data

**Files:**
- Create: `noticias/noticias.json`
- Create: `noticias/ejemplo-noticia/index.html`
- Create: `documentos/documentos.json`

- [ ] **Step 1: Create noticias.json**

```json
[
  {
    "slug": "ejemplo-noticia",
    "title": "Ejemplo de Noticia Sindical",
    "date": "2026-06-13",
    "excerpt": "Esta es una noticia de ejemplo para demostrar el funcionamiento del sistema de noticias.",
    "image": "img/placeholder.jpg",
    "content": "<p>Contenido completo de la noticia de ejemplo.</p>"
  }
]
```

- [ ] **Step 2: Create ejemplo-noticia/index.html**

```html
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Ejemplo de Noticia - La Intersindical VDD</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="../../css/style.css">
  <style>
    .article-header {
      padding: 6rem 0 2rem;
      background: var(--secondary);
      color: var(--bg-light);
      text-align: center;
    }
    .article-meta {
      margin-bottom: 1rem;
      opacity: 0.8;
    }
    .article-content {
      max-width: 800px;
      margin: 0 auto;
      padding: 3rem 1rem;
    }
    .article-content img {
      width: 100%;
      height: auto;
      border-radius: 8px;
      margin: 1.5rem 0;
    }
    .back-link {
      display: inline-block;
      margin-bottom: 2rem;
      color: var(--primary);
    }
  </style>
</head>
<body>
  <header class="scrolled">
    <nav class="container">
      <a href="../../index.html" class="logo">
        <img src="../../img/logo.png" alt="La Intersindical VDD">
      </a>
      <button class="menu-toggle" aria-label="Menú">☰</button>
      <ul class="nav-links">
        <li><a href="../../index.html">Inicio</a></li>
        <li><a href="../../noticias.html">Noticias</a></li>
        <li><a href="../../documentos.html">Documentos</a></li>
        <li><a href="../../contacto.html">Contacto</a></li>
      </ul>
    </nav>
  </header>

  <main>
    <div class="article-header">
      <div class="container">
        <h1>Ejemplo de Noticia Sindical</h1>
        <div class="article-meta">
          <span>13 de junio de 2026</span>
        </div>
      </div>
    </div>

    <article class="article-content">
      <a href="../../noticias.html" class="back-link">← Volver a noticias</a>
      <p>Esta es una noticia de ejemplo para demostrar el funcionamiento del sistema de noticias de La Intersindical VDD.</p>
      <p>El sistema permite generar automáticamente páginas de noticias a partir de documentos PDF, extrayendo el texto y las imágenes contenidas en ellos.</p>
      <p>Para crear una nueva noticia, simplemente ejecuta el script de generación con el comando:</p>
      <pre><code>python generar.py "mi-noticia.pdf" --fecha 2026-06-13 --slug mi-noticia</code></pre>
    </article>
  </main>

  <footer>
    <div class="container">
      <div class="footer-bottom">
        <p>&copy; 2026 La Intersindical VDD. Todos los derechos reservados.</p>
      </div>
    </div>
  </footer>

  <script src="../../js/main.js"></script>
</body>
</html>
```

- [ ] **Step 3: Create documentos.json**

```json
[
  {
    "title": "Convenio Colectivo Ejemplo",
    "description": "Convenio colectivo de ejemplo para demostración",
    "date": "2026-01-15",
    "file": "convenio-ejemplo.pdf",
    "tipo": "convenios"
  }
]
```

- [ ] **Step 4: Commit**

```bash
git add noticias/noticias.json noticias/ejemplo-noticia/ documentos/documentos.json
git commit -m "feat: add example news data and template"
```

---

### Task 13: Create Python Script

**Files:**
- Create: `generar.py`

- [ ] **Step 1: Create generar.py**

```python
#!/usr/bin/env python3
"""
Script para generar noticias y documentos a partir de PDFs.
Uso:
  python generar.py "titulo.pdf" --fecha 2024-01-15 --slug mi-noticia
  python generar.py --documento "Guia Laboral.pdf" --tipo guias
"""

import argparse
import json
import os
import re
from datetime import datetime
from pathlib import Path

try:
    import pdfplumber
except ImportError:
    print("Error: pdfplumber no está instalado. Ejecuta: pip install pdfplumber")
    exit(1)

try:
    from bs4 import BeautifulSoup
except ImportError:
    print("Error: beautifulsoup4 no está instalado. Ejecuta: pip install beautifulsoup4")
    exit(1)


def extract_text_from_pdf(pdf_path):
    """Extrae texto de un archivo PDF."""
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""
            text += "\n"
    return text.strip()


def extract_images_from_pdf(pdf_path, output_dir):
    """Extrae imágenes de un archivo PDF."""
    images = []
    os.makedirs(output_dir, exist_ok=True)
    
    with pdfplumber.open(pdf_path) as pdf:
        for page_num, page in enumerate(pdf.pages):
            for img_num, img in enumerate(page.images):
                # Las imágenes en pdfplumber son diccionarios con información de posición
                # Para extraer imágenes reales, necesitaríamos usar otra librería
                pass
    
    return images


def create_article_html(title, date, content, images, output_path):
    """Crea la página HTML del artículo."""
    html_template = f"""<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} - La Intersindical VDD</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="../../css/style.css">
  <style>
    .article-header {{
      padding: 6rem 0 2rem;
      background: var(--secondary);
      color: var(--bg-light);
      text-align: center;
    }}
    .article-meta {{
      margin-bottom: 1rem;
      opacity: 0.8;
    }}
    .article-content {{
      max-width: 800px;
      margin: 0 auto;
      padding: 3rem 1rem;
    }}
    .article-content img {{
      width: 100%;
      height: auto;
      border-radius: 8px;
      margin: 1.5rem 0;
    }}
    .back-link {{
      display: inline-block;
      margin-bottom: 2rem;
      color: var(--primary);
    }}
  </style>
</head>
<body>
  <header class="scrolled">
    <nav class="container">
      <a href="../../index.html" class="logo">
        <img src="../../img/logo.png" alt="La Intersindical VDD">
      </a>
      <button class="menu-toggle" aria-label="Menú">☰</button>
      <ul class="nav-links">
        <li><a href="../../index.html">Inicio</a></li>
        <li><a href="../../noticias.html">Noticias</a></li>
        <li><a href="../../documentos.html">Documentos</a></li>
        <li><a href="../../contacto.html">Contacto</a></li>
      </ul>
    </nav>
  </header>

  <main>
    <div class="article-header">
      <div class="container">
        <h1>{title}</h1>
        <div class="article-meta">
          <span>{format_date_es(date)}</span>
        </div>
      </div>
    </div>

    <article class="article-content">
      <a href="../../noticias.html" class="back-link">← Volver a noticias</a>
      {content}
    </article>
  </main>

  <footer>
    <div class="container">
      <div class="footer-bottom">
        <p>&copy; 2026 La Intersindical VDD. Todos los derechos reservados.</p>
      </div>
    </div>
  </footer>

  <script src="../../js/main.js"></script>
</body>
</html>"""
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html_template)


def format_date_es(date_string):
    """Formatea una fecha en español."""
    months = {
        1: 'enero', 2: 'febrero', 3: 'marzo', 4: 'abril',
        5: 'mayo', 6: 'junio', 7: 'julio', 8: 'agosto',
        9: 'septiembre', 10: 'octubre', 11: 'noviembre', 12: 'diciembre'
    }
    date = datetime.strptime(date_string, '%Y-%m-%d')
    return f"{date.day} de {months[date.month]} de {date.year}"


def text_to_html(text):
    """Convierte texto plano a HTML con párrafos."""
    paragraphs = text.split('\n\n')
    html = ''
    for p in paragraphs:
        p = p.strip()
        if p:
            # Detectar si es un título (línea corta sin punto final)
            if len(p) < 100 and not p.endswith('.'):
                html += f'<h2>{p}</h2>\n'
            else:
                html += f'<p>{p}</p>\n'
    return html


def update_news_json(news_data, news_json_path):
    """Actualiza el archivo noticias.json."""
    if os.path.exists(news_json_path):
        with open(news_json_path, 'r', encoding='utf-8') as f:
            existing = json.load(f)
    else:
        existing = []
    
    # Verificar si ya existe la noticia
    existing_slugs = [n['slug'] for n in existing]
    if news_data['slug'] in existing_slugs:
        # Actualizar existente
        for i, n in enumerate(existing):
            if n['slug'] == news_data['slug']:
                existing[i] = news_data
                break
    else:
        # Añadir nueva
        existing.append(news_data)
    
    # Ordenar por fecha (más reciente primero)
    existing.sort(key=lambda x: x['date'], reverse=True)
    
    with open(news_json_path, 'w', encoding='utf-8') as f:
        json.dump(existing, f, ensure_ascii=False, indent=2)


def generate_news(pdf_path, date, slug):
    """Genera una noticia a partir de un PDF."""
    pdf_path = Path(pdf_path)
    if not pdf_path.exists():
        print(f"Error: No se encontró el archivo {pdf_path}")
        return
    
    # Extraer texto
    text = extract_text_from_pdf(pdf_path)
    if not text:
        print("Error: No se pudo extraer texto del PDF")
        return
    
    # Usar nombre del archivo como título si no se especifica
    title = pdf_path.stem.replace('-', ' ').replace('_', ' ').title()
    
    # Convertir texto a HTML
    content = text_to_html(text)
    
    # Crear directorio de la noticia
    news_dir = Path('noticias') / slug
    news_dir.mkdir(parents=True, exist_ok=True)
    
    # Crear imagen placeholder
    img_dir = news_dir / 'img'
    img_dir.mkdir(exist_ok=True)
    
    # Crear HTML del artículo
    article_path = news_dir / 'index.html'
    create_article_html(title, date, content, [], article_path)
    
    # Actualizar noticias.json
    news_data = {
        'slug': slug,
        'title': title,
        'date': date,
        'excerpt': text[:200] + '...' if len(text) > 200 else text,
        'image': 'img/placeholder.jpg',
        'content': content
    }
    update_news_json(news_data, Path('noticias') / 'noticias.json')
    
    print(f"Noticia generada: {article_path}")
    print(f"JSON actualizado: noticias/noticias.json")


def add_document(pdf_path, doc_type):
    """Añade un documento a la lista."""
    pdf_path = Path(pdf_path)
    if not pdf_path.exists():
        print(f"Error: No se encontró el archivo {pdf_path}")
        return
    
    # Copiar PDF a directorio de documentos
    docs_dir = Path('documentos') / doc_type
    docs_dir.mkdir(parents=True, exist_ok=True)
    
    import shutil
    dest = docs_dir / pdf_path.name
    shutil.copy2(pdf_path, dest)
    
    # Actualizar documentos.json
    docs_json = Path('documentos') / 'documentos.json'
    if docs_json.exists():
        with open(docs_json, 'r', encoding='utf-8') as f:
            existing = json.load(f)
    else:
        existing = []
    
    doc_data = {
        'title': pdf_path.stem.replace('-', ' ').replace('_', ' ').title(),
        'description': f'Documento de tipo {doc_type}',
        'date': datetime.now().strftime('%Y-%m-%d'),
        'file': f'{doc_type}/{pdf_path.name}',
        'tipo': doc_type
    }
    
    existing.append(doc_data)
    
    with open(docs_json, 'w', encoding='utf-8') as f:
        json.dump(existing, f, ensure_ascii=False, indent=2)
    
    print(f"Documento añadido: {dest}")
    print(f"JSON actualizado: documentos/documentos.json")


def main():
    parser = argparse.ArgumentParser(description='Generar noticias y documentos desde PDFs')
    parser.add_argument('pdf', nargs='?', help='Archivo PDF a procesar')
    parser.add_argument('--fecha', help='Fecha de la noticia (YYYY-MM-DD)')
    parser.add_argument('--slug', help='Slug para la URL de la noticia')
    parser.add_argument('--documento', help='PDF a añadir como documento')
    parser.add_argument('--tipo', default='general', help='Tipo de documento')
    
    args = parser.parse_args()
    
    if args.documento:
        add_document(args.documento, args.tipo)
    elif args.pdf:
        if not args.fecha:
            args.fecha = datetime.now().strftime('%Y-%m-%d')
        if not args.slug:
            args.slug = Path(args.pdf).stem.lower().replace(' ', '-').replace('_', '-')
        generate_news(args.pdf, args.fecha, args.slug)
    else:
        parser.print_help()


if __name__ == '__main__':
    main()
```

- [ ] **Step 2: Commit**

```bash
git add generar.py
git commit -m "feat: add Python script for PDF to HTML conversion"
```

---

### Task 14: Final Testing and Cleanup

**Files:**
- All files

- [ ] **Step 1: Test the structure**

```bash
# Verificar que todos los archivos existen
ls -la index.html noticias.html noticia.html documentos.html contacto.html
ls -la css/style.css js/main.js
ls -la noticias/noticias.json documentos/documentos.json
ls -la generar.py requirements.txt
```

- [ ] **Step 2: Test Python script syntax**

```bash
python -m py_compile generar.py
```

- [ ] **Step 3: Final commit**

```bash
git add -A
git commit -m "feat: complete web structure with all pages and scripts"
```

---

## Plan Summary

| Task | Description | Files |
|------|-------------|-------|
| 1 | Project Setup | requirements.txt, directories |
| 2 | Base CSS Styles | css/style.css |
| 3 | Header/Nav Styles | css/style.css |
| 4 | Hero Section Styles | css/style.css |
| 5 | News/Footer Styles | css/style.css |
| 6 | Create index.html | index.html |
| 7 | Create JavaScript | js/main.js |
| 8 | Create noticias.html | noticias.html |
| 9 | Create Article Template | noticia.html |
| 10 | Create documentos.html | documentos.html |
| 11 | Create contacto.html | contacto.html |
| 12 | Example News Data | noticias.json, ejemplo-noticia |
| 13 | Python Script | generar.py |
| 14 | Final Testing | All files |
