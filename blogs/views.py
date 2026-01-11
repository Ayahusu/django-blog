from django.shortcuts import get_object_or_404, redirect, render
from .models import Blog, Category
# Create your views here.

def posts_by_category(request,pk):
    # fetch the post that belogs to category with the id (pk)
    posts = Blog.objects.filter(status="Published", category=pk)
    # try:
    #     category = Category.objects.get(pk=pk)
    # except:
    #     return redirect('home')

    category = get_object_or_404(Category, pk=pk)
    context = {
        'posts': posts,
        'category': category
    }
    return render(request, 'post_by_category.html', context)