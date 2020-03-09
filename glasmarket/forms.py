from django import forms
from glasmarket.models import UserProfile
from django.contrib.auth.models import User

class ReviewForm(forms.Form):
    sender_name = forms.CharField(max_length=100,help_text="name",label="text")
    sender_email = forms.EmailField(help_text="email",label="email")
    message = forms.CharField(widget=forms.Textarea,help_text="what's up?",label="textarea")
    class Meta:
        fields = ('name','email','message')
        
class UserForm(forms.ModelForm):
    password= forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model=User
        fields=('username','password','email','first_name')
   
        
class UserProfileForm(forms.ModelForm):
    
    class Meta:
        model=UserProfile
        fields=('picture',)


class SearchForm(forms.Form):
    searchWord = forms.CharField(max_length=100,help_text="What are you looking for?",label="text")
    
    class Meta:
        fields=('search')

    