from django.urls import path
from . import views
                    
urlpatterns = [
    path('', views.index),
    path('process', views.create),
    path('process2', views.login),
    path('login', views.log),
    path('category/<int:id>', views.show),
    path('logoff', views.reset),
    path('category/<int:x>/<int:y>', views.show2),
    path('category/<int:a>/<int:b>/<int:c>', views.review),
    path('process3', views.create_review),
    path("contact", views.contact),
    path("about", views.about),
    path("services",views.services),
    path('comment/<int:k>', views.comment),
    path('delete/<int:id>',views.del_review),
]