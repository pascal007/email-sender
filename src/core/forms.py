from django.contrib.auth.forms import UserCreationForm
from DataAccessLayer.User.model import User
from django.contrib.auth.forms import forms


class SignUpForm(UserCreationForm):

    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'First name'
    }))
    email = forms.EmailField(
        max_length=200, widget=forms.TextInput(attrs={
            'placeholder': 'Your Email',
            'type': 'email'
        }))

    class Meta:
        model = User
        fields = ('first_name', 'email', 'password1', 'password2')


class SignInForm:
    pass







