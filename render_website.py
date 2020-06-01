#from http.server import HTTPServer, SimpleHTTPRequestHandler
from jinja2 import Environment, FileSystemLoader, select_autoescape
import json
from livereload import Server, shell
import os

server = Server()

def on_reload():
    template = env.get_template('template.html')
    for i, part in enumerate(parts, 1):
        rendered_page = template.render(books=part, pages=pages, index=i)
        with open(f'pages/index{i}.html', 'w', encoding="utf8") as file:
            file.write(rendered_page)


env = Environment(
    loader=FileSystemLoader('.'),
    autoescape=select_autoescape(['html'])
)


with open('static/data.json', 'r', encoding='utf8') as f:
    books_json = f.read()



books = json.loads(books_json)
parts = [books[i:i + 10] for i in range(0, len(books), 10)]
pages = len(parts)

os.makedirs('pages', exist_ok = True)
on_reload()

server.watch('template.html', on_reload)
# server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
# server.serve_forever()
server.serve(root='.')
