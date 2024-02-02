#!/usr/bin/env python3
# coding=utf-8
# module name: cof_schedule
# author: Cof-Lee
# update: 2024-02-02
# 本模块使用MIT开源协议

import time
import sched


def split_crontab_str(crontab):
    crontab_tuple = crontab.split(" ")
    if len(crontab_tuple) != 5:
        raise Exception("crontab length is not 5", crontab)
    else:
        return crontab_tuple


def get_cron_time_by_second(second_str):
    # input <str> , output tuple<int,int>  <起始时间，间隔倍数>
    # 输入为 * 时，输出 (-1,0)
    # 输入为 */5 时，输出 (-1,5)
    # 输入为 '' 空时，输出 (-2,0)
    # 输入为 0-59 时，输出 (0-59,0)  输入 <0或>59 则报错
    # 其他未识别输入则输出 (-3,0)
    if second_str == "*":
        return -1, 0
    if second_str == '':
        return -2, 0
    if second_str.isdigit():
        if int(second_str) < 0 or int(second_str) > 59:
            raise Exception("second_str is not in [0-59]", second_str)
        else:
            return int(second_str), 0
    second_str_seg = second_str.split("/")  # 对应 '*/5' 每5分钟这种情况
    if len(second_str_seg) == 2 and second_str_seg[1].isdigit():
        return -1, int(second_str_seg[1])
    else:
        return -3, 0


def get_cron_time_by_minute(minute_str):
    # input <str> , output tuple<int,int>  <起始时间，间隔倍数>
    # 输入为 * 时，输出 (-1,0)
    # 输入为 */5 时，输出 (-1,5)
    # 输入为 '' 空时，输出 (-2,0)
    # 输入为 0-59 时，输出 (0-59,0)  输入 <0或>59 则报错
    # 其他未识别输入则输出 (-3,0)
    if minute_str == "*":
        return -1, 0
    if minute_str == '':
        return -2, 0
    if minute_str.isdigit():
        if int(minute_str) < 0 or int(minute_str) > 59:
            raise Exception("minute_str is not in [0-59]", minute_str)
        else:
            return int(minute_str), 0
    minute_str_seg = minute_str.split("/")  # 对应 '*/5' 每5分钟这种情况
    if len(minute_str_seg) == 2 and minute_str_seg[1].isdigit():
        return -1, int(minute_str_seg[1])
    else:
        return -3, 0


def get_cron_time_by_hour(hour_str):
    # input <str> , output tuple<int,int>  <起始时间，间隔倍数>
    # 输入为 * 时，输出 (-1,0)
    # 输入为 */5 时，输出 (-1,5)
    # 输入为 '' 空时，输出 (-2,0)
    # 输入为 0-23 时，输出 (0-23,0)  输入 <0或>23 则报错
    # 其他未识别输入则输出 (-3,0)
    if hour_str == "*":
        return -1, 0
    if hour_str == '':
        return -2, 0
    if hour_str.isdigit():
        if int(hour_str) < 0 or int(hour_str) > 23:
            raise Exception("hour is not in [0-23]", hour_str)
        else:
            return int(hour_str), 0
    hour_str_seg = hour_str.split("/")  # 对应 '*/5' 这种情况
    if len(hour_str_seg) == 2 and hour_str_seg[1].isdigit():
        return -1, int(hour_str_seg[1])
    else:
        return -3, 0


def get_cron_time_by_day(day_str):
    # input <str> , output tuple<int,int>  <起始时间，间隔倍数>
    # 输入为 * 时，输出 (-1,0)
    # 输入为 */5 时，输出 (-1,5)
    # 输入为 '' 空时，输出 (-2,0)
    # 输入为 1-31 时，输出 (1-31,0)  输入 <1或>31 则报错
    # 其他未识别输入则输出 (-3,0)
    if day_str == "*":
        return -1, 0
    if day_str == '':
        return -2, 0
    if day_str.isdigit():
        if int(day_str) < 1 or int(day_str) > 31:
            raise Exception("day is not in [1-31]", day_str)
        else:
            return int(day_str), 0
    day_str_seg = day_str.split("/")  # 对应 '*/5' 这种情况
    if len(day_str_seg) == 2 and day_str_seg[1].isdigit():
        return -1, int(day_str_seg[1])
    else:
        return -3, 0


def get_cron_time_by_month(month_str):
    # input <str> , output tuple<int,int>  <起始时间，间隔倍数>
    # 输入为 * 时，输出 (-1,0)
    # 输入为 */5 时，输出 (-1,5)
    # 输入为 '' 空时，输出 (-2,0)
    # 输入为 1-12 时，输出 (1-12,0)  输入 <1或>12 则报错
    # 其他未识别输入则输出 (-3,0)
    if month_str == "*":
        return -1, 0
    if month_str == '':
        return -2, 0
    if month_str.isdigit():
        if int(month_str) < 1 or int(month_str) > 12:
            raise Exception("month is not in [0-12]", month_str)
        else:
            return int(month_str), 0
    month_str_seg = month_str.split("/")  # 对应 '*/5' 这种情况
    if len(month_str_seg) == 2 and month_str_seg[1].isdigit():
        return -1, int(month_str_seg[1])
    else:
        return -3, 0


def get_cron_time_by_weekday(weekday_str):
    # input <str> , output tuple<int,int>  <起始时间，间隔倍数>
    # 输入为 * 时，输出 (-1,0)
    # 输入为 */5 时，星期不支持这种写法
    # 输入为 '' 空时，输出 (-2,0)
    # 输入为 0-7 时，输出 (0-7,0)  输入 <0或>7 则报错
    # 其他未识别输入则输出 (-3,0)
    if weekday_str == "*":
        return -1, 0
    if weekday_str == '':
        return -2, 0
    if weekday_str.isdigit():
        if int(weekday_str) < 0 or int(weekday_str) > 7:
            raise Exception("weekday is not in [0-7]", weekday_str)
        else:
            return int(weekday_str), 0
    weekday_str_seg = weekday_str.split("/")  # 对应 '*/5' 这种情况
    if len(weekday_str_seg) == 2 and weekday_str_seg[1].isdigit():
        raise Exception("weekday is not support */N", weekday_str)
    else:
        return -3, 0


class Scheduler:
    def __init__(self, crontab='* * * * *', second=None, target_func=None, args=()):
        crontab_tuple = split_crontab_str(crontab)
        self.minute_str = str(crontab_tuple[0])
        self.hour_str = str(crontab_tuple[1])
        self.day_str = str(crontab_tuple[2])
        self.month_str = str(crontab_tuple[3])
        self.weekday_str = str(crontab_tuple[4])
        if second is None:
            self.second_str = '*'
        else:
            self.second_str = second
        self.minute_tuple = ()  # <起始时间，间隔倍数> ，如 '*/5' 转为 (-1,5)
        self.hour_tuple = ()  # <起始时间，间隔倍数> ，如 '3' 转为 (3,0)
        self.day_tuple = ()
        self.month_tuple = ()
        self.weekday_tuple = ()
        self.second_tuple = ()  # 秒数是额外设置的参数
        self.last_job_start_time = 0
        self.last_job_end_time = 0
        self.target_func = target_func
        self.args = args  # <tuple>

    def cron_job_func(self, index):  # 执行周期任务函数，到时间后调用目标函数
        self.last_job_start_time = time.time()
        time_strftime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(self.last_job_start_time))
        print(f"第 {index} 次调度作业任务，开始时间为 {time_strftime}")
        self.target_func(*self.args)

    def get_cron_time(self):
        # 根据__init__()输入的参数（分时日月周），把str转为int型的tuple
        self.minute_tuple = get_cron_time_by_minute(self.minute_str)
        self.hour_tuple = get_cron_time_by_hour(self.hour_str)
        self.day_tuple = get_cron_time_by_day(self.day_str)
        self.month_tuple = get_cron_time_by_month(self.month_str)
        self.weekday_tuple = get_cron_time_by_weekday(self.weekday_str)
        self.second_tuple = get_cron_time_by_second(self.second_str)
        print(self.minute_tuple, self.hour_tuple, self.day_tuple, self.month_tuple, self.weekday_tuple)

    def get_next_cron_job_time(self):
        # output <int> ，根据crontab，获取从当前时间开始，到最近一次(下一次)周期任务的时间间隔，单位：秒
        # 比如创建对象时输入的crontab为 "*/5 * * * *" 表示每5分钟执行一次，则本方法返回值为300（5乘以60）
        last_job_duration_time = self.last_job_end_time - self.last_job_start_time
        if self.weekday_tuple[0] in range(8):  # 如果指定了每周几，则day,month这2个字段无效
            print(f"每周{self.weekday_tuple[0]}")
        if self.second_tuple[0] == -1:
            if self.second_tuple[1] != 0:
                # 如果每次作业运行时长不大于 1个周期时间间隔，则下1次作业等待时间要减去上一次作业运行时长
                next_cron_job_delay_time = self.second_tuple[1] - last_job_duration_time
                if next_cron_job_delay_time >= 0:
                    return next_cron_job_delay_time
                # 如果每次作业运行时长大于 1个周期时间间隔，则直接返回 1个周期时间间隔
                else:
                    return self.second_tuple[1]
        return 10

    def start(self):  # 开始总入口函数
        self.get_cron_time()
        index = 0
        delay_time = 3  # 第一次运行回调函数前要等待的时间
        while True:
            sched1 = sched.scheduler(time.time, time.sleep)  # 创建一个调度器
            sched1.enter(delay_time, 1, self.cron_job_func, (index,))  # 延迟 delay_time 秒，优先级1，回调函数，参数
            sched1.run()  # 运行调度器，默认是blocking=True，阻塞模式，等时间到了才运行回调函数，回调函数运行后才继续
            self.last_job_end_time = time.time()  # 回调函数运行结束后的时间
            time_strftime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(self.last_job_end_time))
            print(f'index: {index} 运行调度器之后的输出 {time_strftime}')
            print(f'index: {index} 回调函数用时 {self.last_job_end_time - self.last_job_start_time} 秒')
            print("#")
            delay_time = self.get_next_cron_job_time()  # 获取下一次周期任务的时间间隔，单位：秒
            index += 1
