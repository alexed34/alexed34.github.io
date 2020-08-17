import glob
import json
import os
from http.server import HTTPServer, SimpleHTTPRequestHandler

from jinja2 import Environment, FileSystemLoader, select_autoescape
from more_itertools import chunked


def delete_unnecessary_files(pages):
    all_pages = glob.glob('pages/index*.html')
    for page in all_pages:
        name_page = page.split('\\')[-1]
        if name_page not in pages:
            os.remove(page)

def writer_pages(parts, template, quantity_pages):
    pages = []
    for i, part in enumerate(parts, 1):
        rendered_page = template.render(books=part, pages=quantity_pages, index=i)
        filename = f'index{i}.html'
        with open(f'pages/{filename}', 'w', encoding="utf8") as file:
            file.write(rendered_page)
        pages.append(filename)
        if i == 1:
            with open(f'index.html', 'w', encoding="utf8") as file:
                file.write(rendered_page)
    return pages


def main():
    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html'])
    )

    with open('static/data.json', 'r', encoding='utf8') as f:
        books_json = f.read()

    books = json.loads(books_json)
    parts = list(chunked(books, 10))
    quantity_pages = len(parts)
    os.makedirs('pages', exist_ok=True)
    template = env.get_template('template.html')

    pages = writer_pages(parts, template, quantity_pages)

    delete_unnecessary_files(pages)

    server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
    server.serve_forever()


if __name__ == '__main__':
    main()
