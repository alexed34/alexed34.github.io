from http.server import HTTPServer, SimpleHTTPRequestHandler
from jinja2 import Environment, FileSystemLoader, select_autoescape
from more_itertools import chunked
import math
import json
import os


def main():
    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html'])
    )

    with open('static/data.json', 'r', encoding='utf8') as f:
        books_json = f.read()

    books = json.loads(books_json)
    piece_books = math.ceil(len(books) / 10)
    parts = list(chunked(books, piece_books))
    pages = len(parts)
    os.makedirs('pages', exist_ok=True)
    template = env.get_template('template.html')

    for i, part in enumerate(parts, 1):
        rendered_page = template.render(books=part, pages=pages, index=i)

        with open(f'pages/index{i}.html', 'w', encoding="utf8") as file:
            file.write(rendered_page)

    server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
    server.serve_forever()


if __name__ == '__main__':
    main()
