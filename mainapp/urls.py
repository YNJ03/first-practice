from django.urls import path

from . import views

urlpatterns = [
    
    # - http://127.0.0.1:8000/
    path('', views.Index),
    
    # - http://127.0.0.1:8000/index/
    path('index/', views.Index),
    
    # - http://127.0.0.1:8000/index.html/
    path('index.html/', views.Index),    
]