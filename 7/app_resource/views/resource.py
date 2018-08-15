from flask import jsonify, request
from mongoengine import Q

import uuid
from urllib import parse
from app import app
from app_resource.models.resource import Resource
from app_spider.resource import btbtdy


@app.route('/api/resource/<keyword>/', methods=['GET'])
def get_resource(keyword):
    resources = Resource.objects(Q(title__icontains=keyword) | Q(
        name__icontains=keyword) | Q(download_link__icontains=keyword))
    return jsonify(resources), 200


@app.route('/api/resource/spider/', methods=['GET'])
def spider_resource():
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
            except Exception as e:
                app.logger.error(e)
    return jsonify({'message': 'ok'}), 200
