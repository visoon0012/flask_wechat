class Config(object):  # 创建配置，用类
    JOBS = [  # 任务列表
        {  # 任务字典
            'id': 'get_movie_resource',
            'func': 'app_apscheduler.apscheduler_jobs:get_movie_resource',
            # 'args': (1, 2),
            'trigger': 'cron',
            'hour': 0,
            'minute': 0
        },
        {  # 第二个任务字典
            'id': 'job_1',
            'func': 'app_apscheduler.apscheduler_jobs:job_1',
            'args': (),
            'trigger': 'interval',
            'seconds': 1,
        }
    ]
