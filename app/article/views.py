import logging

from flask import Blueprint, jsonify, request

from models.article import Article

from app.article.serializers import (
    articles_schema,
    article_schema,
    article_create_schema,
    article_update_schema,
)

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)


article_api_blueprint = Blueprint(
    'article_api', __name__
)


@article_api_blueprint.route("/", methods=['GET', 'POST'], strict_slashes=False)
def articles():
    """view for get articles"""
    log.info("HHHH")
    # print(a)
    if request.method == "GET":
        articles = articles_schema.dump(Article.query.all())
        return jsonify(
            {
                "success": True,
                "data": articles.data,
                "status": 200,
                "code": 200
            }
        ), 200

    """View for Creating the article."""
    if request.method == 'POST':
        article_data = article_create_schema.load(request.get_json() or {})

        if article_data.errors:
            return jsonify(
                {
                    "data": {**article_data.errors},
                    "success": False,
                    "status": 401,
                    "code": 401
                }
            ), 401

        article_data = article_data.data
        article = Article(
            name=article_data.get('name'),
            author=article_data.get('author'),
            description=article_data.get('description', '')
        )
        article.save()
        article = article_schema.dump(article)
        return jsonify(
            {
                "success": True,
                "data": article.data,
                "status": 201,
                "code": 201,
                "message": "Article created successfully.",
            }
        ), 201


@article_api_blueprint.route("/<int:id>", methods=['GET', 'PUT'], strict_slashes=False)
def article_details(id):
    """Checking the article existence"""
    article = Article.query.get(id)
    if not article:
        return jsonify(
            {
                "success": False,
                "message": "Article not found",
                "status": 404,
                "code": 404,
                "data": None,
            }
        ), 404

    """Detail of the article"""
    if request.method == 'GET':
        article = article_schema.dump(article)
        return jsonify(
            {
                "success": True,
                "data": article.data,
                "status": 200,
                "code": 200,
                "message": "Data fetched successfully.",
            }
        ), 200

    """Updating the  article"""
    if request.method == "PUT":
        article_serializer = article_update_schema.load(request.get_json() or {})
        if article_serializer.errors:
            return jsonify(
                {
                    "data": {**article_serializer.errors},
                    "success": False,
                    "code": 401,
                    "status": 401
                }
            ), 401
        article_data = article_serializer.data
        article.name = article_data.get('name', article.name)
        article.author = article_data.get('author', article.author)
        article.description = article_data.get('description', article.description)
        article.save()
        article = article_schema.dump(article)
        return jsonify(
            {
                "success": True,
                "article": article.data
            }
        ), 200
