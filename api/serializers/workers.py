from rest_framework import serializers

import basic_app.models as models


class AdministratorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Administrator
        fields = ("id","title","title_uz","title_ru","title_en","name","name_uz","name_ru","name_en","position","position_uz","position_ru","position_en","phone","image")


class AdministratorDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Administrator
        fields = "__all__"
