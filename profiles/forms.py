from django.contrib.auth.forms import UserCreationForm
from .models import MyUserModel,Comement
from django import forms


class SignupForm(UserCreationForm):
    class Meta:
        model = MyUserModel
        fields = ('username', 'password1','password2')

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comement
        fields = ['title','text'] 

class FeedBackForm(forms.Form):
    number =forms.CharField(max_length=20)
    name = forms.CharField(max_length=20)
    text = forms.CharField(max_length=200)


