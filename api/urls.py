from django.urls import path,include
from . import views

from rest_framework import routers

from rest_framework.authtoken import views as viewdefault






urlpatterns = [
    path('',views.AllDetails,name="ahome"),
    path('list/',views.TaskList.as_view(),name="alist"),
    path('list/<str:pk>/',views.TaskDetail.as_view(),name="adetail"),
    path('mytasks/',views.UserSpecificTasks.as_view(),name="amytasks"),
    path('mytasks/<str:pk>/',views.UserTaskDetails.as_view(),name="amydetail"),
    path('create/',views.TaskCreation.as_view(),name="acreate"),
    path('update/<str:pk>/',views.TaskUpdate.as_view(),name="aupdate"),
    path('delete/<str:pk>/',views.TaskDelete.as_view(),name="adelete"),
    path('login/',viewdefault.obtain_auth_token,name="login1"),
    path('signup/',views.CreateAccount.as_view(),name="asignup"),
    
    
]

