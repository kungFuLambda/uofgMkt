from django import forms
from glasmarket.models import User

class ReviewForm(forms.Form):
    sender_name = forms.CharField(max_length=100,help_text="name",label="text")
    sender_email = forms.EmailField(help_text="email",label="email")
    message = forms.CharField(widget=forms.Textarea,help_text="what's up?",label="textarea")
    class Meta:
        fields = ('name','email','message')
        
class LoginForm(forms.ModelForm):
    username= forms.CharField(max_length=100,help_text="name",label="text")
    password= forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model=User
        fields=('username','password')
        
class ProfileForm(forms.ModelForm):
    username= forms.CharField(max_length=100,help_text="name",label="text")
    password= forms.CharField(widget=forms.PasswordInput())
    email= forms.Charfield(max_length=128,help_text="email",label="email" )
    phone= forms.IntegerField(max_length=30,help_text="phone",label="phone" )
    class Meta:
        model=User
        fields=('username','password','email','phone')

