from controller import SmartHomeController
from models import DeviceModel


def test_toggle_device():
    controller = SmartHomeController()
    device = DeviceModel(name='Light', state=False)
    controller.db.add_device(device)
    controller.toggle_device(1, True)
    assert controller.get_device_state(1) is True


def test_create_device(monkeypatch):
    controller = SmartHomeController()

    monkeypatch.setattr('builtins.input', lambda _: 'y')
    monkeypatch.setattr('builtins.input', lambda _: 'Test Device')

    controller.create_device()
    devices = controller.db.get_all_devices()
    assert len(devices) == 1
    assert devices[1].name == 'Test Device'
    assert devices[1].state is False
