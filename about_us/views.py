from django.shortcuts import render
from .models import About

def about_us(request):
    about = About.objects.all()
    return render(request, 'about/about.html', {'about':about,})

# Create your views here.
