import uuid
from urllib import parse

from app_apscheduler.utils.spider.movie.douban.ranking import get_ranking
from app_apscheduler.utils.spider.movie.resource import dygang, dy2018, piaohua, btbtdy
from app_resource.models.resource import Resource


def job_1(a, b):  # 一个函数，用来做定时任务的任务。
    print(str(a) + ' ' + str(b))


def get_movie_ranking():
    get_ranking('movie', '热门', 500, 0)


def get_movie_resource():
    urls = ['btbtdy.com', 'dygang.com', 'dy2018.com', 'piaohua.com', ]
    count = 1
    for url in urls:
        result = []
        try:
            if "dygang" in url:
                items = dygang.processing_index()
                for item in items:
                    result = dygang.processing_detail(item.href)
            elif "dy2018" in url:
                items = dy2018.processing_index()
                for item in items:
                    result = dy2018.processing_detail(item.href)
            elif "piaohua" in url:
                items = piaohua.processing_index()
                for item in items:
                    result = piaohua.processing_detail(item.href)
            elif "btbtdy" in url:
                items = btbtdy.processing_index()
                for item in items:
                    result = btbtdy.processing_detail(item.href)
            else:
                print('没有可以处理的方法')
                return
        except Exception as e:
            print(e.args)
        # 保存到数据库
        for item in result:
            try:
                resource = Resource(
                    name=parse.unquote(item['name'][:255] if len(item['name']) > 255 else item['name']),
                    title=parse.unquote(item.title),
                    download_link=parse.unquote(item['download_link']),
                    download_uuid=uuid.uuid3(uuid.NAMESPACE_URL, parse.unquote(item['download_link'])),
                    source=parse.unquote(item['source']),
                    source_type=item.source_type
                )
                resource.save()
                count += 1
            except Exception as e:
                resource = Resource.objects.get(download_uuid=uuid.uuid3(uuid.NAMESPACE_URL, parse.unquote(item['download_link'])))
                resource.source_type = item.source_type
                resource.save()
                pass
    return count
