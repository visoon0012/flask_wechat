import uuid
from urllib import parse
import datetime

import app_spider
from app_resource.models.resource import Resource

from app_movie.models.ranking import Ranking
from app_movie.models.movie import Movie


def job_1():  # 一个函数，用来做定时任务的任务。
    print(datetime.datetime.now())


def get_movie_resource():
    count = 1
    items = app_spider.resource.btbtdy.processing_list()
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


def get_movie_ranking():
    type_tag_list = [
        {'type': 'movie', 'tag': '热门'}
    ]
    for type_tag in type_tag_list:
        _type = type_tag['type']
        tag = type_tag['tag']
        movies = app_spider.movie.ranking.get_ranking(_type, tag, 500, 0)
        # 先把原有的该类型的排行更新为0
        Ranking.objects(douban_tag=tag, douban_type=_type).update(level=0)
        # 循环更新
        level = len(movies)
        for item in movies:
            item['level'] = level
            item['mid'] = item['id']
            del item['id']
            level -= 1
            ranking = Ranking.objects(
                mid=item['mid'], douban_tag=tag, douban_type=_type).first()
            if ranking:
                ranking.update(**item)
            else:
                item['resources'] = 0
                ranking = Ranking(douban_tag=tag, douban_type=_type, **item)
                ranking.save()
