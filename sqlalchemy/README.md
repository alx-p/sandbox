# sqlalchemy
За основу взята схема данных официальной демо базы данных от PostgresPro: https://postgrespro.com/community/demodb

Разворачивается только схема данных. Если нужны данные, то их необходимо "подгузить" из дампа, который можно скачать по ссылке выше.

Запуск проекта:
```
sudo docker compose up --build
```

Увидеть ответ можно тут:
```
http://localhost:5003/airplanes
```