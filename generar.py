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
