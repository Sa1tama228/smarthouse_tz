from controller import SmartHomeController
from views import SmartHomeView


def main():
    """запуск главных функций"""
    controller = SmartHomeController()
    view = SmartHomeView(controller)
    view.run()


if __name__ == "__main__":
    main()
