from controller import SmartHomeController
from views import SmartHomeView


def main():
    """запуск главных функций"""
    try:
        controller = SmartHomeController()
        view = SmartHomeView(controller)
        view.run()
    except Exception as e:
        print(f"Ошибка при запуске системы: {e}")


if __name__ == "__main__":
    main()
