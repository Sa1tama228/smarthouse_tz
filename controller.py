from models import DeviceModel, Database


class SmartHomeController:
    def __init__(self):
        try:
            self.db = Database('database/smart_home.db')  # выбираем бд
            self.devices = self.load_devices()  # инициализация девайсов
        except Exception as e:
            print(f"Ошибка инициализации контроллера: {e}")

    def load_devices(self):
        try:
            return self.db.get_all_devices()
        except Exception as e:
            print(f"Ошибка загрузки устройств: {e}")
            return {}

    def toggle_device(self, device_id, state):
        try:
            device = self.devices.get(device_id)
            if device:
                device.state = state
                self.db.update_device_state(device_id, state)
            else:
                print(f"Устройство с ID {device_id} не найдено")
        except Exception as e:
            print(f"Ошибка переключения устройства: {e}")

    def get_device_state(self, device_id):
        try:
            device = self.devices.get(device_id)
            if device:
                return device.state
            else:
                print(f"Устройство с ID {device_id} не найдено")
                return None
        except Exception as e:
            print(f"Ошибка получения состояния устройства: {e}")
            return None

    def create_device(self):
        try:
            accept = input('Создать новый девайс? y/n: ').strip().lower()
            if accept == 'y':
                name = input('Название девайса: ')
                state = False  # Новые устройства по умолчанию выключены
                new_device = DeviceModel(name=name, state=state)
                self.db.add_device(new_device)
                self.devices = self.load_devices()  # Обновляемый список устройств
            else:
                print('Операция отменена')
        except Exception as e:
            print(f"Ошибка создания устройства: {e}")
