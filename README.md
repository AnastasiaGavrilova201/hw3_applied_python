# Описание API.

# Примеры запросов.

- post/links/shorten -- сокращение ссылки, указание кастомной сокращенной ссылки (необязательно) и даты истечения работы ссылки (необязательно). Заглушка: вместо кастомного алиаса можно передавать кастомную сокращенную ссылкы, так как для применения алиаса на сайтах надо платить.

Запрос: 

{

  "your_url": "https://translated.turbopages.org/proxy_u/en-ru.ru.92363b6c-67dd5e3e-c547f50b-74722d776562/https/stackoverflow.com/questions/17492550/can-i-run-multiple-sections-of-sql-in-one-statement",
  
  "expires_at": "2025-04-22T19:26:15.648"
  
}

![image](https://github.com/user-attachments/assets/771285dd-e300-425e-b177-f10aae980680)

Ответ: 

![image](https://github.com/user-attachments/assets/52620142-2573-48db-950f-e07d37e3a2c7)

- get/links/{short_code} -- получение оригинальной ссылки по сокращенной ссылке

-![image](https://github.com/user-attachments/assets/4d900c1a-1712-4510-adc2-8af8ccc3958c)

- put/links/{url} -- обновление сокращенной ссылки по оригинальной ссылке
  
![image](https://github.com/user-attachments/assets/0204e8b5-6cea-47c3-a0db-742699aae985)

- get/links/stats -- статистика по ссылке

![image](https://github.com/user-attachments/assets/15b8fed8-1865-40b6-8870-07fb28e612d0)

- get/links/search -- поиск сокращенной ссылки по оригинальной
- 
![image](https://github.com/user-attachments/assets/1d2cc09b-7cdc-43df-b96d-558b5e2de0f4)

- get/links/show_expired_url -- просмотр "просроченных" ссылок
- 
 ![image](https://github.com/user-attachments/assets/f0bad6d8-f11c-42ae-8538-b522e5fa0437)

- delete/links/{short_code} -- удаление связи по сокращенной ссылке

 ![image](https://github.com/user-attachments/assets/1fc7067c-0fab-470e-bfaa-8fed695861d9)



# Инструкцию по запуску.

docker build . -t fastapi_app:latest

если не запустится в докере, то uvicorn main:app точно работает, не ругайте

в .env необходимо прописать значения для подключения к бд:

DB_USER=

DB_PASS=

DB_HOST=

DB_PORT=

DB_NAME=

Для запуска тестов введите pytest. % покрытия в ./htmlcov/index.html

![image](https://github.com/user-attachments/assets/3e5aac3e-70fb-4c14-80d4-ed179588f7be)

![image](https://github.com/user-attachments/assets/7a744c21-bedc-477f-8d6b-690f68772e7e)

![image](https://github.com/user-attachments/assets/785145fe-45c5-43b8-8569-8e9ca2d762b2)


# Описание БД (при наличии)

Таблица user 

Column("id", Integer, primary_key=True), -- id записи

Column("url", String, nullable=False), -- оригинальная ссылка

Column("url_short", String, nullable=False), -- сокращенная ссылка

Column("expires_at", DateTime, nullable=True), -- дата создания

Column("created_at", DateTime, nullable=False) -- дата истечения срока 
