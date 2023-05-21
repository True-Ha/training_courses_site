<h2 align="center">Training Courses Site</h2>

### Описание проекта

How it works? --> https://youtu.be/DyaqUyQikZ4

Описание проекта:
- Создание профиля, оплата через тг бота
- Права доступа к контенту только после оплаты
- 
- Удобное создание плана тренировок через админ панель
- Восстановление пароля через почту, смена пароля на сайте
- Доступ к контенту с привязкой к IP
- Просмотр и обновление профиля юзера

**Стек**
- Python >= 3.10
- Django >= 4.1.7
- sqlite3

Установка

pip install requirements.txt

Старт

python manage.py runserver

## Разработка
#### 1) Поставить звездочку)
#### 2) Клонировать репозиторий
git clone https://github.com/True-Ha/training_courses_site.git

#### 3) Создать виртуальное окружение
python -m venv venv

#### 4) Активировать виртуальное окружение
Linux:
source venv/bin/activate
Windows:
./venv/Scripts/activate
#### 5) Устанавливить зависимости:
pip install -r requirements.txt

#### 6) Выполнить команду для выполнения миграций
python manage.py migrate

#### 7) Создать суперпользователя
python manage.py createsuperuser

#### 8) Запустить сервер
python manage.py runserver

#### 9) Ссылки
Сайт http://127.0.0.1:8000/
Админ панель http://127.0.0.1:8000/admin

