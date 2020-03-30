from django.urls import path,include
from glasmarket import views 
from django.contrib.auth.views import PasswordResetDoneView,PasswordResetView, PasswordResetConfirmView, PasswordResetCompleteView
from django.conf.urls import url
app_name = 'glasmarket'

urlpatterns = [
    #BASIC PATTERS
    path('/',views.market,name='market'),
    path('glasmarket',views.market,name="market"),
    path('home/',views.home,name="index"),
    path('about/',views.about,name='about'),

    #PROFILE PATTERN
    path('login/',views.user_login,name='login'),
    path('register/', views.register,name='register'),
    path('logout/',views.user_logout,name='logout'),
    path('profilePage/<slug:username>/',views.profilePage,name='profilePage'),
    path('profilePage/<slug:username>/addListing',views.addListing,name='addListing'),
    path('profilePage/<slug:username>/<slug:listingID>',views.removeListing,name='removeListing'),
    path('editUser/<slug:username>',views.user_edit,name='editUser'),



    #MARKET PATTERN
    path('market/',views.market,name='market'),
    path('market/<slug:category_name_slug>/', views.market, name='show_category'),
    path('market/<slug:category_name_slug>/search', views.market, name='search_category'),

    path('market/<slug:category_name_slug>/<slug:chosen_button>',views.sort,name='sort_category'),

    path('sendMail/',views.about,name="review"),

    #change password
    url(r'^reset-password/$', PasswordResetView.as_view(template_name='glasmarket/password_reset_form.html'), name='password_reset'),
    url(r'^password_reset/done/$', PasswordResetCompleteView.as_view(template_name='glasmarket/password_reset_done.html'), name='password_reset_done'),
    url(r'^/reset-password/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$', PasswordResetConfirmView.as_view(template_name='glasmarket/password_reset_complete.html'), name='password_reset_confirm'),
    url(r'^reset-password/complete/$', PasswordResetCompleteView.as_view(template_name='glasmarket/password_reset_complete.html'), name='password_reset_complete')
    

    
    
    

    
]