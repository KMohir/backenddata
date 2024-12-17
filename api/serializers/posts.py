from rest_framework import serializers

import basic_app.models as models
import api.serializers.dinamic_serializers as base_serializers


class PostsListSerializer(serializers.ModelSerializer):
    navbar = base_serializers.build_relational_model_serializer(models.Navbar, fields_=("id", "name", "slug"))

    class Meta:
        model = models.Posts
        fields = ("id", "title","subtitle", "subtitle","navbar", "added_at", "image", "slug", "post_viewed_count", "author_post")


class PostsDetailSerializer(serializers.ModelSerializer):
    navbar = base_serializers.build_relational_model_serializer(models.Navbar, fields_=("id", "name", "slug"))

    class Meta:
        model = models.Posts
        fields = "__all__"

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["post"] = instance.post.html
        return data
