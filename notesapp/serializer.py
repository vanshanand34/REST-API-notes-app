from rest_framework import serializers
from .models import Note
from django.contrib.auth.models import User

from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password


#Serializer to Register User
#helps in easy resgistration
class RegisterSerializer(serializers.ModelSerializer):
  email = serializers.EmailField(required=True,validators=[UniqueValidator(queryset=User.objects.all())])
  password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
  password2 = serializers.CharField(write_only=True, required=True)
  class Meta:
    model = User
    fields = ('username', 'password', 'password2','email', 'first_name', 'last_name')
    extra_kwargs = {'first_name': {'required': True},'last_name': {'required': True}}
  def validate(self, attrs):
    if attrs['password'] != attrs['password2']:
      raise serializers.ValidationError({"password": "Password fields didn't match."})
    return attrs
  def create(self, validated_data):
    user = User.objects.create(
      username=validated_data['username'],
      email=validated_data['email'],
      first_name=validated_data['first_name'],
      last_name=validated_data['last_name']
    )
    user.set_password(validated_data['password'])
    user.save()
    return user

#use to convert user objects into json type
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','email','username')

#serailizer for note objects
class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ('title','id','content','allowed_users')
    def update(self, instance, validated_data):
      instance.title = validated_data.get('title', instance.title)  # Use existing value if not provided
      instance.content = validated_data.get('content', instance.content)
      instance.allowed_users =  validated_data.get('allowed_users', instance.allowed_users)
      instance.save()
      return instance

#used to return a note to the user with data that is necessary for the user
#not included the alowed users , timestamp fields as they are not of that much importance
class NoteContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ('title' , 'content')