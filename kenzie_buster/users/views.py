from rest_framework.views import APIView, status, Response, Request
from .models import User
from .serializers import UserSerializer, LoginSerializer
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from .permissions import IsAuthenticatedUser
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.shortcuts import get_object_or_404

# Create your views here.


class UserView(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request: Request) -> Response:
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class UserDetailedView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedUser]

    def get(self, request: Request, pk: int) -> Response:
        user = get_object_or_404(User, id=pk)
        if not request.user.is_employee and pk != request.user.id:
            return Response(status=status.HTTP_403_FORBIDDEN)

        serializer = UserSerializer(user, data=request.data, partial=True)

        serializer.is_valid(raise_exception=True)
        return Response(serializer.data)

    def patch(self, request: Request, pk: int) -> Response:
        user = get_object_or_404(User, id=pk)
        if not request.user.is_employee and pk != request.user.id:
            return Response(status=status.HTTP_403_FORBIDDEN)

        serializer = UserSerializer(user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)

        serializer.save()
        return Response(serializer.data)
