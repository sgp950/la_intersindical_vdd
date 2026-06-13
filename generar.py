#!/usr/bin/env python3
"""
Script per generar notícies i documents a partir de PDFs.
Ús:
  python generar.py "titol.pdf" --data 2024-01-15 --slug mi-noticia
  python generar.py --document "Guia Laboral.pdf" --tipus guies
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
    print("Error: pdfplumber no està instal·lat. Executa: pip install pdfplumber")
    exit(1)

try:
    from bs4 import BeautifulSoup
except ImportError:
    print("Error: beautifulsoup4 no està instal·lat. Executa: pip install beautifulsoup4")
    exit(1)


def extract_text_from_pdf(pdf_path):
    """Extreu text d'un fitxer PDF."""
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""
            text += "\n"
    return text.strip()


def extract_images_from_pdf(pdf_path, output_dir):
    """Extreu imatges d'un fitxer PDF."""
    images = []
    os.makedirs(output_dir, exist_ok=True)

    with pdfplumber.open(pdf_path) as pdf:
        for page_num, page in enumerate(pdf.pages):
            for img_num, img in enumerate(page.images):
                # Les imatges en pdfplumber són diccionaris amb informació de posició
                # Per extreure imatges reals, necessitaríem usar una altra llibreria
                pass

    return images


def create_article_html(title, date, content, images, output_path):
    """Crea la pàgina HTML de l'article."""
    html_template = f"""<!DOCTYPE html>
<html lang="ca">
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
        <li><a href="../../index.html">Inici</a></li>
        <li><a href="../../noticias.html">Notícies</a></li>
        <li><a href="../../documentos.html">Documents</a></li>
        <li><a href="../../contacto.html">Contacte</a></li>
      </ul>
    </nav>
  </header>

  <main>
    <div class="article-header">
      <div class="container">
        <h1>{title}</h1>
        <div class="article-meta">
          <span>{format_date_ca(date)}</span>
        </div>
      </div>
    </div>

    <article class="article-content">
      <a href="../../noticias.html" class="back-link">← Tornar a les Notícies</a>
      {content}
    </article>
  </main>

  <footer>
    <div class="container">
      <div class="footer-bottom">
        <p>&copy; 2026 La Intersindical VDD. Tots els drets reservats.</p>
      </div>
    </div>
  </footer>

  <script src="../../js/main.js"></script>
</body>
</html>"""
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html_template)


def format_date_ca(date_string):
    """Formata una data en català."""
    months = {
        1: 'gener', 2: 'febrer', 3: 'març', 4: 'abril',
        5: 'maig', 6: 'juny', 7: 'juliol', 8: 'agost',
        9: 'setembre', 10: 'octubre', 11: 'novembre', 12: 'desembre'
    }
    date = datetime.strptime(date_string, '%Y-%m-%d')
    return f"{date.day} de {months[date.month]} de {date.year}"


def text_to_html(text):
    """Converteix text pla a HTML amb paràgrafs."""
    paragraphs = text.split('\n\n')
    html = ''
    for p in paragraphs:
        p = p.strip()
        if p:
            # Detectar si és un títol (línia curta sense punt final)
            if len(p) < 100 and not p.endswith('.'):
                html += f'<h2>{p}</h2>\n'
            else:
                html += f'<p>{p}</p>\n'
    return html


def update_news_json(news_data, news_json_path):
    """Actualitza el fitxer noticias.json."""
    if os.path.exists(news_json_path):
        with open(news_json_path, 'r', encoding='utf-8') as f:
            existing = json.load(f)
    else:
        existing = []

    # Verificar si ja existeix la notícia
    existing_slugs = [n['slug'] for n in existing]
    if news_data['slug'] in existing_slugs:
        # Actualitzar existent
        for i, n in enumerate(existing):
            if n['slug'] == news_data['slug']:
                existing[i] = news_data
                break
    else:
        # Afegir nova
        existing.append(news_data)

    # Ordenar per data (més recent primer)
    existing.sort(key=lambda x: x['date'], reverse=True)

    with open(news_json_path, 'w', encoding='utf-8') as f:
        json.dump(existing, f, ensure_ascii=False, indent=2)


def generate_news(pdf_path, date, slug):
    """Genera una notícia a partir d'un PDF."""
    pdf_path = Path(pdf_path)
    if not pdf_path.exists():
        print(f"Error: No s'ha trobat el fitxer {pdf_path}")
        return

    # Extreure text
    text = extract_text_from_pdf(pdf_path)
    if not text:
        print("Error: No s'ha pogut extreure text del PDF")
        return

    # Usar nom del fitxer com a títol si no s'especifica
    title = pdf_path.stem.replace('-', ' ').replace('_', ' ').title()

    # Convertir text a HTML
    content = text_to_html(text)

    # Crear directori de la notícia
    news_dir = Path('noticias') / slug
    news_dir.mkdir(parents=True, exist_ok=True)

    # Crear imatge placeholder
    img_dir = news_dir / 'img'
    img_dir.mkdir(exist_ok=True)

    # Crear HTML de l'article
    article_path = news_dir / 'index.html'
    create_article_html(title, date, content, [], article_path)

    # Actualitzar noticias.json
    news_data = {
        'slug': slug,
        'title': title,
        'date': date,
        'excerpt': text[:200] + '...' if len(text) > 200 else text,
        'image': 'img/placeholder.jpg',
        'content': content
    }
    update_news_json(news_data, Path('noticias') / 'noticias.json')

    print(f"Notícia generada: {article_path}")
    print(f"JSON actualitzat: noticias/noticias.json")


def add_document(pdf_path, doc_type):
    """Afegeix un document a la llista."""
    pdf_path = Path(pdf_path)
    if not pdf_path.exists():
        print(f"Error: No s'ha trobat el fitxer {pdf_path}")
        return

    # Copiar PDF al directori de documents
    docs_dir = Path('documentos') / doc_type
    docs_dir.mkdir(parents=True, exist_ok=True)

    import shutil
    dest = docs_dir / pdf_path.name
    shutil.copy2(pdf_path, dest)

    # Actualitzar documentos.json
    docs_json = Path('documentos') / 'documentos.json'
    if docs_json.exists():
        with open(docs_json, 'r', encoding='utf-8') as f:
            existing = json.load(f)
    else:
        existing = []

    doc_data = {
        'title': pdf_path.stem.replace('-', ' ').replace('_', ' ').title(),
        'description': f'Document de tipus {doc_type}',
        'date': datetime.now().strftime('%Y-%m-%d'),
        'file': f'{doc_type}/{pdf_path.name}',
        'tipo': doc_type
    }

    existing.append(doc_data)

    with open(docs_json, 'w', encoding='utf-8') as f:
        json.dump(existing, f, ensure_ascii=False, indent=2)

    print(f"Document afegit: {dest}")
    print(f"JSON actualitzat: documentos/documentos.json")


def main():
    parser = argparse.ArgumentParser(description='Generar notícies i documents des de PDFs')
    parser.add_argument('pdf', nargs='?', help='Fitxer PDF a processar')
    parser.add_argument('--data', help='Data de la notícia (YYYY-MM-DD)')
    parser.add_argument('--slug', help='Slug per a la URL de la notícia')
    parser.add_argument('--document', help='PDF a afegir com a document')
    parser.add_argument('--tipus', default='general', help='Tipus de document')
    
    args = parser.parse_args()

    if args.document:
        add_document(args.document, args.tipus)
    elif args.pdf:
        if not args.data:
            args.data = datetime.now().strftime('%Y-%m-%d')
        if not args.slug:
            args.slug = Path(args.pdf).stem.lower().replace(' ', '-').replace('_', '-')
        generate_news(args.pdf, args.data, args.slug)
    else:
        parser.print_help()


if __name__ == '__main__':
    main()
