import math

from flask import jsonify

from app import app
from app_apscheduler import apscheduler_jobs
from app_movie.models.ranking import Ranking
from config import PAGE_LIMIT


@app.route('/api/movie/ranking/<douban_type>/<douban_tag>/<int:page>', methods=['GET'])
def get_ranking(douban_type, douban_tag, page):
    """获取排名"""
    ranking = Ranking.objects(douban_type=douban_type,
                              douban_tag=douban_tag).order_by('-level')
    return jsonify({'pages': math.ceil(len(ranking) / PAGE_LIMIT), 'items': ranking[page * PAGE_LIMIT:(page + 1) * PAGE_LIMIT]}), 200
