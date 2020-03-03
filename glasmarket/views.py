from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
context_dict = {}
context_dict['navBar'] = ['home','about','market','profile']


def home(request):
    #contruct dictionary to pass values to the {{boldmessage}} variable
    
    #here Category.objects.order_by('-likes')[:5] --> queries the category model to retrieve the top five categories
    context_dict['active'] = 'home'

    return render(request,'glasmarket/home.html',context=context_dict)



def about(request):
    
    #here Category.objects.order_by('-likes')[:5] --> queries the category model to retrieve the top five categories
    context_dict['active'] = 'about'
    
    return render(request,'glasmarket/about.html',context=context_dict)



def market(request):
    
    #here Category.objects.order_by('-likes')[:5] --> queries the category model to retrieve the top five categories
    context_dict['active'] = 'market'
    
    return render(request,'glasmarket/market.html',context=context_dict)

def profile(request):
    
    #here Category.objects.order_by('-likes')[:5] --> queries the category model to retrieve the top five categories
    context_dict['active'] = 'profile'

    return render(request,'glasmarket/profile.html',context=context_dict)



def reviewMail(request):
    context_dict['active'] = 'profile'