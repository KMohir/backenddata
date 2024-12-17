from rest_framework import serializers

import basic_app.models as models


class NewsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.News
        fields = ("id", "title", "subtitle","added_at", "image", "slug", "post_viewed_count", "author_post",'created_at', 'updated_at', 'created_by', 'updated_by')


class NewsDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.News
        fields = "__all__"

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["post"] = instance.post.html
        return data
