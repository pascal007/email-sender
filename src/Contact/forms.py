from django.contrib.auth.forms import forms
from DataAccessLayer.constants import CONTACT_GROUP_CHOICES


class AddContactForm(forms.Form):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'First name'
    }))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Last name'
    }))
    email = forms.EmailField(
        max_length=200, widget=forms.TextInput(attrs={
            'placeholder': 'Enter User Email',
            'type': 'email'
        }))
    group = forms.ChoiceField(choices=CONTACT_GROUP_CHOICES)


class SendMailForm(forms.Form):
    email = forms.EmailField(
        max_length=200, widget=forms.TextInput(attrs={
            'type': 'email',
            'disabled': True,
            'id': 'email_box'
        }), required=False)
    subject = forms.CharField(
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter Mail Subject here'
        }), required=True
    )
    body = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'placeholder': 'Enter Body here'
            }
        ), required=False
    )


