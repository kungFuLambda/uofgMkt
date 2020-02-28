from django.urls import path 
from glasmarket import views 

app_name = 'glasmarket'

urlpatterns = [
    path('',views.index,name='index'),
]