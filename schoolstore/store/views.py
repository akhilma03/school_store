from django.shortcuts import render
from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import NewEntryForm
from . models import *

# Create your views here.
def index(request):
    departments=Department.objects.all()
    context={
        'departments':departments
    }
    return render(request,'store/main.html',context)

def home(request):
    return render(request,'store/home2.html')


def userlogin(request):  
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
                auth.login(request, user)           
                return redirect('home2')  
               
        else:
            messages.success(request,("Enter  Username and Password Correctly...."))  
            return redirect('login')  
        # Return an 'invalid login' error message.
       
    else:
        return render(request,'store/login.html')
    
    
def usersignup(request): 

    if request.method == 'POST':
        first_name = request.POST['first_name'] 
        last_name = request.POST['last_name'] 
        username = request.POST['username'] 
        email = request.POST['email'] 
        password1 = request.POST['password1'] 
        password2 = request.POST['password2'] 


        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username Already Exist')
                return redirect('signup')

            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email Already Exist')
                return redirect('signup')
        
            else:
                if username == '' and password1 == '' :
                    messages.info(request,'Enter All Fields to Continue')
                    return redirect ('signup')
                else:

                    user = User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
                    user.save()
                    messages.info(request,'User Created Sucessfully')
                    return redirect( 'login' ) 

        else:
            messages.info(request,'Password Not Matching')
            return redirect('signup')
        
        
    return render(request,'store/signnup.html')        

def newentry(request):
    form = NewEntryForm()
    if request.method == 'POST':
        form = NewEntryForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'store/sucess.html')
    
    else:
        form = NewEntryForm()    
        
        
    context = {
        'form': form
    }
    return render(request, 'store/Formentry.html', context)    

def load_course(request):
    department_id=request.GET.get('department')
    courses=Course.objects.filter(department_id=department_id).order_by('Name')
    return render(request,'store/course_dropdown.html',{'courses':courses})
