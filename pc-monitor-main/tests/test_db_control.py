import pytest
import sqlite3
import db_control


@pytest.fixture
def test_db():
    """
    DB fixture.
    """
    print("Check DB possibility of deletion and creation of records")
    con = db_control.init_db()
    yield con
    cur = con.cursor()
    cur.execute('DELETE FROM sys_data')
    con.commit()
    con.close()


def test_init_db():
    """
    Check if db created correct and successfully.
    """
    print("Check if db created correct and successfully.")
    con = db_control.init_db()
    assert isinstance(con, sqlite3.Connection)
    con.close()


def test_insert_sys_data(test_db):
    """
    Check if insertion to DB is correct.
    """
    print("Check if insertion to DB is correct.")
    con = test_db
    test_data = {
        'cpu_percent': 10.0,
        'ram_percent': 50.0,
        'ram_used': 2.0,
        'ram_total': 8.0,
        'disk_percent': 60.0,
        'disk_used': 100.0,
        'disk_total': 1.0,
        'time': '2023-11-20 10:00:00'
    }
    db_control.insert_sys_data(test_data)

    cur = con.cursor()
    cur.execute('SELECT * FROM sys_data')
    rows = cur.fetchall()
    assert len(rows) == 1
    assert rows[0][1:] == (
        10.0, 50.0, 2.0, 8.0, 60.0, 100.0, 1.0, '2023-11-20 10:00:00'
    )


def test_db_records_list(test_db):
    """
    Check if DB return all records.
    """
    print("Check if DB return all records.")
    # con = test_db
    test_data = {
        'cpu_percent': 10.0,
        'ram_percent': 50.0,
        'ram_used': 2.0,
        'ram_total': 8.0,
        'disk_percent': 60.0,
        'disk_used': 100.0,
        'disk_total': 1.0,
        'time': '2023-11-20 10:00:00'
    }
    db_control.insert_sys_data(test_data)
    rows = db_control.db_records_list()
    assert len(rows) == 1
    assert rows[0][1:] == (
        10.0, 50.0, 2.0, 8.0, 60.0, 100.0, 1.0, '2023-11-20 10:00:00'
    )
