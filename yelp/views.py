from django.shortcuts import render, redirect
from . models import *
from django.contrib import messages
import bcrypt

def index(request):
    context={
        "categories": BusinessCategory.objects.all(),
        "reviews": Review.objects.all().order_by("-created_at")
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
            return redirect('/')
    messages.error(request, "The password or email you entered is incorrect",extra_tags="login")
    return redirect("/login")

def log(request):
    return render(request,'login.html')

def show(request,id):
    category_x=BusinessCategory.objects.get(id=id)
    data={
        "speciality":Speciality.objects.filter(category=category_x)
    }
    
    return render(request,"category.html",data)


def show2(request,x,y):
    speaciality_x=Speciality.objects.get(id=y)
    data={
        "category_x":BusinessCategory.objects.get(id=x),
        "business":BusinessDetail.objects.filter(speciality=speaciality_x),
    }
    return render(request,"business.html",data)


def review(request, a, b, c):
    business = BusinessDetail.objects.get(id=c)
    request.session['bus'] = business.id
   
    data = {
        "category1": BusinessCategory.objects.get(id=a),
        "spec": Speciality.objects.get(id=b),
        "reviews": Review.objects.filter(detail=business).order_by("-updated_at"),
    }
    request.session['a'] = a
    request.session['b'] = b
    request.session['c'] = c
    if 'userid' in request.session:
        return render(request, "wall.html", data)
    return redirect(f"/category/{a}/{b}")

def create_review(request):
    if request.method == "POST" and 'userid' in request.session:
        user = User.objects.get(id=request.session['userid'])
        business = BusinessDetail.objects.get(id=request.session['bus'])
        a = request.session['a']
        b = request.session['b']
        c = request.session['c']
        
        Review.objects.create(
            user=user,
            detail=business,
            content=request.POST['review'],
            rating=request.POST['rating'],
        )
        return redirect(f'/category/{a}/{b}/{c}')
    else:
        return redirect('/login')

def contact(request):
    return render(request,"contact_us.html")

def about(request):
    return render(request, "about.html")

def services(request):
    return render(request,'services.html')

def comment(request,k):
    if request.method == "POST":
        Comment.objects.create(
            content=request.POST['content'],
            user=User.objects.get(id=request.session['userid']),
            review=Review.objects.get(id=k),
        )
        a = request.session['a']
        b = request.session['b']
        c = request.session['c']
        return redirect(f'/category/{a}/{b}/{c}')
    

def reset(request):
    request.session.clear()
    return redirect("/")