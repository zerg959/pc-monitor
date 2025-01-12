from flask import Flask, render_template, jsonify
import psutil
import time

import db_control


app = Flask(__name__)


is_recording = False  # Flag to control recording status


def get_sys_info():
    cpu_percentage = psutil.cpu_percent()
    ram = psutil.virtual_memory()
    disk = psutil.disk_usage('/')
    return {
        'cpu_percent': cpu_percentage,
        'ram_percent': ram.percent,
        'ram_used': ram.used / (1024**3),
        'ram_total': ram.total / (1024**3),
        'disk_percent': disk.percent,
        'disk_used': disk.used / (1024**3),
        'disk_total': disk.total / (1024**3),
        'time': time.strftime("%Y-%m-%d %H:%M:%S")
    }


@app.route('/')
def index():
    sys_info = get_sys_info()
    return render_template(
        "index.html",
        sys_info=sys_info,
        is_recording=is_recording
        )


@app.route('/data')
def data():
    sys_info = get_sys_info()
    global is_recording
    if is_recording:
        db_control.insert_sys_data(sys_info)
    return jsonify(sys_info)

@app.route('/switch_recording', methods=['POST'])
def switch_recording():
    global is_recording
    is_recording = not is_recording
    return jsonify({'is_recording': is_recording})

@app.route('/db_records')
def data_records():
    rows = db_control.db_records_list()
    return render_template("data_records.html", rows=rows)


# if __name__ == '__main__':
#     app.run(host='localhost', debug=True)
