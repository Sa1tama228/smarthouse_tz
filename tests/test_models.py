import pytest
import sqlite3
from models import Database, DeviceModel

@pytest.fixture
def db():
    db = Database(':memory:')
    yield db
    db.connection.close()

def test_create_tables(db):
    cursor = db.connection.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='devices';")
    assert cursor.fetchone() is not None

def test_add_device(db):
    device = DeviceModel(name='Light', state=False)
    db.add_device(device)
    devices = db.get_all_devices()
    assert len(devices) == 1
    assert devices[1].name == 'Light'
    assert devices[1].state is False

def test_update_device_state(db):
    device = DeviceModel(name='Light', state=False)
    db.add_device(device)
    db.update_device_state(1, True)
    devices = db.get_all_devices()
    assert devices[1].state is True
