import datetime

from app import db


class Resource(db.DynamicDocument):
    title = db.StringField()
    name = db.StringField()
    source = db.StringField()
    source_type = db.StringField()
    download_link = db.StringField()  # 下载链接
    download_uuid = db.StringField()  # uuid3 防止重复
    show_times = db.IntField()  # 显示次数
    like_times = db.IntField()  # 喜欢次数
    dislike_times = db.IntField()  # 不喜欢次数
    report_times = db.IntField()  # 举报次数

    created_time = db.DateTimeField(default=datetime.datetime.now)  # 创建时间
    updated_time = db.DateTimeField(default=datetime.datetime.now)  # 更新时间

    @classmethod
    def pre_save(cls, sender, document, **kwargs):
        document.updated_time = datetime.datetime.now()

    def __str__(self):
        return self.name
