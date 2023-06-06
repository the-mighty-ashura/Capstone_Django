from django.shortcuts import render, redirect
import os
from django.conf import settings
from django.urls import reverse_lazy
from django.core.files.storage import default_storage
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import login, authenticate
from .forms import RegistrationForm, GalleryImageForm, GalleryImage
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.contrib.auth.forms import UserCreationForm

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

@login_required
def gallery(request):
    image_list = GalleryImage.objects.all()
    paginator = Paginator(image_list, 6) # Show 6 images per page
    page = request.GET.get('page')
    images = paginator.get_page(page)
    return render(request, 'gallery.html', {'images': images})

@login_required
def upload_image(request):
    if request.method == 'POST':
        form = GalleryImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.image = request.FILES['image']  # Assuming the image field name is 'image'
            image.save()
            # Move the uploaded image to the static/gallery directory
            file_path = os.path.join(settings.STATICFILES_STORAGE, 'gallery', image.image.name)
            default_storage.save(file_path, image.image)

            return redirect('gallery')
    else:
        form = GalleryImageForm()
    return render(request, 'upload_image.html', {'form': form})


class MyLoginView(LoginView):
    template_name = 'login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if next_url:
            return next_url
        else:
            return reverse_lazy('gallery')

class MyLogoutView(LogoutView):
    template_name = 'logout.html'

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration.html', {'form': form})


def user_authentication(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to the 'gallery' page after login
            return redirect('gallery')
        else:
            return render(request, 'login.html', {'error_message': 'Invalid credentials'})
    else:
        return render(request, 'login.html')
