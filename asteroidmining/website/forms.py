from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, GalleryImage

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class GalleryImageForm(forms.ModelForm):
    class Meta:
        model = GalleryImage
        fields = ('title', 'image')
