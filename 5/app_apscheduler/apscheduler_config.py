class Config(object):  # 创建配置，用类
    JOBS = [  # 任务列表
        # {  # 任务字典（细节）
        #     'id': 'job1',
        #     'func': '__main__:print_hello',
        #     # 'args': (1, 2),
        #     'trigger': 'cron',
        #     'hour': 0,
        #     'minute': 0
        # },
        {  # 第二个任务字典
            'id': 'get_movie_ranking',
            'func': 'app_apscheduler.apscheduler_jobs:get_movie_ranking',
            'args': (),
            'trigger': 'interval',
            'seconds': 60 * 10,
        }
    ]
