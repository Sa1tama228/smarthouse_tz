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
        try:
            self.connection = sqlite3.connect(db_file)
            self.create_tables()
        except sqlite3.Error as e:
            print(f"Ошибка подключения к базе данных: {e}")

    def create_tables(self):
        try:
            with self.connection:
                self.connection.execute(
                    "CREATE TABLE IF NOT EXISTS devices (id INTEGER PRIMARY KEY, name TEXT, state BOOLEAN)"
                )
        except sqlite3.Error as e:
            print(f"Ошибка создания таблиц: {e}")

    def get_all_devices(self):
        try:
            cursor = self.connection.execute("SELECT * FROM devices")
            devices = {}
            for row in cursor:
                device = DeviceModel(device_id=row[0], name=row[1], state=row[2])
                devices[device.device_id] = device
            return devices
        except sqlite3.Error as e:
            print(f"Ошибка получения устройств: {e}")
            return {}

    def update_device_state(self, device_id, state):
        try:
            with self.connection:
                self.connection.execute(
                    "UPDATE devices SET state = ? WHERE id = ?", (state, device_id)
                )
        except sqlite3.Error as e:
            print(f"Ошибка обновления состояния устройства: {e}")

    def add_device(self, device):
        try:
            with self.connection:
                self.connection.execute(
                    "INSERT INTO devices (name, state) VALUES (?, ?)",
                    (device.name, device.state)
                )
        except sqlite3.Error as e:
            print(f"Ошибка добавления устройства: {e}")
