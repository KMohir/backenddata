from rest_framework import serializers

from basic_app.models.youtube import Youtube

class YoutubeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Youtube
        fields = ('url', 'created_at', 'updated_at', 'created_by', 'updated_by')

class NewsDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Youtube
        fields = "__all__"

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["post"] = instance.post.html
        return data
