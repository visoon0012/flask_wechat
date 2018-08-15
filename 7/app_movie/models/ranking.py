import datetime

from app import db


class Ranking(db.DynamicDocument):
    douban_type = db.StringField()
    douban_tag = db.StringField()
    level = db.IntField()

    created_time = db.DateTimeField(default=datetime.datetime.now)  # 创建时间
    updated_time = db.DateTimeField(default=datetime.datetime.now)  # 更新时间

    @classmethod
    def pre_save(cls, sender, document, **kwargs):
        document.updated_time = datetime.datetime.now()

    def __str__(self):
        return '{}:{}'.format(self.douban_type, self.douban_tag)
