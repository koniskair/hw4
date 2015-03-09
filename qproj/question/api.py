from tastypie.resources import ModelResource
from tastypie.authorization import Authorization
from qproj.question import models
from tastypie import fields

class PostResource(ModelResource):
    author = fields.CharField(attribute = "author", use_in = "list");
    title = fields.CharField(attribute = "title", use_in = "list");
    text = fields.CharField(attribute = "text", use_in = "list");

    is_public = fields.BooleanField(attribute = "is_public", use_in = "detail");
    comment = fields.ToManyField('qproj.question.api.CommentResource', 'comment_set', null=True, use_in="detail");


    class Meta:
        queryset = models.Post.objects.all();
        resource_name = 'post';
        authorization= Authorization();
        always_return_date = True;

class CommentResource(ModelResource):
    author = fields.CharField(attribute = "author");
    text = fields.CharField(attribute = "text");

    post = fields.ToOneField('qproj.question.api.PostResource', 'post');


    class Meta:
        queryset = models.Comment.objects.all();
        resource_name = 'comment';
        authorization= Authorization();
        always_return_date = True;