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





class SearchForm(forms.Form):
    searchWord = forms.CharField(max_length=100,help_text="What are you looking for?",label="text")
    
    class Meta:
        fields=('search')

    