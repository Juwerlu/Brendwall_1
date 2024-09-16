# Тестовое задание для собеседования в компанию "Brendwall"

## Описание проекта  

Django-приложение, которое состоит из двух частей:

1. API для работы с продуктами (создание и получение списка).  
2. Страница на HTML с использованием JavaScript для отправки данных на API и отображения продуктов.  

## Как запустить проект:  

Клонировать репозиторий:  

    git clone git@github.com:Juwerlu/Brendwall.git
    
Перейти в него в командной строке:  

    cd Brendwall
	
Cоздать и активировать виртуальное окружение:  

    python3 -m venv venv

    source venv/bin/activate

Установить зависимости из файла requirements.txt:  

    python3 -m pip install --upgrade pip  
    
    pip install -r requirements.txt

Выполнить миграции:  

    python3 manage.py migrate
    
Запустить проект:  

    python3 manage.py runserver
