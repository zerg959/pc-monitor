1. Установить python, pip
2. Перейти в директорию 'pc-monitor-main' (cd pc-monitor-main)
3. Создать и запустить виртуальное окружение:
  - python3 -m venv venv
  - source venv/bin/activate
4. Установить зависимости из requirements.txt:
  - pip install -r requirements.txt
5. Запустить сервер Flask:
  - python3 app.py
Приложение запустится на localhost, при старте будет создана БД Sqlite.