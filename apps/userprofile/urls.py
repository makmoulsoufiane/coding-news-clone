from django.urls import path

from .views import userprofile


urlpatterns = [
    
    path('<str:username>/', userprofile, name='userprofile'),

]
