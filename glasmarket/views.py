from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.core.mail import EmailMessage
from .forms import ReviewForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

from glasmarket.models import Listing,Category,User,UserProfile,Message
from glasmarket.forms import UserForm,UserProfileForm,addListingForm,loginForm
from glasmarket.forms import SearchForm

from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.urls import reverse

#general context dict for navbar
context_dict = {}
context_dict['navBar'] = ['home','about','market','login']

###################################################################################################################################################################################################
###################################################################################################################################################################################################
###################################################################################################################################################################################################
###################################################################################################################################################################################################
###################################################################################################################################################################################################
###################################################################################################################################################################################################
def home(request):
    #contruct dictionary to pass values to the {{boldmessage}} variable

    #here Category.objects.order_by('-likes')[:5] --> queries the category model to retrieve the top five categories
    context_dict['active'] = 'home'

    return render(request,'glasmarket/home.html',context=context_dict)

###################################################################################################################################################################################################
###################################################################################################################################################################################################
###################################################################################################################################################################################################
###################################################################################################################################################################################################
###################################################################################################################################################################################################
###################################################################################################################################################################################################

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
            context_dict['active'] = 'home'
            return render(request,'glasmarket/home.html',context=context_dict)
        #email = EmailMessage("submit",form.message,"sender",['glasmarketmail@gmail.com'])
        #email.send()


    return render(request,'glasmarket/about.html',context=context_dict)

###################################################################################################################################################################################################
###################################################################################################################################################################################################
###################################################################################################################################################################################################
###################################################################################################################################################################################################
###################################################################################################################################################################################################
###################################################################################################################################################################################################




def market(request,**kwargs):

    category_name_slug = kwargs.get('category_name_slug','all')

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
            listings2 = Listing.objects.filter(category__in=category,description__contains=keyWord)
            qs3 = listings | listings2

            context_dict['listings'] = qs3
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
    return render(request,'glasmarket/cat.html',context=context_dict)



def sort(request,category_name_slug,chosen_button):
    if category_name_slug == 'all':
        categories = Category.objects.order_by('name')
    else:
        categories = Category.objects.filter(slug=category_name_slug)



    if chosen_button == 'newest':
        listings = Listing.objects.filter(category__in=categories).order_by('-date')
    elif chosen_button == 'oldest':
        listings = Listing.objects.filter(category__in=categories).order_by('date')
    elif chosen_button == 'highLow':
        listings = Listing.objects.filter(category__in=categories).order_by('-price')
    elif chosen_button == 'lowHigh':
        listings = Listing.objects.filter(category__in=categories).order_by('price')

    context_dict['listings'] = listings

    return render(request,'glasmarket/cat.html',context_dict)



def addListing(request,username):

    context_dict['active'] = 'login'
    UserID = User.objects.get(username=username)
    sell = UserProfile.objects.get(user=UserID)
    if request.method == 'POST':

        form = addListingForm(request.POST)

        if form.is_valid():
            if type(form.cleaned_data['price']) != int:
                context_dict['form'] = form
            else:
                listing = form.save(commit=False)
                if 'picture' in request.FILES:
                    listing.picture = request.FILES['picture']
                listing.save()

            return redirect(reverse('glasmarket:profilePage',kwargs={'username':username}))
        else:
            return render(request,'glasmarket/addListingPage.html',context_dict)



    context_dict['form'] = addListingForm(initial={'seller':sell})
    return render(request,'glasmarket/addListingPage.html',context_dict)



def removeListing(request,username,listingID):
    listing = Listing.objects.filter(id=listingID)
    listing.delete()
    return profilePage(request,username)

###################################################################################################################################################################################################
###################################################################################################################################################################################################
###################################################################################################################################################################################################
###################################################################################################################################################################################################
###################################################################################################################################################################################################
###################################################################################################################################################################################################
def user_login(request):


    context_dict['active'] = 'login'

    if request.method == 'POST':

        form = loginForm(request.POST)
        if form.is_valid():

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username,password=password)
            if user == None:
                try:
                    userObject = User.objects.get(email=username)

                    if userObject != None:
                        username = userObject.username
                        user = authenticate(username=username,password=password)
                except:
                    print("no user")

            if user:
                if user.is_active:
                    login(request,user)
                    return(redirect(reverse('glasmarket:profilePage' ,kwargs={'username':username})))
                else:
                    context_dict['error'] = 'user not active'
            else:
                return(redirect(reverse('glasmarket:login'), context=context_dict))

        context_dict['form'] = form


    else:
        context_dict['form'] = loginForm()

    return render(request,'glasmarket/login.html',context=context_dict)



def profilePage(request,username):

    context_dict['active'] = 'login'

    if not request.user.is_superuser:

        UserObject = User.objects.get(username=username)
        Profile = UserProfile.objects.get(user=UserObject)

        context_dict['pageUser'] = UserObject
        context_dict['profile'] = Profile

        listings = Listing.objects.filter(seller=Profile)

        context_dict['listings'] = listings

    return render(request,'glasmarket/userListings.html',context=context_dict)



def register(request):

    context_dict['registered']=False
    context_dict['active'] = 'login'

    if request.method=='POST':
        user_form=UserForm(request.POST)
        profile_form=UserProfileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():

            email = user_form.cleaned_data['email']
            if email != "":
                try:
                    if User.objects.get(email=email) != None:
                        context_dict['user_form']=user_form
                        context_dict['profile_form']=profile_form
                        return render (request,'glasmarket/register.html',context=context_dict)

                except :
                    print("")

                user=user_form.save()
                user.set_password(user.password)
                user.save()
                username = user_form.cleaned_data['username']
                password = user_form.cleaned_data['password']
                profile=profile_form.save(commit=False)
                profile.user=user

                if 'picture' in request.FILES:
                    profile.picture=request.FILES['picture']

                profile.save()
                context_dict['registered']=True
                user = authenticate(username=username,password=password)
                if user:
                    login(request,user)
                return(redirect(reverse('glasmarket:profilePage' ,kwargs={'username':username})))

        else:
            context_dict['user_form'] = user_form
            context_dict['profile_form'] = profile_form
            return render (request,'glasmarket/register.html',context=context_dict)


    else:
        context_dict['user_form']=UserForm()
        context_dict['profile_form']=UserProfileForm()


    return render (request,'glasmarket/register.html',context=context_dict)


@login_required
def user_logout(request):
    logout(request)
    context_dict['active'] = 'home'
    return(redirect(reverse('glasmarket:index') ,context=context_dict))


@login_required
def user_edit(request,username):
    context_dict['active'] = 'login'

    if request.method == 'POST':

        UserObject = User.objects.get(username=username)
        Profile = UserProfile.objects.get(user=UserObject)



        facebookLink = request.POST.get('facebook')
        phoneNumber = request.POST.get('phoneNumber')

        if facebookLink:
            Profile.facebook = facebookLink

        if phoneNumber:
            Profile.phone  = phoneNumber

        if 'profilePic' in request.FILES:
                Profile.picture=request.FILES['profilePic']



        Profile.save()
        return(redirect(reverse('glasmarket:profilePage' ,kwargs={'username':username})))


    else:
        context_dict['profile_form']=UserProfileForm()
    return render(request,'glasmarket/editInfo.html',context=context_dict)

###################################################################################################################################################################################################
###################################################################################################################################################################################################
###################################################################################################################################################################################################
###################################################################################################################################################################################################
###################################################################################################################################################################################################
###################################################################################################################################################################################################
@login_required
def messageUser(request,receiver,sender):
    context_dict['receiver'] = receiver
    context_dict['sender'] = sender
    context_dict['active'] = 'login'


    UserReceiver = User.objects.get(username=receiver)
    UserSender = User.objects.get(username=sender)

    UserObjectRcv = UserProfile.objects.get(user=UserReceiver)
    UserObjectSnd = UserProfile.objects.get(user=UserSender)


    msg1 = Message.objects.filter(receiver=UserObjectRcv,sender=UserObjectSnd).order_by('-date')
    msg2 = Message.objects.filter(receiver=UserObjectSnd,sender=UserObjectRcv).order_by('-date')

    context_dict['messages'] = msg1 | msg2
    if request.method=='POST':
        message = request.POST.get('message')
        if len(message) != 0:
            newMsg = Message()
            newMsg.receiver = UserProfile.objects.get(user_id=UserReceiver.id)
            newMsg.sender=UserProfile.objects.get(user_id=UserSender.id)
            newMsg.message = message
            newMsg.save()
            email = EmailMessage('You got mail in your glasmarket account',UserSender.username + " said " + message,'glasmarketmail@gmail.com',UserReceiver.email)
            email.send()


    return render(request,'glasmarket/messaging.html',context=context_dict)


@login_required
def myMessages(request,username):


    context_dict['received'] = []
    PeopleMessages = list(Message.objects.filter(receiver=UserProfile.objects.get(user_id=User.objects.get(username=username).id)))
    PeopleMessages2 = list(Message.objects.filter(sender=UserProfile.objects.get(user_id=User.objects.get(username=username).id)))

    for e in PeopleMessages:
        if e.sender not in context_dict['received']:
            context_dict['received'].append(e.sender)
    for e in PeopleMessages2:
        if e.receiver not in context_dict['received']:
            context_dict['received'].append(e.receiver)

    return render(request,'glasmarket/myMessages.html',context_dict)