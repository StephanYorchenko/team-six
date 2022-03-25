# team-six-backend

> [![](https://img.shields.io/badge/frontend-Степан%20Юрченко-lightblue)](https://t.me/StephanYorchenko 'telegram')
> [![](https://img.shields.io/badge/backend-Степан%20Денисов-green)](https://t.me/sd_denisoff 'telegram')
> [![](https://img.shields.io/badge/backend-Александр%20Лепинских-orange)](https://t.me/el_nut 'telegram')
> [![](https://img.shields.io/badge/research-Александр%20Петров-blue)](https://t.me/ceezism 'telegram')

## Описание

Использование стандарта OpenAPI для инициации платежей из ERP/CRM-системы клиента

## Стек технологий

#### Backend

- python3.9
- FastAPI

#### Frontend

- React
- HTML5 + CSS3 + JS

## Инструкция по запуску

1. Установите [python3](https://www.python.org/)

2. Склонируйте репозиторий и перейдите в директорию с проектом
   ```bash
   $ git clone https://github.com/StephanYorchenko/team-six-backend.git && cd team-six-backend
   ```

3. Создайте и активируйте виртуальное окружение
   ```bash
   $ virtualenv --python=python3 venv
   $ source venv/bin/activate
   ```

4. Добавьте файл ```settings/.env``` c переменными, заданными согласно формату файла ```settings/.env.example```.

5. Выполните миграции
   ```bash
   $ make migrate
   ```

6. Запустите сервер
   ```bash
   $ make run
   ```

## Справка

Просмотр спецификаций:

- Swagger UI ```/swagger```
- Документация ```/redoc```

Разработано team-six
