from pickle import GET
from platform import platform
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import status

from watchlist_app.models import Movie,StreamPlatform,WatchList
from watchlist_app.api.serializers import MovieSerializer
from watchlist_app.api.serializers import StreamPlatformSerializer, WatchlistSerializer


@api_view(['GET','POST'])
def movie_list(request):
    if request.method=='GET':
        movies=Movie.objects.all()
        serializer=MovieSerializer(movies,many=True)
        'many=True rakhnu parxa id .objects all use garne vaye kina vane sabai data linu parxa '
        return Response(serializer.data)
    
    if request.method=='POST':
        serializer=MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

@api_view(['GET','PUT','DELETE'])
def movie_detail(request,pk):
    if request.method=='GET':
        movie=Movie.objects.get(pk=pk)
        serializer=MovieSerializer(movie)
        return Response(serializer.data)

    if request.method=='PUT':
        movie=Movie.objects.get(pk=pk)
        serializer=MovieSerializer(movie,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    if request.method=='DELETE':
        movie=Movie.objects.get(pk=pk)
        movie.delete()
        return HttpResponse("Deleted")


'Class based Views'
class StreamPlatformAV(APIView):
    def get(self,request):
        platform=StreamPlatform.objects.all()
        serializer=StreamPlatformSerializer(platform,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer=StreamPlatformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=status.HTTP_406_NOT_ACCEPTABLE)


class WatchListAV(APIView):
    def get(self,request):
        platform=WatchList.objects.all()
        serializer=WatchlistSerializer(platform,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer=WatchlistSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        else:
            return Response(serializer.errors,status=status.HTTP_406_NOT_ACCEPTABLE)
