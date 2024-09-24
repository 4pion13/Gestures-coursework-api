from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from . import serializers
from django.contrib.auth.models import User
from .models import Guitars



class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer

class GuitarList(generics.ListAPIView):
    queryset = Guitars.objects.all()
    serializer_class = serializers.GuitarSerializer



from .models import Video
class VideoUploadView(generics.CreateAPIView):
    queryset = Video.objects.all()
    serializer_class = serializers.VideoSerializer
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        video = serializer.save()
        # Получаем полный путь к файлу
        file_url = request.build_absolute_uri(video.file.url)
        return Response({'file_url': file_url}, status=status.HTTP_201_CREATED)