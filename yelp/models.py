from django.db import models
import re

class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['first_name']) < 2:
            errors["first_name"] = "First name should be at least 2 characters"
        if len(postData['last_name']) < 2:
            errors["last_name"] = "Last name should be at least 2 characters"
        if len(postData['email'])<0:
            errors['email']='Email is required'
        if len(postData['password'])<8:
            errors['password']="Password must be longer than 8 characters"
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):               
            errors['email'] = "Invalid email address!"
        if User.objects.filter(email = postData['email']).exists():
            errors['email']= "Email already exists"
        if postData['password'] != postData['confirm_password']:
            errors['password']="Passwords don't match"
        return errors
    
class CategoryManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['name']) < 4 :
            errors['name']='Category name should be at least 2 characters'
        return 
    
class LocationManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['city']) < 2 : 
            errors ['city'] = "City name should be at least 2 characters"
        if len(postData['neighboorhood']) < 2 :
            errors['neighboorhood'] = " Neighborhood name should be at least 2 characters"
        return errors    

class BusinessManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['name']) < 2 :
            errors['name'] = "Name should be at least 2 characters"
        if len(postData['description']) < 10 :
            errors['description'] = "Description should be at least 10 characters"
        if len(postData['phone']) < 5 :
            errors['phone']= "Phone should be at least 5 characters"
        return errors
    
class CommentManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['content']) < 4:
            errors['content'] = "Content should be at least 10 characters"
        return errors
    
class ReviewManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['content']) < 10 :
            errors['content'] = "Rating should be at least 5 characters"
        if len(postData['rating']) < 1 :
            errors['rating'] = "Rating should be at least 1 character"
        return errors

        
class User(models.Model):
    first_name=models.CharField(max_length=45)
    last_name=models.CharField(max_length=45)
    email=models.CharField(max_length=45, unique=True)
    password=models.CharField(max_length=45)
    user_level=models.SmallIntegerField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects=UserManager()
    
class BusinessCategory(models.Model):
    name=models.CharField(max_length=45)
    users=models.ForeignKey(User,related_name="categories", on_delete=models.CASCADE)
    image_url=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects=CategoryManager()
    
class Location (models.Model):
    city=models.CharField(max_length=45)
    neighborhood=models.CharField(max_length=45)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects=LocationManager()
    
class Speciality (models.Model):
    name=models.CharField(max_length=45)
    image_url=models.TextField()
    category=models.ForeignKey(BusinessCategory,related_name="speciality",on_delete=models.CASCADE, null=True )
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    
class BusinessDetail(models.Model):
    name=models.CharField(max_length=45)
    description=models.TextField(null=True)
    business_hours=models.CharField(max_length=45, default="")
    image_url=models.CharField(max_length=255,null=True)
    phone=models.IntegerField()
    category=models.ForeignKey(BusinessCategory,related_name="business",on_delete=models.CASCADE)
    speciality=models.CharField(max_length=45)
    users=models.ManyToManyField(User,related_name="details", through="Review")
    location=models.ForeignKey(Location,related_name="details", on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects=BusinessManager()

    
class Review(models.Model):
    user=models.ForeignKey(User,related_name="reviews", on_delete=models.CASCADE)
    detail=models.ForeignKey(BusinessDetail,related_name="reviews", on_delete=models.CASCADE)
    content=models.TextField()
    rating=models.SmallIntegerField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects=ReviewManager()
    
class Comment(models.Model):
    content=models.TextField()
    user=models.ForeignKey(User,related_name="comments", on_delete=models.CASCADE)
    review=models.ForeignKey(Review,related_name="comments", on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects=CommentManager()
    

    



    
    
    
    
