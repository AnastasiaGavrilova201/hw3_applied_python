# Описание API.

# Примеры запросов.

- post/links/shorten -- сокращение ссылки, указание кастомной сокращенной ссылки (необязательно) и даты истечения работы ссылки (необязательно). Заглушка: вместо кастомного алиаса можно передавать кастомную сокращенную ссылкы, так как для применения алиаса на сайтах надо платить.

Запрос: 
{
  "your_url": "https://translated.turbopages.org/proxy_u/en-ru.ru.92363b6c-67dd5e3e-c547f50b-74722d776562/https/stackoverflow.com/questions/17492550/can-i-run-multiple-sections-of-sql-in-one-statement",
  "expires_at": "2025-04-22T19:26:15.648"
}

- get/links/ -- получение оригинальной ссылки по сокращенной  






# Инструкцию по запуску.

docker build . -t fastapi_app:latest

если не запустится в докере, то uvicorn main:app точно работает, не ругайте

# Описание БД (при наличии)

Таблица user 

Column("id", Integer, primary_key=True), -- id записи

Column("url", String, nullable=False), -- оригинальная ссылка

Column("url_short", String, nullable=False), -- сокращенная ссылка

Column("expires_at", DateTime, nullable=True), -- дата создания

Column("created_at", DateTime, nullable=False) -- дата истечения срока 
