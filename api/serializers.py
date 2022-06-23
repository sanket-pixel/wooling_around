from rest_framework import serializers
from base.models import WoolItem

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = WoolItem
        fields = '__all__'

