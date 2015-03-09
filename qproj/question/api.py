from tastypie.resources import ModelResource
from qproj.question import models

class PostResource(ModelResource):
    class Meta:
        queryset = models.Post.objects.all();
        resource_name = 'post';

class CommentResource(ModelResource):
    class Meta:
        queryset = models.Comment.objects.all();
        resource_name = 'comment';