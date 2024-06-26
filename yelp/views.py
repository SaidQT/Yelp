from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpRequest
from . models import *
import bcrypt



def contactus(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = request.POST.get('subject')
            email = request.POST.get('email')
            message = request.POST.get('message')
            name = request.POST.get('name')

            body=f"his name {name}\n his {email} \n his{message}"
            # Send email notification
            send_mail(
                'New message from website contact form',
                body,
                email,
                ['ranni.tawasha@gmail.com'],
                fail_silently=False,
            )
            return render(request, 'contact_success.html')
    else:
        form = ContactForm()
    return render(request, 'contact_us.html', {'form': form})



def index(request):
    context={
        "categories": BusinessCategory.objects.all(),
        "reviews": Review.objects.all().order_by("-created_at"),
    }
    return render(request, 'index2.html', context)


def get_recent_reviews(request):
    recent_reviews = Review.objects.order_by('-updated_at')[:10]  
    

    reviews_data = [{
        'image_url': review.detail.image_url,
        'category_name': review.detail.name,
        'content': review.content,
        'rating': review.rating,
        'user_name': f'{review.user.first_name} {review.user.last_name}',
        'updated_at': review.updated_at.strftime('%Y-%m-%d %H:%M:%S')  
    } for review in recent_reviews]
    
    return JsonResponse({'reviews': reviews_data})




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
    request.session['name']=business.name
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
    return redirect(f"/login")

def create_review(request):
    if request.method == "POST" and 'userid' in request.session:
        user = User.objects.get(id=request.session['userid'])
        business = BusinessDetail.objects.get(id=request.session['bus'])
        
        a = request.session['a']
        b = request.session['b']
        c = request.session['c']
        errors = Review.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value,extra_tags="rev")
                return redirect(f'/category/{a}/{b}/{c}')
        else:
            Review.objects.create(
                user=user,
                detail=business,
                content=request.POST['review'],
                rating=request.POST['rating'],
            )
            return redirect(f'/category/{a}/{b}/{c}')

def contact(request):
    return render(request,"contact_us.html")

def about(request):
    return render(request, "about.html")

def services(request):
    return render(request,'services.html')

def comment(request,k):
    if request.method == "POST":
        errors = Comment.objects.basic_validator(request.POST)
        a = request.session['a']
        b = request.session['b']
        c = request.session['c']
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value,extra_tags="com")
                return redirect(f'/category/{a}/{b}/{c}')
        Comment.objects.create(
            content=request.POST['content'],
            user=User.objects.get(id=request.session['userid']),
            review=Review.objects.get(id=k),
        )
    
        return redirect(f'/category/{a}/{b}/{c}')
    
def del_review(request,id):
    review_x=Review.objects.get(id=id)
    review_x.delete()
    a = request.session['a']
    b = request.session['b']
    c = request.session['c']
    return redirect(f'/category/{a}/{b}/{c}')


def get_recent_reviews(request):

    recent_reviews = Review.objects.order_by('-updated_at')[:8] 
    
    reviews_data = [{
        'image_url': review.detail.image_url,
        'category_name': review.detail.name,
        'content': review.content,
        'rating': review.rating,
        'user_name': f'{review.user.first_name} {review.user.last_name}',
        'updated_at': review.updated_at.strftime('%Y-%m-%d %H:%M:%S')  
    } for review in recent_reviews]
    
    return JsonResponse({'reviews': reviews_data})


def reset(request):
    request.session.clear()
    return redirect("/")