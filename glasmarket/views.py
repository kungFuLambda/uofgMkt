from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.core.mail import EmailMessage
from .forms import ReviewForm

from glasmarket.models import Listing,Category,User


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
    context_dict['form'] = ReviewForm()

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        context_dict['form'] = form
        if form.is_valid():
            email = EmailMessage(form.cleaned_data['sender_email'],form.cleaned_data['message']+"\n"+form.cleaned_data['sender_name'],"sender",['glasmarketmail@gmail.com'])
            email.send()
        #email = EmailMessage("submit",form.message,"sender",['glasmarketmail@gmail.com'])
        #email.send()
    context_dict['form']=ReviewForm()


    return render(request,'glasmarket/about.html',context=context_dict)



def market(request):
    
    #here Category.objects.order_by('-likes')[:5] --> queries the category model to retrieve the top five categories
    product_list = Listing.objects.order_by('-name')
    category_list = Category.objects.order_by('-name')
    context_dict['active'] = 'market'
    context_dict['listings'] = product_list
    context_dict['categories'] = category_list
    return render(request,'glasmarket/market.html',context=context_dict)

def profile(request):
    
    #here Category.objects.order_by('-likes')[:5] --> queries the category model to retrieve the top five categories
    context_dict['active'] = 'profile'

    return render(request,'glasmarket/profile.html',context=context_dict)



def product(request):

    context_dict['active'] = 'market'
    
    return render(request,'glasmarket/product.html',context=context_dict)


def show_category(request,category_name_slug):
    context_dict['active'] = 'market'

    if category_name_slug == 'all':
        print("here")
        product_list = Listing.objects.order_by('-name')
        category_list = Category.objects.order_by('-name')
        context_dict['active'] = 'market'
        context_dict['listings'] = product_list
        context_dict['categories'] = category_list
        context_dict['category'] = 'all'
    else:
        try:
            category = Category.objects.filter(slug=category_name_slug)
            listings = Listing.objects.filter(category__in=category)

            context_dict['listings'] = listings
            context_dict['category'] = category

        except Category.DoesNotExist:
            context_dict['category'] = None
            context_dict['listings'] = None
    
    return render(request,'glasmarket/category.html',context=context_dict)