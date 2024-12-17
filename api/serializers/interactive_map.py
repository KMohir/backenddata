from rest_framework import serializers

import basic_app.models as models


class InteractiveMapSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.InteractiveMap
        fields = ("id", "region_name", "total_area", "cultivated_area",
                  "forest_area", "wasteland_area", "pastures_area", "other_agricultural_land")
