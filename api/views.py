from django.shortcuts import render
from django.http import HttpResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from base.models import Task
from .serializers import TaskSerializer,MyTaskSerializer,TaskCreationSerializer,UserLoginSerializer,UserCreationSerializer

from rest_framework import permissions, viewsets
from django.contrib.auth.models import User
from django.http import Http404

from rest_framework import status
from .custom_permessions import IsObjectOwnerOrReject

# Create your views here.


#Writing a class based views
from rest_framework.views import APIView

from rest_framework import mixins
from rest_framework import generics

from rest_framework.permissions import BasePermission, IsAuthenticated,AllowAny
from rest_framework.authtoken.models import Token

from django.contrib.auth import login,logout,authenticate

from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import Http404
from rest_framework.throttling import UserRateThrottle,AnonRateThrottle


@api_view(['GET'])
def AllDetails(request):

    dicts = {

        'api/'          :     'information',
        'list/'         :     'Task List',
        'list/:id/'     :     'Task details',
        'signup/'       :     'Create account',
        'login/'        :     'login to account',
        'mytasks/'      :     'indivisual user tasks',
        'mytasks/:id/'  :     'my task details',
        'update/:id/'   :     'update my tasks',
        'delete/:id/'   :     'delete my task'

    }

    return Response(dicts)



class TaskList(generics.ListAPIView):
    throttle_scope = 'burst'
    queryset=Task.objects.all()
    serializer_class=TaskSerializer

class TaskDetail(generics.RetrieveAPIView):
    throttle_scope = 'simple'
    queryset=Task.objects.all()
    serializer_class=TaskSerializer



class UserSpecificTasks(APIView):
    permission_classes=[IsAuthenticated]
    
    
    def get(self,request,format=None):
        queryset=Task.objects.filter(user=request.user)
        serialize=MyTaskSerializer(queryset,many=True).data
        return Response(serialize)

class UserTaskDetails(APIView):
    permission_classes=[IsAuthenticated,IsObjectOwnerOrReject]
    
    
    def get(self,request,pk,format=None):
        queryset=Task.objects.get(id=pk)
        self.check_object_permissions(request, queryset)
        serialize=MyTaskSerializer(queryset,many=False).data
        return Response(serialize)
    

    
class TaskCreation(APIView):
    permission_classes=[IsAuthenticated]
    
    def post(self,request,format=None):
        serializer=TaskCreationSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data)
        else:
            return Response("Something went wrong",status=400)
        


class TaskUpdate(APIView):
    
    permission_classes=[IsAuthenticated,IsObjectOwnerOrReject]
    
    def patch(self,request,pk,format=None):
        queryset=Task.objects.get(id=pk)
        self.check_object_permissions(request, queryset)
        serializer=TaskCreationSerializer(queryset,data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data)
        else:
            return Response("Some Error",status=400)
        


class TaskDelete(APIView):
    permission_classes=[IsAuthenticated,IsObjectOwnerOrReject]

    def delete(self,request,pk,format=None):
        queryset=Task.objects.get(id=pk)
        self.check_object_permissions(request, queryset)
        queryset.delete()
        return Response("Delete Successs",status=200)


"""class Logout(APIView):
    permission_classes=[IsAuthenticated]
    
    def get(self, request, format=None):
        # simply delete the token to force a login
        request.user.auth_token.delete()
        return Response("log out success",status=status.HTTP_200_OK)"""

class CreateAccount(APIView):

    def post(self,request,format=None):

        serializer=UserCreationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            username= serializer.data['username']
            password= serializer.data['password1']

            user=authenticate(username=username,password=password)

            tokenvalue=Token.objects.get(user=user)
            dict1={'token':tokenvalue.key}

            return Response(dict1,status=200)
        else:
            return Response("Error!!! Try again",status=400)
    





   
    

    







    
