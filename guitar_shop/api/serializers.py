
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Guitars


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']


class GuitarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guitars
        fields = ['id', 'name', 'img', 'price']


from .models import Video
class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ['file']