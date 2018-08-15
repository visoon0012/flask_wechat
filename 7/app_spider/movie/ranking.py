import json
from datetime import datetime

import requests


def get_ranking(_type, tag, page_limit, page_start):
    """
    获取排名
    :param _type: 类型 movie/tv
    :param tag: 标签 热门/最新...
    :param page_limit:
    :param page_start:
    :return: []
    """
    url = 'https://movie.douban.com/j/search_subjects?type=%s&tag=%s&sort=recommend&page_limit=%s&page_start=%s' \
          % (_type, tag, page_limit, page_start)
    response = requests.get(url)
    if response.text:
        return json.loads(response.text)['subjects']
    else:
        return []


if __name__ == '__main__':
    print(get_ranking('movie', '热门', 10, 0))
