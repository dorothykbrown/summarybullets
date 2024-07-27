from rest_framework import serializers
from .models import BulletPoint, Summary

class SummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Summary
        fields = ['id', 'name', 'original_text', 'summary']

class BulletPointSerializer(serializers.ModelSerializer):
    class Meta:
        model = BulletPoint
        fields = ['id', 'name', 'original_text', 'bullet_points']