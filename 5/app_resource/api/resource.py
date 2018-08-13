
from flask import jsonify, request
from mongoengine import Q

from app import app
from app_resource.models.resource import Resource


@app.route('/api/resource/<keyword>', methods=['GET'])
def get_resource(keyword):
    resources = Resource.objects(Q(title__icontains=keyword) | Q(
        name__icontains=keyword) | Q(download_link__icontains=keyword))
    return jsonify(resources), 200
