from django.shortcuts import render, redirect
from . models import *
from django.contrib import messages
import bcrypt

def index(request):
    context={
        "categories": BusinessCategory.objects.all(),
    }
    return render(request, 'index2.html', context)

def create(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value,extra_tags="fail")
        return redirect('/login')
    else:
        password = request.POST['password']
        pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        print (pw_hash)
        if request.method == "POST":
            user=User.objects.create(
                first_name=request.POST['first_name'],
                last_name=request.POST['last_name'],
                email=request.POST['email'],
                password=pw_hash,
                user_level=0,
                )
            request.session['userid'] = user.id
    return redirect('/')

def login(request):
    email = User.objects.filter(email=request.POST['email']) 
    if email: 
        logged_email = email[0] 
        if bcrypt.checkpw(request.POST['password'].encode(), logged_email.password.encode()):
            request.session['userid'] = logged_email.id
            return redirect('/login')
    messages.error(request, "The password or email you entered is incorrect",extra_tags="login")
    return redirect("/")

def log(request):
    return render(request,'login.html')

def show(request,id):
    category_x=BusinessCategory.objects.get(id=id)
    data={
        "speciality":Speciality.objects.filter(category=category_x)
    }
    
    return render(request,"category.html",data)

def reset(request):
    request.session.clear()
    return redirect("/")

