from rest_framework.views import status, APIView, Request, Response
from .models import Movie
from .serializers import MovieSerializer, MovieOrderSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.shortcuts import get_object_or_404
from users.permissions import IsEmployee
from rest_framework.pagination import PageNumberPagination

from rest_framework.permissions import IsAuthenticated


class MovieView(APIView, PageNumberPagination):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsEmployee]

    def get(self, request: Request) -> Response:
        movies = Movie.objects.all()
        result_page = self.paginate_queryset(movies, request)
        serializer = MovieSerializer(result_page, many=True)
        return self.get_paginated_response(serializer.data)

    def post(self, request: Request) -> Response:
        serializer = MovieSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class MovieDetailedView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsEmployee]

    def get(self, request: Request, pk: int) -> Response:
        movie = get_object_or_404(Movie, pk=pk)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)

    def patch(self, request: Request, pk: int) -> Response:
        movie = get_object_or_404(Movie, pk=pk)
        serializer = MovieSerializer(movie, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request: Request, pk: int) -> Response:
        movie = get_object_or_404(Movie, pk=pk)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class MovieOrderView(APIView):
    authentication_classes = [JWTAuthentication]  # decodificação do token
    permission_classes = [IsAuthenticated]

    def post(self, request: Request, movie_id: int) -> Response:
        movie = get_object_or_404(Movie, pk=movie_id)
        serializer = MovieOrderSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(title=movie, buyed_by=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
