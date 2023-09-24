from django.urls import path
from .views import MovieView, MovieDetailedView, MovieOrderView
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path("movies/", MovieView.as_view()),
    path("movies/<int:movie_id>/orders/", MovieOrderView.as_view()),
    path("movies/<int:pk>/", MovieDetailedView.as_view()),
]
