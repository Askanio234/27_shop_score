# Мониторинг KPI для кол-центра

**сценарий:** Нужно вывести на большой монитор в офисе текущий KPI команды менеджеров
основной показатель – максимальное время ожидания еще не обработанных заявок. 
При этом вывод данных должен хорошо смотреться как на большом экране, так и на экране телефона.
для работы скрипта предоставляется функционирующая PostgreSQL база данных. 

**функционал:** Максимальное время ожидания еще не обработанных заявок понимается как разница во времени между
текущим моментом и временем создания самого раннего не обработанного заказа, дополнительно выводится также общее количество
необработанных заказов и общее количество заказов, обработанных за текущий день (с 00.00.00 до 23.59.59).
Фоновый цвет меняется в зависимости от времени ожидания: *зеленый* – ожидание не более 7 минут,
*желтый* – ожидание от 7 до 30 минут и *красный* – ожидание более 30 минут.
Модель данных строится с использованием функции automap SQLalchemy [документация](http://docs.sqlalchemy.org/en/latest/orm/extensions/automap.html)
Страница защищена от индексирования поисковыми ботами с помощью соответствующего meta тега и robots.txt

# Как запустить на localhost:

Перед запуском необходимо установить зависимости из requirements.txt:
```#!bash
pip install -r requirements.txt
```
## Создаем подключение к БД:
для этого создадим переменную окружения ```db_conf```,
и присваиваем ей значение формата
**'postgresql://user:password@host:port/'**

*Для Windows*
```#!bash
SET db_conf=postgresql://user:password@host:port/
```
*Для Linux*
```#!bash
db_conf=postgresql://user:password@host:port/
```

## Запуск серверного скрипта

Запустить локально
```#!bash
python server.py 
```
Затем открыть в браузере [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

Пример, запущенный на [Heroku](https://frozen-headland-34365.herokuapp.com/)

# Цели проекта

Код написан в образовательных целях. Курс веб-разработки – [DEVMAN.org](https://devman.org)
