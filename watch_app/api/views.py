# from rest_framework import mixins
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from watch_app.api.serializers import WatchListSerializer, StreamPlatformSerializer, ReviewSerializer
from watch_list.models import WatchList, StreamPlatform, Reviews


class ReviewList(generics.ListCreateAPIView):
    queryset = Reviews.objects.all()
    serializer_class = ReviewSerializer

class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reviews.objects.all()
    serializer_class = ReviewSerializer

# class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Reviews.
# class ReviewList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
#     queryset = Reviews.objects.all()
#     serializer_class = ReviewSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
#
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, *kwargs)


class WatchListAV(APIView):
    def get(self, request):
        try:
            content_names = WatchList.objects.all()
        except WatchList.DoesNotExist:
            return Response({'error': 'Not Found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = WatchListSerializer(content_names, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = WatchListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class WatchDetailAV(APIView):
    def get(self, request, pk):
        try:
            content_name = WatchList.objects.get(pk=pk)
        except WatchList.DoesNotExist:
            return Response({'error': 'Not Found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = WatchListSerializer(content_name)
        return Response(serializer.data)

    def put(self, request, pk):
        content_name = WatchList.objects.get(pk=pk)
        serializer = WatchListSerializer(content_name, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({'Not Valid Data'}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            content_name = WatchList.objects.get(pk=pk)
        except WatchList.DoesNotExist:
            return Response({'error': 'Content Not Found'}, status=status.HTTP_404_NOT_FOUND)
        else:
            content_name.delete()
            return Response({'message': 'Content deleted'}, status=status.HTTP_204_NO_CONTENT)


class StreamPlatformAV(APIView):
    def get(self, request):
        try:
            platforms_names = StreamPlatform.objects.all()
        except StreamPlatform.DoesNotExist:
            return Response({'No Data Found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = StreamPlatformSerializer(platforms_names, many=True, context={'request': request})
        return Response(serializer.data)

    def post(self, request):
        serializer = StreamPlatformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PlatformAV(APIView):
    def get(self, request, pk):
        try:
            platform_name = StreamPlatform.objects.get(pk=pk)
        except StreamPlatform.DoesNotExist:
            return Response({'Not Found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = StreamPlatformSerializer(platform_name)
        return Response(serializer.data)

    def put(self, request, pk):
        try:
            platform_name = StreamPlatform.objects.get(pk=pk)
        except StreamPlatform.DoesNotExist:
            return Response({'Not Found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = StreamPlatformSerializer(platform_name, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        try:
            platform_name = StreamPlatform.objects.get(pk=pk)
        except StreamPlatform.DoesNotExist:
            return Response({'Not Found'}, status=status.HTTP_404_NOT_FOUND)
        platform_name.delete()
        return Response({'Deleted'}, status=status.HTTP_200_OK)

# from rest_framework.decorators import api_view
# @api_view(['GET', 'POST'])
# def movies_list(request):
#     if request.method == "GET":
#         try:
#             movies = Movie.objects.all()
#         except Movie.DoesNotExist:
#             return Response({'error': 'Movie Not Found'}, status=status.HTTP_404_NOT_FOUND)
#
#         serializer = MovieSerializer(movies, many=True)
#         return Response(serializer.data)
#     if request.method == "POST":
#         serializer = MovieSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)
#
#
# @api_view(['GET', 'PUT', 'DELETE'])
# def watch_list(request, pk):
#     if request.method == 'GET':
#         try:
#             movie = Movie.objects.get(pk=pk)
#         except Movie.DoesNotExist:
#             return Response({'error': 'Movie Not Found'}, status=status.HTTP_404_NOT_FOUND)
#         else:
#             serializer = MovieSerializer(movie)
#             return Response(serializer.data)
#     if request.method == 'PUT':
#         movie = Movie.objects.get(pk=pk)
#         serializer = MovieSerializer(movie, request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         else:
#             return Response({'Not Valid data'}, status=status.HTTP_400_BAD_REQUEST)
#     if request.method == 'DELETE':
#         try:
#             movie = Movie.objects.get(pk=pk)
#         except Movie.DoesNotExist:
#             return Response({'error': 'Movie Not Found'}, status=status.HTTP_404_NOT_FOUND)
#         else:
#             movie.delete()
#             return Response({'message': 'Movie deleted'}, status=status.HTTP_204_NO_CONTENT)
#
#
