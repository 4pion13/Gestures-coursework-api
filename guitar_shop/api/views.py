from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from . import serializers
from django.contrib.auth.models import User
from .models import Guitars, Video
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.decorators import api_view
import sys




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
        file_url = request.build_absolute_uri(video.file.url)
        file_id = Video.objects.get(file=video.file)
        return Response({'file_url': file_url, 'file_id':file_id.id}, status=status.HTTP_201_CREATED)
    
@api_view(['POST'])
def video_process(request):
    number = request.data.get('id')
    print(number)
    if isinstance(number, (int, float)):
        return Response({'message': 'Number received!', 'number': number}, status=status.HTTP_200_OK)
    return Response({'error': 'Invalid input'}, status=status.HTTP_400_BAD_REQUEST)