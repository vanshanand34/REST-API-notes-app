from rest_framework import generics
from django.contrib.auth.models import User
from .models import Note
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.decorators import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .serializers import NoteSerializer , TempNoteSerializer , NotePagination ,UserSerializer
from django.contrib.auth import authenticate , login , logout 
# Create your views here.
from datetime import datetime
from rest_framework import viewsets


class RegisterApi(generics.CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = TempNoteSerializer
    pagination_class = NotePagination
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

class NoteListView(generics.ListCreateAPIView):
    serializer_class = TempNoteSerializer
    pagination_class = NotePagination
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save(creator = self.request.user)
            return Response(serializer.data)
        else:
            return serializer.errors()
        
    def get_queryset(self):
        obj = Note.objects.filter(creator = self.request.user)
        return obj

class NoteEdit(generics.RetrieveUpdateDestroyAPIView):
    
    serializer_class = TempNoteSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    def get_queryset(self):
        obj = Note.objects.filter(creator = self.request.user)
        return obj

class Login(APIView):
    def post(self,request):
        username = request.data['username']
        password = request.data['password']
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            token , _= Token.objects.get_or_create(user = request.user)
            return Response({"message":"User loggedin successfully","token":token.key})
        return Response({"Invalid credentials!!!!!!"})
    
class Logout(APIView):
    def get(self,request):
        if request.user.is_authenticated():
            logout(request.user)
            token , _ = Token.objects.delete(user = request.user)
            return Response({"Logged out successfully!!!!1"})
        return Response({"You need to be logged in first to logout"})