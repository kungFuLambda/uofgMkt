from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.core.mail import EmailMessage
from .forms import ReviewForm
from django.contrib.auth.forms import UserCreationForm

from glasmarket.models import Listing,Category,User
from glasmarket.forms import UserForm,UserProfileForm


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


def logIn(request):
    
    #here Category.objects.order_by('-likes')[:5] --> queries the category model to retrieve the top five categories
    context_dict['active'] = 'logIn'

    return render(request,'glasmarket/logIn.html',context=context_dict)

def register(request):
    registered=False

    if request.method=='POST':
        user_form=UserForm(request.POST)
        profile_form=UserProfileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user=user_form.save()
            user.set_password(user.password)
            user.save()
            
            profile=profile_form.save(commit=False)
            profile.user=user

            if 'picture' in request.FILES:
                profile.picture=request.FILES['picture']
            
            profile.save()
            registered=True

    
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form=UserForm()
        profile_form=UserProfileForm()

    return render (request,'glasmarket/register.html',context={'user_form':user_form,
                                                                'profile_form':profile_form,
                                                                'registered':registered})