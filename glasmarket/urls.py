from django.urls import path 
from glasmarket import views 

app_name = 'glasmarket'

urlpatterns = [
    #BASIC PATTERS
    path('',views.home,name='index'),
    path('glasmarket',views.home,name="index"),
    path('home/',views.home,name="index"),
    path('about/',views.about,name='about'),

    #PROFILE PATTERN
    path('profile/',views.profile,name='profile'),

    #MARKET PATTERN
    path('market/',views.market,name='market'),
    path('market/<slug:category_name_slug>/', views.market, name='show_category'),
    path('market/<slug:category_name_slug>/search', views.market, name='search_category'),

    path('market/<slug:category_name_slug>/<slug:chosen_button>',views.sort,name='sort_category'),

    path('sendMail/',views.about,name="review"),
    
]