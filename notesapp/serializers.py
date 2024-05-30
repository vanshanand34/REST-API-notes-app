from rest_framework import serializers
from rest_framework.pagination import  PageNumberPagination
from .models import Note
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from rest_framework import permissions

# class TokenPermission(permissions.BasePermission):
#     print("inside")
#     def has_permission(self, request, view):
#         print("insd")
#         user,created = Token.objects.get_or_create(user=request.user)
#         if user:
#             return True
#         return False


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','password']
        extra_kwargs = {'password':{'write_only':True}}
        partial=True

    def create(self,validated_data):
        user = User.objects.create_user(**validated_data)
        print(user)
        return user
    
class NotePagination(PageNumberPagination):
    page_size = 2
    max_page_size = 4
    page_size_query_param = 'page_size'

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ('__all__')
        depth = 1
        partial = True

class TempNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ("title","content","timestamp","id","allowed_users")
        partial = True

