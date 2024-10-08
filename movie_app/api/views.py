from rest_framework.decorators import api_view
from rest_framework.response import Response

from movie_app.api.serializers import MovieSerializer
from movie_list.models import Movie


@api_view()
def movies_list(request):
    movies = Movie.objects.all()
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)


@api_view()
def movie_list(request, pk):
    movie = Movie.objects.get(pk=pk)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)
