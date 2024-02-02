import cof_schedule
import time


def call_back(index):
    print(f"this is cron job func: {index}")
    time.sleep(3)


sched1 = cof_schedule.Scheduler(crontab="* * * * *", second="*/5", target_func=call_back, args=("abc",))
sched1.start()
