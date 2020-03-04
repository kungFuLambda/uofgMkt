from django import forms

class ReviewForm(forms.Form):
    sender_name = forms.CharField(max_length=100,help_text="name",label="text")
    sender_email = forms.EmailField(help_text="email",label="email")
    message = forms.CharField(widget=forms.Textarea,help_text="what's up?",label="textarea")
    class Meta:
        fields = ('name','email','message')