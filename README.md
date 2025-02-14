![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E)
![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)


Simple web-app PC-monitor.
1. Install python, pip
2. Open root folder 'pc-monitor-main' (cd pc-monitor-main)
3. Create and start virtual environment:
  - python3 -m venv venv
  - source venv/bin/activate
4. Install requierements из requirements.txt:
  - pip install -r requirements.txt
    Start Flask server:
  - python3 app.py
    App will start on localhost.
  - Default update interval is 1 sec, data shows on the page
  - Button "Start Recording" creates DB Sqlite where data saved and timer starts. Is shows timestamps in DB.
  - Interaval can be set by "Set Interval" button.
  - Second tap on "Stop Recording" stopped recording to the DB, timer canceled to 0.
7. CI/CD on github actions (on push and pull requests).
<hr><br>

![Главная](pc-monitor-main/static/screenshots/pc-monitor.JPG)
![Данные](pc-monitor-main/static/screenshots/pc-monitor-db-data.JPG)
![Тесты](pc-monitor-main/static/screenshots/pc-monitor-tests.JPG)


