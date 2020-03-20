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
    path('login/',views.user_login,name='login'),
    path('register/', views.register,name='register'),
    path('logout/',views.user_logout,name='logout'),
    path('profilePage/<slug:username>/',views.profilePage,name='profilePage'),
    path('profilePage/<slug:username>/addListing',views.addListing,name='addListing'),
    path('profilePage/<slug:username>/<slug:listingID>',views.removeListing,name='removeListing'),
    #MARKET PATTERN
    path('market/',views.market,name='market'),
    path('market/<slug:category_name_slug>/', views.market, name='show_category'),
    path('market/<slug:category_name_slug>/search', views.market, name='search_category'),

    path('market/<slug:category_name_slug>/<slug:chosen_button>',views.sort,name='sort_category'),

    path('sendMail/',views.about,name="review"),
    
    
]