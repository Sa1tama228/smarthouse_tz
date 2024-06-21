import sqlite3
'''Основные модели умного дома'''


class DeviceModel:
    def __init__(self, name, state, device_id=None):
        self.device_id = device_id
        self.name = name
        self.state = state
        # настройка девайсов


class Database:
    def __init__(self, db_file):
        self.connection = sqlite3.connect(db_file)
        self.create_tables()

    def create_tables(self):
        with self.connection:
            self.connection.execute(
                "CREATE TABLE IF NOT EXISTS devices (id INTEGER PRIMARY KEY, name TEXT, state BOOLEAN)"
            )

    def get_all_devices(self):
        cursor = self.connection.execute("SELECT * FROM devices")
        devices = {}
        for row in cursor:
            device = DeviceModel(device_id=row[0], name=row[1], state=row[2])
            devices[device.device_id] = device
        return devices

    def update_device_state(self, device_id, state):
        with self.connection:
            self.connection.execute(
                "UPDATE devices SET state = ? WHERE id = ?", (state, device_id)
            )

    def add_device(self, device):
        with self.connection:
            self.connection.execute(
                "INSERT INTO devices (name, state) VALUES (?, ?)",
                (device.name, device.state)
            )
