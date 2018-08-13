from flask import Flask

from flask_mongoengine import MongoEngine

app = Flask(__name__)

app.config['MONGODB_SETTINGS'] = {
    'db': 'flask_wechat',
    'host': '127.0.0.1',
    'port': 27017
}
db = MongoEngine(app)

# api的业务逻辑
import app_resource.api

if __name__ == '__main__':
    app.run()
