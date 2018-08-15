import datetime

from app import db


class Movie(db.DynamicDocument):
    mid = db.StringField(unique=True)
    title = db.StringField()

    created_time = db.DateTimeField(default=datetime.datetime.now)  # 创建时间
    updated_time = db.DateTimeField(default=datetime.datetime.now)  # 更新时间

    @classmethod
    def pre_save(cls, sender, document, **kwargs):
        document.updated_time = datetime.datetime.now()

    def __str__(self):
        return self.title
