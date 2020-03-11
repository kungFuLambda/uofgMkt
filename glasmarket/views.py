from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.core.mail import EmailMessage
from .forms import ReviewForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

from glasmarket.models import Listing,Category,User,UserProfile
from glasmarket.forms import UserForm,UserProfileForm,addListingForm
from glasmarket.forms import SearchForm

from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.urls import reverse

# Create your views here.
context_dict = {}
context_dict['navBar'] = ['home','about','market','login']


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



def user_login(request):
    
    #here Category.objects.order_by('-likes')[:5] --> queries the category model to retrieve the top five categories
    context_dict['active'] = 'login'
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return(redirect(reverse('glasmarket:profilePage' ,kwargs={'username':username})))
            else:
                return HttpResponse("your glasmarket account is disabled")
        else:
            #print(f"Invalid login details: {username},{password}")
            return HttpResponse("invalid login details")
    

    return render(request,'glasmarket/login.html',context=context_dict)

def profilePage(request,username):

    context_dict['active'] = 'login'
    if not request.user.is_superuser:

        UserObject = User.objects.filter(username=username)[0]
        Profile = UserProfile.objects.filter(user=UserObject)[0]

        context_dict['profile'] = Profile
        context_dict['usernm'] = UserObject.username 
        context_dict['email'] = UserObject.email
        context_dict['pic'] = Profile.picture
        
        listings = Listing.objects.filter(seller=Profile)
        
        context_dict['userPage'] = username
        context_dict['listings'] = listings
    
    return render(request,'glasmarket/profilePage.html',context=context_dict)


def addListing(request,username):

    context_dict['active'] = 'login'
    context_dict['usernm'] = username

    if request.method == 'POST':
        form = addListingForm(request.POST)
        if form.is_valid():    
            new_listing = form.save(commit=False)
            new_listing.seller = request.user
            new_listing.save()

        return redirect(reverse('glasmarket:profilePage',kwargs={'username':username}))
    else:
        context_dict['form'] = addListingForm()
        context_dict['usernm'] = username
        return render(request,'glasmarket/addListing.html',context_dict)





def market(request,category_name_slug):

    context_dict['active'] = 'market'
    context_dict['currentCategory'] = category_name_slug
    context_dict['form'] = SearchForm()


    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            keyWord = form.cleaned_data['searchWord']
            if category_name_slug == 'all':
                category = Category.objects.order_by('-name')
            else:
                category = Category.objects.filter(slug=category_name_slug)
            listings = Listing.objects.filter(category__in=category,name__contains=keyWord)
            context_dict['listings'] = listings
    else:
    #check if no cateogry name slug was given
        if category_name_slug == 'all':
            listings = Listing.objects.order_by('-name')
            categories = Category.objects.order_by('-name')
            context_dict['active'] = 'market'
            context_dict['listings'] = listings
            context_dict['categories'] = categories
            context_dict['category'] = 'all'
        
        #if a specific category was selected
        else:
            try:
                category = Category.objects.filter(slug=category_name_slug)
                listings = Listing.objects.filter(category__in=category)

                context_dict['listings'] = listings
                context_dict['category'] = category

            except Category.DoesNotExist:
                context_dict['category'] = None
                context_dict['listings'] = None
    
    
    context_dict['form'] = SearchForm()
    return render(request,'glasmarket/category.html',context=context_dict)



def sort(request,category_name_slug,chosen_button):
    if category_name_slug == 'all':
        categories = Category.objects.order_by('name')
    else:
        categories = Category.objects.filter(slug=category_name_slug)

    context_dict['categories'] = categories
    if chosen_button == 'newest':
        listings = Listing.objects.filter(category__in=categories).order_by('-date')
    elif chosen_button == 'oldest':
        listings = Listing.objects.filter(category__in=categories).order_by('date')    
    elif chosen_button == 'highLow':
        listings = Listing.objects.filter(category__in=categories).order_by('-price')
    elif chosen_button == 'lowHigh':
        listings = Listing.objects.filter(category__in=categories).order_by('price')
    context_dict['listings'] = listings

def user_login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=authenticate(username=username,password=password)
        if user:
            if user.is_active:
                login(request,user)
                return redirect(reverse('glasmarket:profile'))
    return render(request,'glasmarket/category.html',context=context_dict)




def register(request):
    context_dict['registered']=False
    context_dict['active'] = 'login'
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
            context_dict['registered']=True

    
        else:
            print(user_form.errors, profile_form.errors)
        return render (request,'glasmarket/login.html',context_dict)
    else:
        context_dict['user_form']=UserForm()
        context_dict['profile_form']=UserProfileForm()
        

    return render (request,'glasmarket/register.html',context_dict)

@login_required
def user_logout(request):
    logout(request)
    context_dict['active'] = 'home'
    return render(request,'glasmarket/home.html',context=context_dict)