# YamDB project(but with Docker).

## Агрегатор произведений и рецензий к ним.

### Инструкция к установке:
1. Клонировать репозиторий 
```
git clone git@github.com:SowaSova/infra_sp2.git
```
2. Создать файл .env в директории инфра и заполнить его данными ниже

  ```
  nano infra/.env
```

>     SECRET_KEY=
>     DB_ENGINE= 
>     DB_NAME= 
>     POSTGRES_USER= 
>     POSTGRES_PASSWORD= 
>     DB_HOST= 
>     DB_PORT= 
>     EMAIL_USERNAME=
>     EMAIL_PASSWORD=

3. Инициализировать контейнер в директории ***infra/***
```
cd infra/ ; docker-compose build ; docker-compose up -d
```
4. Провести миграции, создать суперюзера и собрать статику
```
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser
docker-compose exec web python manage.py collectstatic --no-input
```
5. Админка проекта доступна [здесь](http://localhost/admin/). Функционал API описывается [здесь](http://localhost/redoc/).
6. Установить фикстуры
```
docker-compose exec web python manage.py shell
>>> from django.contrib.contenttypes.models import ContentType
>>> ContentType.objects.all().delete()
>>> quit()
docker-compose exec web python manage.py loaddata fixtures/fixtures.json
```
7. Для остановки контейнера 
```
docker-compose down
```
