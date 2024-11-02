from django.shortcuts import render, redirect
from rest_framework.response import Response
from rest_framework.views import APIView
from restWatch_app.models import (WatchList, 
                                  StreamPlatform, Review)
from restWatch_app.api.serializers import (WatchListSerializer, 
                                           StreamPlatformSerializer, ReviewSerializer)
from rest_framework import status
from rest_framework import generics
from rest_framework import viewsets
from django.shortcuts import get_object_or_404


class StreamPlatformVS(viewsets.ViewSet):
    def list(self, request):
        queryset = StreamPlatform.objects.all()
        serializer = StreamPlatformSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def retrive(self, request, pk=None):
        queryset = StreamPlatform.objects.all()
        watchlist = get_object_or_404(queryset, pk=pk)
        serializer = StreamPlatformSerializer(watchlist)
        return Response(serializer.data)


class ReviewListCreate(generics.ListCreateAPIView):
    serializer_class = ReviewSerializer

    def perform_create(self, serializer):
        pk = self.kwargs["pk"]
        watch = WatchList.objects.get(pk=pk)
        serializer.save(watchlist=watch)

class ReviewList(generics.ListCreateAPIView):
    # queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get_queryset(self):
        pk = self.kwargs["pk"]
        return Review.objects.filter(watchlist=pk)

class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class WatchListAV(APIView):
    def get(self, request):
        watch = WatchList.objects.all()
        serializer = WatchListSerializer(watch, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        watch = WatchListSerializer(data=request.data)
        if watch.is_valid():
            watch.save()
            return Response(watch.data, status=status.HTTP_201_CREATED)

class WatchDetailAV(APIView):
    def get(self, request, pk):
        try:
            watch = WatchList.objects.get(pk=pk)
        except WatchList.DoesNotExist:
            return Response({"error": "WatchList not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = WatchListSerializer(watch)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

    def put(self, request, pk):
        try:
            watch = WatchList.objects.get(pk=pk)
        except WatchList.DoesNotExist:
            return Response({"error": "WatchList not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = WatchListSerializer(watch, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        watch = WatchList.objects.get(pk=pk)
        watch.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class StreamPlatformAV(APIView):
    def get(self, request):
        platform = StreamPlatform.objects.all()
        serializer = StreamPlatformSerializer(platform, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        platform = StreamPlatformSerializer(data=request.data)
        if platform.is_valid():
            platform.save()
            return Response(platform.data, status=status.HTTP_201_CREATED)
        return Response(platform.errors, status=status.HTTP_400_BAD_REQUEST)
    
class StreamPlatformDetailAV(APIView):
    def get(self, request, pk):
        try:
            platform = StreamPlatform.objects.get(pk=pk)
        except StreamPlatform.DoesNotExist:
            return Response({"error": "StreamPlatform not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = StreamPlatformSerializer(platform)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, pk):
        try:
            platform = StreamPlatform.objects.get(pk=pk)
        except StreamPlatform.DoesNotExist:
            return Response({"error": "StreamPlatform not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = StreamPlatformSerializer(platform, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        platform = StreamPlatform.objects.get(pk=pk)
        platform.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
