from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, GalleryImage

class RegistrationForm(UserCreationForm):
    """
    User registration form.

    Extends Django's UserCreationForm and adds an email field.
    """
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class GalleryImageForm(forms.ModelForm):
    """
    Form for uploading gallery images.

    Uses the GalleryImage model and includes fields for title and image.
    """
    class Meta:
        model = GalleryImage
        fields = ('title', 'image')
