from flask import Flask

from flask_mongoengine import MongoEngine
from flask_apscheduler import APScheduler

from app_apscheduler.apscheduler_config import Config

app = Flask(__name__)

app.config['MONGODB_SETTINGS'] = {
    'db': 'flask_wechat',
    'host': '127.0.0.1',
    'port': 27017
}
db = MongoEngine(app)

# 定时任务配置
app.config.from_object(Config())
scheduler = APScheduler()  # 实例化APScheduler
scheduler.init_app(app)  # 把任务列表放进flask
scheduler.start()  # 启动任务列表

# api的业务逻辑
import app_resource.api
