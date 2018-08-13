import uuid
from urllib import parse
import datetime

from app_spider.resource import btbtdy
from app_resource.models.resource import Resource


def job_1():  # 一个函数，用来做定时任务的任务。
    print(datetime.datetime.now())


def get_movie_resource():
    count = 1
    items = btbtdy.processing_list()
    for item in items:
        results = btbtdy.processing_detail(item['href'])
        for result in results:
            try:
                resource = Resource(
                    name=parse.unquote(result['name'][:255] if len(
                        result['name']) > 255 else result['name']),
                    title=parse.unquote(item['title']),
                    download_link=parse.unquote(result['download_link']),
                    download_uuid=str(uuid.uuid3(
                        uuid.NAMESPACE_URL, parse.unquote(result['download_link']))),
                    source=parse.unquote(result['source']),
                    source_type=item['source_type']
                )
                resource.save()
                count += 1
            except Exception as e:
                app.logger.error(e)
    return count
