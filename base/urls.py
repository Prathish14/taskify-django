from django.urls import path
from . import views

urlpatterns=[

path('',views.signup,name="signup1"),
path('signin/',views.signin,name="signin1"),
path('signout/',views.signout,name="signout1"),
path('add1/',views.add_task,name="add1"),
path('list/',views.list_task,name="list1"),
path('del/<str:pk>',views.delete_task,name="delete1"),
path('update/<str:pk>',views.edit_task,name="edit1"),

]