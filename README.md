# Тестовое задание Middle-Backend Python

### Как развернуть
- docker-compose build
- docker-compose up -d --build

### Описание
Базовая структура:
- Пользователи (Логин, Полное имя, Пароль)
- Задачи ([ID исполнителя/ей], Название задачи, Описание задачи, Дата завершения задачи

### Что реализовано
- JWT авторизация
- Open API спецификация, с возможностью ручного взаимодействия (e.g., Swagger)
- Пагинатор для списков данных

### Методы (см.`/doc`):

- Регистрация пользователя
- Авторизация пользователя
- Добавление новой задачи
- Изменение задачи
- Удаление задачи
- Список задач
- Список задач, созданных текущим пользователем


# Частично реализовано
- Тесты на регистрацию/авторизацию
- Тесты на получение/обновление токена




		
