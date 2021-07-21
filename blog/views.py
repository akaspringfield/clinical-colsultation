from django.shortcuts import render, get_object_or_404
from .models import Blog



def blog(request):
    blogs = Blog.objects.order_by('-date')[:4]
    return render(request, 'blog/home.html', {'blogs':blogs})
