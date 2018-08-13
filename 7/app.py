from flask import Flask

from flask_mongoengine import MongoEngine
from logging.config import dictConfig

dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://flask.logging.wsgi_errors_stream',
        'formatter': 'default'
    }},
    'root': {
        'level': 'INFO',
        'handlers': ['wsgi']
    }
})

app = Flask(__name__)

app.config['MONGODB_SETTINGS'] = {
    'db': 'flask_wechat',
    'host': '127.0.0.1',
    'port': 27017
}
db = MongoEngine(app)

# api的业务逻辑
import app_resource.api
