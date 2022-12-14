from utils.bilibili import BILIBILI

BILI = BILIBILI()


class Config:

    JOBS = [
        {  # 每天01：15执行
            'id': 'job1',
            'func': BILI.start,
            'args': ('update', BILI.update_user_info),
            'trigger': 'cron',
            'day_of_week': '0-6',
            'hour': 1,
            'minute': 15,
        },
        {  # 每周日 23:59:00 执行
            'id': 'job2',
            'func': BILI.start,
            'args': ('check', BILI.week_chenck),
            'trigger': 'cron',
            'day_of_week': 6,
            'hour': 23,
            'minute': 45
        },
        {  # 每半小时执行
            'id': 'job3',
            'func': BILI.start,
            'args': ('push', BILI.push),
            'trigger': 'interval',
            'minutes': 30,
        }
    ]
    # 配置时区
    SCHEDULER_TIMEZONE = 'Asia/Shanghai'
    # 调度器开关
    SCHEDULER_API_ENABLED = True

