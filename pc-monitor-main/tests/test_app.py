import pytest
from unittest.mock import patch
from main import app  # get_sys_info, is_recording
import db_control


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.app_context():
        db_control.init_db()
    return app.test_client()


@pytest.fixture
def test_db():
    con = db_control.init_db()
    cur = con.cursor()
    cur.execute('''
        INSERT INTO sys_data (
            cpu_percent,
            ram_percent,
            ram_used,
            ram_total,
            disk_percent,
            disk_used,
            disk_total,
            timestamp
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', (10.0, 50.0, 2.0, 8.0, 60.0, 100.0, 1.0, "2023-11-20 10:00:00"))
    con.commit()
    yield con
    cur.execute('DELETE FROM sys_data')
    con.commit()
    con.close()


def test_index_route(client):
    """
    Checks if the main page exists and returns 200 if ok.
    """
    print("Checks if the main page\
           exists and returns 200 if ok.")
    response = client.get('/')
    assert response.status_code == 200


def test_data_route(client):
    """
    Check if data-dictionary has correct keys and structure.
    """
    print("Check if page 'data' returns 200 and\
          JSON object has correct keys and structure.")
    response = client.get('/data')
    assert response.status_code == 200
    assert response.is_json
    data = response.get_json()
    assert all(
        key in data for key in [
            'cpu_percent',
            'ram_percent',
            'ram_used',
            'ram_total',
            'disk_percent',
            'disk_used',
            'disk_total',
            'time'
            ]
            )


@patch('main.db_control.insert_sys_data')
@patch('main.is_recording', new=True)
def test_data_route_with_recording(mock_insert_sys_data, client):
    """
    Check if route '/data' calls db_control.insert_sys_data,
    when flag is_recording == True.
    """
    print("Check if route '/data calls' db_control.insert_sys_data,\
          when flag is_recording == True.")
    response = client.get('/data')
    assert response.status_code == 200
    assert response.is_json
    data = response.get_json()
    mock_insert_sys_data.assert_called_with(data)


@patch('main.db_control.insert_sys_data')
@patch('main.is_recording', new=False)
def test_data_route_without_recording(mock_insert_sys_data, client):
    """
    Check if route '/data' does not call db_control.insert_sys_data,
    when flag is_recording == False.
    """
    print("Check if route '/data' does not call db_control.insert_sys_data,\
          when flag 'is_recording' == False.")
    response = client.get('/data')
    assert response.status_code == 200
    assert response.is_json
    mock_insert_sys_data.assert_not_called()


def test_switch_recording(client):
    """
    Check if /switch_recording switch status
    "is_recording" and return JSON.
    """
    print("Check if '/switch_recording' switch status\
    'is_recording' and return JSON.")
    response = client.post('/switch_recording')
    assert response.status_code == 200
    assert response.is_json
    data = response.get_json()
    assert data['is_recording'] is True

    response = client.post('/switch_recording')
    assert response.status_code == 200
    assert response.is_json
    data = response.get_json()
    assert data['is_recording'] is False


def test_data_records_route(client, test_db):
    """
    Check if route /db_records returns page with records.
    """
    print("Check if route '/db_records' returns page with records.")
    response = client.get('/db_records')
    assert response.status_code == 200
    rows = db_control.db_records_list()
    assert len(rows) > 0
