from django import forms
from glasmarket.models import UserProfile,Listing,Category
from django.contrib.auth.models import User


class ReviewForm(forms.Form):
    sender_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'your name'}),max_length=100,help_text="name",label="text")
    sender_email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder':'email'}),help_text="email",label="email")
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder':'message'}),help_text="what's up?",label="textarea")
    class Meta:
        fields = ('name','email','message')

        
class UserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=('username','password','email')
        widgets={
            'username':forms.TextInput(attrs={'placeholder':'username'}),
            'email':forms.TextInput(attrs={'placeholder':'email'}),
            'password':forms.PasswordInput(attrs={'placeholder':'password'}),
        }
        
class UserProfileForm(forms.ModelForm):
    class Meta:
        model=UserProfile
        fields=('phone','facebook','picture')
        widgets = {
            'facebook':forms.TextInput(attrs={'placeholder':'facebook link'}),
            'phone':forms.TextInput(attrs={'placeholder':'phone number'}),
        }

class addListingForm(forms.ModelForm):
    class Meta:
        model=Listing
        fields = ('name','price','picture','description','category','seller',)
        widgets={
            'name':forms.TextInput(attrs={'placeholder':'product name'}),
            'description':forms.Textarea(attrs={'placeholder':'product description'}),
            'seller':forms.HiddenInput(),
            'price':forms.TextInput(),
            'category':forms.Select(attrs={'placeholder':'choose a category'}),

        }




class SearchForm(forms.Form):
    searchWord = forms.CharField(max_length=100,help_text="What are you looking for?",label="text")
    
    class Meta:
        fields=('search')

    
class loginForm(forms.Form):
    class Meta:
        model=User
        fields=('username','password')
        widgets={
            'username':forms.TextInput(attrs={'placeholder':'username'}),
            'password':forms.PasswordInput(attrs={'placeholder':'password'}),
        }