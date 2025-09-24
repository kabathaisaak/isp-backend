from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializers import UserSerializer
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.contrib.auth import authenticate, login 
from django.contrib.auth import get_user_model
User = get_user_model()
from rest_framework import status

class UserMe(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)

class ActiveUsers(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        users = User.objects.filter(is_active=True)
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

class TokenObtainPair(TokenObtainPairView):
    # Custom logic can be added here if needed
    pass

class TokenRefresh(TokenRefreshView):
    # Custom logic can be added here if needed
    pass

from rest_framework import status

class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get('username')
        email = request.data.get('email')
        password = request.data.get('password')

        if not username:
            return Response({'error': 'Username required'}, status=status.HTTP_400_BAD_REQUEST)
        if not email:
            return Response({'error': 'Email required'}, status=status.HTTP_400_BAD_REQUEST)
        if not password:
            return Response({'error': 'Password required'}, status=status.HTTP_400_BAD_REQUEST)

        if User.objects.filter(username=username).exists():
            return Response({'error': 'Username already exists'}, status=status.HTTP_400_BAD_REQUEST)
        if User.objects.filter(email=email).exists():
            return Response({'error': 'Email already exists'}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        if not username or not password:
            return Response(
                {"error": "Username and password are required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)  # ✅ sets the session cookie
            serializer = UserSerializer(user)
            return Response(
                {"message": "Login successful", "user": serializer.data},
                status=status.HTTP_200_OK
            )

        return Response(
            {"error": "Invalid credentials"},
            status=status.HTTP_401_UNAUTHORIZED
        )

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        logout(request)
        return Response({"message": "Logged out"}, status=status.HTTP_200_OK)
