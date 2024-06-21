from models import DeviceModel, Database


class SmartHomeController:
    def __init__(self):
        self.db = Database('database/smart_home.db')  # выбираем бд
        self.devices = self.load_devices()  # инициализация девайсов

    def load_devices(self):
        return self.db.get_all_devices()

    def toggle_device(self, device_id, state):
        device = self.devices.get(device_id)
        if device:
            device.state = state
            self.db.update_device_state(device_id, state)

    def get_device_state(self, device_id):
        return self.devices.get(device_id).state

    def create_device(self):
        accept = input('Создать новый девайс? y/n: ').strip().lower()
        if accept == 'y':
            name = input('Название девайса: ')
            state = False  # Новые устройства по умолчанию выключены
            new_device = DeviceModel(name=name, state=state)
            self.db.add_device(new_device)
            self.devices = self.load_devices()  # Обновляемый список устройств
        else:
            print('Операция отменена')
