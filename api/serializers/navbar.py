from rest_framework import serializers

import basic_app.models as models


class NavbarListSerializer(serializers.ModelSerializer):
    children = serializers.SerializerMethodField()

    class Meta:
        model = models.Navbar
        fields = [
            "id", "name", "slug", "url", "children"
        ]

    def get_children(self, obj):
        """Recursively get the children of the Navbar."""
        if obj.get_children().exists():
            return NavbarListSerializer(obj.get_children(), many=True).data
        return []
