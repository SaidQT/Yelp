from django.urls import path
from . import views
                    
urlpatterns = [
    path('', views.index),
    path('process', views.create),
    path('process2', views.login),
    path('login', views.log),
    path('category/<int:id>', views.show),
    path('delete', views.reset),
    path('category/<int:x>/<int:y>', views.show2),
]