from django import forms
from django.contrib.auth.forms import UserCreationForm
from taggit.forms import TagField, TagWidget


from .models import *
from .serializers import ImageSerializer


class CustomUserForm(UserCreationForm):
    email = forms.EmailField(label="Email", required=True,
                             help_text=("Please enter email"))

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
            return user


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']


class InvalidDataException(forms.ValidationError):
    pass


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['image', "email"]


class CreateAdForm(forms.ModelForm):
    tags = TagField()

    class Meta:
        model = Ad
        fields = ['title', 'description', 'tags']

        widgets = {
            'tags': TagWidget(),
        }

 

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('image',)
