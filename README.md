## Библиотека научной фантастики

### Описание

Библиотека содержит около 100 книг в жанре научной фантасктики. Формат книг 'txt'.

Онлайн версия находится по адресу 

Книги взяты из библиотеки [tululu.org](http://tululu.org/)

### Установка


* Создайте виртуальное окружение 
    
* Скачайте [скрипт библиотеки](https://github.com/alexed34/devman-api-3/archive/master.zip) c github.com

* Разархивируйте файл с скриптом библиотеки в вашу папку c виртуальным окружением

* Установите библиотеки командой `pip install -r requirements.txt`

### Данные скрипта

Все материалы находятся в папке `static`
* `static/books` - книги
* `static/images` - обложки к  книгам
* `static/data.json` - json файл с информацией о книгах

### Запуск скрипта

* В консоле перейдите в папку layout-4
* запустите файл render_website.py `(venv) C:\Users\asus\PycharmProjects\layout-4>render_website.py`
* Запустится код 
```
[I 200601 13:29:58 server:296] Serving on http://127.0.0.1:5500
[I 200601 13:29:58 handlers:62] Start watching changes
[I 200601 13:29:58 handlers:64] Start detecting changes
[W 200601 13:29:59 web:2250] 404 GET / (127.0.0.1) 2.00ms
```
* Откройте в браузере ссылку (http://127.0.0.1:8000/pages/index1.html)

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).



