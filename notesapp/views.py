from django.shortcuts import render
from django.contrib.auth import login , logout , authenticate
from django.contrib.auth.models import User
from datetime import datetime
from .models import Note , MyUser
from .serializer import UserSerializer , NoteSerializer , NoteContentSerializer , RegisterSerializer
from rest_framework.decorators import api_view , permission_classes
from rest_framework.response import Response 
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token

# Create your views here.
@api_view(['POST'])
def loginapi(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(request,username=username,password=password)
    if user is not None:
        login(request,user)
        token , created = Token.objects.get_or_create(user=user)
        myuser = MyUser(user=user)
        myuser = UserSerializer(myuser)
        mydata = Note.objects.all()
        mynotes = []
        print(mydata,myuser.data)
        for i in mydata:
            for myemail in i.allowed_users.strip().split(','):
                if myemail == myuser.data['email']:
                    mynotes.append(i)
        mynotes = NoteContentSerializer(mydata , many=True)
        return Response({'token':token.key ,'your notes':mynotes.data},status=status.HTTP_200_OK)
    else:
        return Response({'error':'invalid credentials'})

@api_view(['POST'])
def registerapi(request):
    myuser = RegisterSerializer(data = request.data)
    if(myuser.is_valid()):
        myuser.save()
        return Response(myuser.data , status=status.HTTP_201_CREATED)
    else:
        return Response(myuser.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def logoutapi(request):
    logout(request)


@api_view(['POST'])
def createnoteapi(request):
    if(not request.user.is_authenticated()):    return Response({"Loggin required to create a note"},status=status.HTTP_400_BAD_REQUEST)
    myuser = UserSerializer(data = request.user)
    mydata = request.data
    mydata = NoteSerializer(data = mydata)
    if(mydata.is_valid()):
        mydata.data['timestamp'] = datetime.now()
        mydata.data['email'] = myuser.email  
        mydata.save()
        return Response(mydata.data , status=status.HTTP_201_CREATED)
    else:
        return Response(mydata.errors,status=status.HTTP_400_BAD_REQUEST)
    pass

@api_view(['POST'])
def deletenoteapi():
    pass

@api_view(['POST'])
def updatenoteapi():
    pass

