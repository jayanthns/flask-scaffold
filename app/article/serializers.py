from extensions import ma
from models.article import Article
from marshmallow import ValidationError, validate


def validate_required_string(field_value):
    if not len(field_value):
        raise ValidationError("This field value is required")


class ArticleSchema(ma.Schema):
    # created_on = ma.Function(lambda obj: obj.created_on.strftime("%d-%m-%y"))
    # modified_on = ma.Function(lambda obj: obj.modified_on.strftime("%d-%m-%y"))

    class Meta:
        fields = ('id', 'name', 'author', 'description',
                  'created_on', 'modified_on')


article_schema = ArticleSchema()
articles_schema = ArticleSchema(many=True)


class ArticleCreateSchema(ma.Schema):
    name = ma.String(required=True, allow_null=False,
                     max_length=100, validate=validate_required_string)
    author = ma.String(required=True, allow_null=False,
                       max_length=100, validate=validate_required_string)
    description = ma.String(max_length=250)

    class Meta:
        fields = ('name', 'author', 'description')


article_create_schema = ArticleCreateSchema()


class ArticleUpdateSchema(ma.Schema):
    class Meta:
        fields = ('name', 'author', 'description')


article_update_schema = ArticleUpdateSchema()
