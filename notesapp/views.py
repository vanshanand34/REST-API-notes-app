from django.shortcuts import render
from django.contrib.auth import login , logout , authenticate
from django.contrib.auth.models import User


from rest_framework.decorators import api_view , permission_classes
from rest_framework.response import Response 
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token

# Create your views here.
def loginapi():

    pass

def registerapi():
    pass

def logoutapi():
    pass

def createnoteapi():
    pass

def deletenoteapi():
    pass

def updatenoteapi():
    pass

