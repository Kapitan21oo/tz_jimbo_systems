from rest_framework import serializers
from .models import Page, Block


class BlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Block
        fields = ['title', 'video_link', 'sort_order', 'view_count']


class PageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Page
        fields = ['title', 'slug']
