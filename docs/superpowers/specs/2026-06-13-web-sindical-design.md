# Diseño Web La Intersindical VDD

## Resumen

Web estática para información sindical (noticias, documentos, contacto) con sistema de generación automática de noticias desde PDFs.

## Objetivo

- Web estática con HTML, CSS y JavaScript
- Estilo serio inspirado en https://laintersindical.cat/
- Sistema para subir PDFs y generar noticias automáticamente
- Diseño responsive para móviles y tablets

## Estructura de archivos

```
la_intersindical_vdd/
├── index.html              # Página de inicio
├── noticias.html           # Listado de noticias
├── noticia.html            # Plantilla para artículos individuales
├── documentos.html         # Sección de documentos
├── contacto.html           # Contacto
├── css/
│   └── style.css           # Estilos principales
├── js/
│   └── main.js             # JavaScript (navegación, listado noticias)
├── img/                    # Imágenes del sitio
├── noticias/
│   ├── noticias.json       # Datos de todas las noticias
│   └── [slug]/             # Carpeta por noticia
│       ├── index.html      # Artículo completo
│       └── img/            # Imágenes de la noticia
├── pdfs/                   # PDFs originales
├── documentos/             # Documentos del sindicato
└── generar.py              # Script de conversión PDF→HTML
```

## Diseño visual

### Colores
- Primario: #e5352c (rojo - acentos, botones)
- Secundario: #1a1a1a (oscuro - header, footer)
- Fondo: #ffffff (blanco - contenido)
- Texto: #333333 (gris oscuro)

### Fuentes
- Principal: Poppins (Google Fonts)
- Títulos: Poppins Bold
- Cuerpo: Poppins Regular

### Header
- Logo a la izquierda
- Menú horizontal a la derecha
- Fondo transparente que se vuelve blanco al hacer scroll

### Footer
- Fondo oscuro (#1a1a1a)
- 4 columnas: Info, Recursos, Legales, Contacto
- Iconos sociales abajo

## Secciones del sitio

### Inicio (index.html)
- Hero con imagen parallax y overlay oscuro
- Título principal y botones de acción
- Últimas noticias destacadas

### Noticias (noticias.html)
- Tarjetas con imagen, título, fecha y resumen
- Orden cronológico (más recientes primero)
- Botón "Leer más" que enlaza al artículo completo

### Artículo individual (noticia.html)
- Título grande arriba
- Fecha
- Imágenes del PDF insertadas en el contenido
- Texto completo formateado
- Botón volver al listado

### Documentos (documentos.html)
- Lista de documentos PDF disponibles para descargar
- Cada documento muestra: título, descripción, fecha, botón descargar
- Organizados en secciones

### Contacto (contacto.html)
- Información del sindicato (nombre, dirección, teléfono, email)
- Mapa embebido (OpenStreetMap)
- Formulario de contacto simple (nombre, email, mensaje, enviar)

## Sistema de noticias (generar.py)

### Uso
```bash
# Generar noticia desde PDF
python generar.py "titulo.pdf" --fecha 2024-01-15 --slug mi-noticia

# Añadir documento
python generar.py --documento "Guia Laboral.pdf" --tipo guias
```

### Funcionamiento
1. Extrae texto del PDF usando pdfplumber
2. Extrae imágenes del PDF y las guarda en carpeta de la noticia
3. Genera la página HTML del artículo completo
4. Actualiza noticias.json con el nuevo artículo
5. Actualiza documentos.json si se añade un documento

### Dependencias Python
- pdfplumber (extracción de texto e imágenes)
- beautifulsoup4 (procesamiento HTML)

## Responsive

### Breakpoints
- Desktop: > 980px
- Tablet: 768px - 980px
- Móvil: < 768px

### Comportamiento
- Header: menú colapsa en hamburguesa en móviles
- Noticias: tarjetas se apilan verticalmente
- Documentos: lista simplificada
- Footer: columnas se apilan
