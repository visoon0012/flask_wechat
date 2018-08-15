import json

import requests
from flask import jsonify

from app import app
from app_movie.models.movie import Movie

@app.route('/api/movie/movie/o/<oid>/', methods=['GET'])
def get_movie_oid(oid):
    movie = Movie.objects.get_or_404(id=oid)
    return jsonify(movie), 200


@app.route('/api/movie/movie/m/<mid>/', methods=['GET'])
def get_movie_mid(mid):
    movie = Movie.objects(mid=mid)
    if movie:
        pass
    else:
        # 如果电影详情不存在，则用豆瓣API查询
        url = 'http://api.douban.com/v2/movie/subject/%s' % str(mid)
        response = requests.get(url)
        item = json.loads(response.text)
        item['mid'] = item['id']
        del item['id']
        movie = Movie(**item)
        movie.save()
    return jsonify(movie), 200
