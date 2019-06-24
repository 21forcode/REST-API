from rest_framework import serializers
from .models import poat


class appSerializer(serializers.ModelSerializer):
    class Meta:
        model = poat
        fields = ("bank_name", "city","details")
