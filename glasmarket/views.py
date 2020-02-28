from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.




def home(request):
    #contruct dictionary to pass values to the {{boldmessage}} variable
    context_dict = {}
    #here Category.objects.order_by('-likes')[:5] --> queries the category model to retrieve the top five categories
    context_dict['active'] = 'home'
    context_dict['navBar'] = ['home','market','about','profile']




    return render(request,'glasmarket/home.html',context=context_dict)



def about(request):
    context_dict = {}
    #here Category.objects.order_by('-likes')[:5] --> queries the category model to retrieve the top five categories
    context_dict['active'] = 'about'
    context_dict['navBar'] = ['home','market','about','profile']

    return render(request,'glasmarket/about.html',context=context_dict)



def market(request):
    context_dict = {}
    #here Category.objects.order_by('-likes')[:5] --> queries the category model to retrieve the top five categories
    context_dict['active'] = 'market'
    context_dict['navBar'] = ['home','market','about','profile']




    return render(request,'glasmarket/market.html',context=context_dict)