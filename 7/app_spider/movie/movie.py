import json

import requests


def get_movie(mid):
    url = 'http://api.douban.com/v2/movie/subject/%s' % str(mid)
    response = requests.get(url)
    item = json.loads(response.text)
    item['mid'] = item['id']
    del item['id']  # 为了ID字段不被占用
    return item


if __name__ == '__main__':
    print(get_movie(26588308))
