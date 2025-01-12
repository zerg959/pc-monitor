![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E)
![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)


Простая десктопная утилита для мониторинга производительности компьютера.
1. Установить python, pip
2. Перейти в директорию 'pc-monitor-main' (cd pc-monitor-main)
3. Создать и запустить виртуальное окружение:
  - python3 -m venv venv
  - source venv/bin/activate
4. Установить зависимости из requirements.txt:
  - pip install -r requirements.txt
5. Запустить сервер Flask:
  - python3 app.py
6. Приложение запустится на localhost.
  - по умолчанию, параметры обновляются каждую секунду, данные выводятся на страницу
  - при нажатии на "Start Recording" создается БД Sqlite, в которую записываются параметры PCб и стартует таймер, отражающий время записи в БД.
  - интервал таймера можно задавать с помощью "Set Interval".
  - по кнопке "Stop Recording" запись в БД останавливается, таймер обнуляется.
7. Настроено автоматическое тестирование на github actions изменений при пуше изменений в ветку и пул-реквесте.


