from django.shortcuts import render 
from blogs.models import Category, Blog
from core.models import About

def home(request):
    featured_posts = Blog.objects.filter(is_featured=True).order_by('updated_at')
    # Fetch AboutUs
    try:
        about = About.objects.get()
    except: 
        None
    context = {
        'featured_posts': featured_posts,
        'about': about
    }
    return render(request, 'home.html', context)