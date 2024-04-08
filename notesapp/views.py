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
        mynotes = Note.objects.filter(Q(allowed_users__contains=user.email) | Q(creator=user))
        mynotes = NoteContentSerializer(mynotes,many=True)
        return Response({'token':token.key ,'your notes':mynotes.data},status=status.HTTP_200_OK)
    else:
        return Response({'error':'invalid credentials'},status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def registerapi(request):
    myuser = RegisterSerializer(data = request.data)
    if(myuser.is_valid()):
        myuser.save()
        return Response(myuser.data , status=status.HTTP_201_CREATED)
    else:
        return Response(myuser.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def logoutapi(request):
    token = request.data.get('token')
    try:
        token_obj = Token.objects.get(key=token)
        token_obj.delete()  # Invalidate the token
        return Response({'message': 'Successfully logged out'})
    except Token.DoesNotExist:
        return Response({'error': 'Invalid token'}, status=status.HTTP_401_UNAUTHORIZED)


@api_view(['POST'])
def createnoteapi(request):
    token = request.data.get('token')
    token = Token.objects.get(key=token)
    user = token.user
    if not user:    return Response(status=status.HTTP_401_UNAUTHORIZED)
    data = request.data.copy()
    data.pop('token',None)
    mydata = Note.objects.create(title=data['title'],creator=user,timestamp=datetime.now(),content=data['content'],allowed_users=data['allowed_users'])
    mydata.save()
    return Response(NoteSerializer(mydata).data , status=status.HTTP_201_CREATED)

@api_view(['POST'])
def deletenoteapi(request):
    token = request.data.get('token')
    user = Token.objects.get(key=token).user
    id = int(request.data.get('id'))            #delete a note by using its id
    if not id:  
        return Response({"Error":"Include the id properly for deleting the note"},status=status.HTTP_400_BAD_REQUEST)
    mynote = Note.objects.get(pk=id)
    if not mynote:  
        return Response({"error":"Note does not exist"},status=status.HTTP_400_BAD_REQUEST)
    if(mynote.creator!=user):
        return Response({"Error":"You cannot delete this note ...you can only delete notes created by you!!"},status=status.HTTP_400_BAD_REQUEST)
    mynote.delete()
    return Response({"Note deleted successfully"},status=status.HTTP_200_OK)

@api_view(['POST'])
def updatenoteapi(request):
    token = request.data.get('token')
    user = Token.objects.get(key=token).user
    print(user,user.email)
    if not user:
        return Response({"Error":"Authentication required"},status=status.HTTP_401_UNAUTHORIZED)
    data = request.data.copy()
    data.pop('token',None)
    mynote = Note.objects.get(pk=data.get('id'))
    serializer = NoteSerializer(mynote,data=data,partial=True)
    if(serializer.is_valid()):
        serializer.save()
        return Response(serializer.data,status=status.HTTP_200_OK)
    else:
        return Response({"Error":"Note data incorrect"},status=status.HTTP_400_BAD_REQUEST)
    pass

