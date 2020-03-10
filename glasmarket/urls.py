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
<<<<<<< HEAD
=======
    path('logIn/',views.user_login,name='logIn'),
>>>>>>> 98ba893ad61b62aea10b565c3191e18abd5437f4
    path('register/', views.register,name='register'),
    path('logout/',views.user_logout,name='logout'),

    #MARKET PATTERN
    path('market/',views.market,name='market'),
    path('market/<slug:category_name_slug>/', views.market, name='show_category'),
    path('market/<slug:category_name_slug>/search', views.market, name='search_category'),

    path('market/<slug:category_name_slug>/<slug:chosen_button>',views.sort,name='sort_category'),

    path('sendMail/',views.about,name="review"),
    
    
]