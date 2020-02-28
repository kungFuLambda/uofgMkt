from django.urls import path 
from glasmarket import views 

app_name = 'glasmarket'

urlpatterns = [
    path('',views.home,name='index'),
    path('glasmarket',views.home,name="index"),
    path('home/',views.home,name="index"),
    path('about/',views.about,name='about'),
    path('market/',views.market,name='market'),
    
]