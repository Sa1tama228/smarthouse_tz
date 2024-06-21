import schedule
import time
import threading


class Scheduler:
    """модуль для работы с расписанием, вместе с многопоточностью"""
    def __init__(self, controller):
        self.controller = controller
        self.jobs = []

    def schedule(self, device_id, time, state):
        try:
            job = schedule.every().day.at(time).do(self.controller.toggle_device, device_id, state)
            self.jobs.append(job)
            threading.Thread(target=self.run_scheduler).start()
        except Exception as e:
            print(f"Ошибка планирования задачи: {e}")

    def run_scheduler(self):
        while True:
            try:
                schedule.run_pending()
                time.sleep(1)
            except Exception as e:
                print(f"Ошибка выполнения задач: {e}")
