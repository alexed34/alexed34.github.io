import glob
import json
import math
import os
from http.server import HTTPServer, SimpleHTTPRequestHandler

from jinja2 import Environment, FileSystemLoader, select_autoescape
from more_itertools import chunked


def delete_unnecessary_files(add_pages):
    all_pages = glob.glob('pages/index*.html')
    for page in all_pages:
        page_split = page.split('\\')[-1]
        if page_split not in add_pages:
            os.remove(page)

def writer_pages(parts, template, pages):
    add_pages = []
    for i, part in enumerate(parts, 1):
        rendered_page = template.render(books=part, pages=pages, index=i)
        with open(f'pages/index{i}.html', 'w', encoding="utf8") as file:
            file.write(rendered_page)
        add_pages.append(f'index{i}.html')
        if i == 1:
            with open(f'index.html', 'w', encoding="utf8") as file:
                file.write(rendered_page)
    return add_pages


def main():
    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html'])
    )

    with open('static/data.json', 'r', encoding='utf8') as f:
        books_json = f.read()

    books = json.loads(books_json)
    parts = list(chunked(books, 10))
    pages = len(parts)
    os.makedirs('pages', exist_ok=True)
    template = env.get_template('template.html')

    add_pages = writer_pages(parts, template, pages)

    delete_unnecessary_files(add_pages)

    server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
    server.serve_forever()


if __name__ == '__main__':
    main()
