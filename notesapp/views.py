from django.shortcuts import render
from django.db.models import Q
from django.contrib.auth import login , logout , authenticate
from django.contrib.auth.models import User
from datetime import datetime
from .models import Note
from .serializer import UserSerializer , NoteSerializer , NoteContentSerializer , RegisterSerializer
from rest_framework.decorators import api_view , permission_classes 
from functools import wraps
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
        # if(not myuser.is_valid()):  return Response(mydata.errors,status=status.HTTP_400_BAD_REQUEST
        mynotes = Note.objects.filter(Q(allowed_users__contains=user.email) | Q(creator=user))
        mynotes = NoteContentSerializer(mynotes,many=True)
        # mydata = NoteContentSerializer(mydata)
        # if(mynotes.is_valid() and mydata.is_valid()):
        # else:   return Response(mynotes.data,status=status.HTTP_400_BAD_REQUEST)
        # mynotes = []
        # print(mydata,myuser.data)
        # for i in mydata:
        #     for myemail in i.allowed_users.strip().split(','):
        #         if myemail == myuser.data['email']:
        #             mynotes.append(i)
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
    token = request.data.get('token')
    token = Token.objects.get(key=token)
    user = token.user
    data = request.data.copy()
    data.pop('token',None)
    # print(data)
    mydata = Note.objects.create(title=data['title'],creator=user,timestamp=datetime.now(),content=data['content'],allowed_users=data['allowed_users'])
    mydata.save()
    # print(mydata.allowed_users)
    return Response(NoteSerializer(mydata).data , status=status.HTTP_201_CREATED)

@api_view(['POST'])
def deletenoteapi(request):
    #delete a note by using its id
    id = int(request.data.get('id'))
    print(id,type(id))
    if not id:
        return Response({"Error":"Include the id properly for deleting the note"},status=status.HTTP_400_BAD_REQUEST)
    mynote = Note.objects.get(pk=id)
    print(mynote)
    if not mynote:
        return Response({"error":"Note does not exist"},status=status.HTTP_400_BAD_REQUEST)
    mynote.delete()
    return Response({"Note deleted successfully"},status=status.HTTP_200_OK)

@api_view(['POST'])
def updatenoteapi():

    pass

