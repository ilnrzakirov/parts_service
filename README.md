# parts_service

Сервис для учета остатка запасных частей на складе, ведение заказов клиентов, регистрации и ведение покупателей

Приложение хранит остаток запасных частей, по запросу возвращает список деталей по группам и производителям. Хранит историю покупок. 


>Переменные окружения прописываются в файле .env

<br/>Установка зависимостей: 

```
pip install -r requirements/requirements.txt
```

<br/>Применить миграции: 

```
make migrate
```
