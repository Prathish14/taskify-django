from base.models import Task
from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"

class MyTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id','title','desc','complete','date']

class TaskCreationSerializer(serializers.ModelSerializer):
    class Meta:
        model=Task
        fields=['title','desc','complete']

class UserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['username','password']

class UserCreationSerializer(UserCreationForm):
    class Meta:
        model=User
        fields=['username','password1','password2']


