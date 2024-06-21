class SmartHomeView:
    def __init__(self, controller):
        self.controller = controller

    def run(self):
        try:
            while True:
                self.display_menu()
        except Exception as e:
            print(f"Ошибка в работе интерфейса: {e}")

    def display_menu(self):
        """небольшое меню пользователя"""
        print("1. Включить устройство")
        print("2. Выключить устройство")
        print("3. Показать состояние устройств")
        print("4. Создать новое устройство")
        print("5. Выйти")

        choice = input("Выберите действие: ")
        try:
            if choice == '1':
                self.toggle_device(True)
            elif choice == '2':
                self.toggle_device(False)
            elif choice == '3':
                self.show_device_states()
            elif choice == '4':
                self.create_device()
            elif choice == '5':
                exit()
            else:
                print("Некорректный выбор")
        except Exception as e:
            print(f"Ошибка обработки выбора: {e}")

    def toggle_device(self, state):
        try:
            device_id = int(input("Введите ID устройства: "))
            self.controller.toggle_device(device_id, state)
        except ValueError:
            print("Некорректный ID устройства")
        except Exception as e:
            print(f"Ошибка переключения устройства: {e}")

    def show_device_states(self):
        try:
            for device_id, device in self.controller.devices.items():
                print(f"Устройство {device_id}: {device.name} - {'Включено' if device.state else 'Выключено'}")
        except Exception as e:
            print(f"Ошибка отображения состояния устройств: {e}")

    def create_device(self):
        try:
            self.controller.create_device()
        except Exception as e:
            print(f"Ошибка создания устройства: {e}")
