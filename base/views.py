from django.shortcuts import render,redirect
from .add_task import TaskForm
from .models import Task
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout,authenticate
import requests
from django.contrib.auth.decorators import login_required

# Create your views here.

"""
Using requests module for getting data from api.
Sample api endpoint: http://127.0.0.1:8000/api/


        'api/'          :     'information',
        'list/'         :     'Task List',
        'list/:id/'     :     'Task details',
        'signup/'       :     'Create account',
        'login/'        :     'login to account',
        'mytasks/'      :     'indivisual user tasks',
        'mytasks/:id/'  :     'my task details',
        'update/:id/'   :     'update my tasks',
        'delete/:id/'   :     'delete my task'
        

Authentication : Token based authentication


"""
header_val ={}

base_url="http://127.0.0.1:8000/api/"

"""***********************************************************************************************************************"""

@login_required(login_url="signin1")
def add_task(request):
    global header_val
    
    if request.method=="GET":
        return render(request,'add_task.html')
    
    else:
        title=request.POST.get('title')
        desc=request.POST.get('desc')
        complete=request.POST.get('complete')

        url=base_url+'create/'

        creating=requests.post(url,headers=header_val,data={'title':title,'desc':desc,'complete':complete})

        if creating.status_code==200:
            return redirect('list1')
        else:
            return render(request,'add_task.html')




@login_required(login_url="signin1")
def list_task(request):
    global header_val
    print(header_val)
    url=base_url+'mytasks/'
    alltask=requests.get(url,headers=header_val)
    form=alltask.json()
    return render(request,'list_task.html',{'form':form})




@login_required(login_url="signin1")
def  edit_task(request,pk):
    global header_val

    if request.method=="GET":
        url = base_url+'mytasks/'+pk+'/'
        update_task1=requests.get(url,headers=header_val)
        form=update_task1.json()
        print(form)
        return render(request,'add_task.html',{'form':form})
    else:
        title=request.POST.get('title')
        desc=request.POST.get('desc')
        complete="True" if request.POST.get('complete') else "False"

        url=base_url+'update/'+pk+'/'
        update_task=requests.patch(url,headers=header_val,data={'title':title,'desc':desc,'complete':complete})

        if update_task.status_code==200:
            return redirect('list1')
        else:
            return redirect('list1')
        
    


@login_required(login_url="signin1")
def delete_task(request,pk):
    global header_val
    url=base_url+'delete/'+pk+'/'
    deleting=requests.delete(url,headers=header_val)

    if deleting.status_code==200:
        return redirect('list1')
    else:
        return redirect('list1')




def signup(request):
    global header_val

    if request.user.is_authenticated:
        return redirect('list1')

    if request.method=="GET":
        return render(request,'signup.html')
    else:
        username=request.POST.get('username')
        password1=request.POST.get('password1')
        password2=request.POST.get('password2')

        user_details={
            'username':username,
            'password1':password1,
            'password2':password2
        }

        url=base_url+"signup/"

        signup1=requests.post(url,data=user_details)

        if signup1.status_code==200:
            user=authenticate(username=username,password=password1)

            login(request,user)

            auth_token_json=signup1.json()
            token_val='Token '+ auth_token_json.get('token')
            header_val = {'authorization': token_val }

            return redirect('list1')
        else:
            return render(request,'signup.html')

        


def signin(request):
    url=base_url+'login/'

    global header_val

    if request.user.is_authenticated:
        return redirect('list1')

    if request.method=="GET":
         return render(request,'signin.html')
    else:
        username=request.POST['username']
        password=request.POST['password']

        signin=requests.post(url,data={'username':username,'password':password})

        if signin.status_code == 200:

            auth_token_json=signin.json()
            token_val='Token '+ auth_token_json.get('token')
            header_val = {'authorization': token_val }

            user=authenticate(username=username,password=password)
            login(request,user)
            return redirect('list1')
        
        else:
            print("Some error occured")
            return render(request,'signin.html')




@login_required(login_url="signin1")
def signout(request):

    global header_val
    header_val={'authorization':''}
    print(header_val)
    logout(request)
    
    return redirect('signup1')
    

    

