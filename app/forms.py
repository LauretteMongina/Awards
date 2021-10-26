from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *
INTEGER_CHOICES= [tuple([x,x]) for x in range(1,11)]

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=254)

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None


class UpdateUserForm(forms.ModelForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email')


class UpdateUserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['user', 'email', 'photo', 'bio']


class PostForm(forms.ModelForm):
    class Meta:
        model = Post

        fields = ('image', 'title', 'url', 'description', 'technology',)


class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['design', 'usability', 'content']
        widgets = {
            'design': forms.Select(choices=INTEGER_CHOICES),
            'usability': forms.Select(choices=INTEGER_CHOICES),
            'content': forms.Select(choices=INTEGER_CHOICES),
            'review': forms.TextInput(attrs={'placeholder':'Add a review'})
        }