import schedule
import time
from models import DeviceModel
from scheduler import Scheduler
from controller import SmartHomeController


def test_schedule():
    controller = SmartHomeController()
    scheduler = Scheduler(controller)
    device = DeviceModel(name='Light', state=False)
    controller.db.add_device(device)

    scheduler.schedule(1, "00:00", True)
    assert len(schedule.jobs) > 0
