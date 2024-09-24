from django.shortcuts import render, get_object_or_404
from . models import *
from django.db.models import Count
# Create your views here.
def index(request):
    post = Blog.objects.order_by('-id')
    Main_post = Blog.objects.order_by('-id').filter(main_post=True)[0:1]
    latest = Blog.objects.all().order_by('-date')[0:5]
    recent = Blog.objects.all().order_by('-date')[0:5]
    popular = Blog.objects.filter(section="Trending").order_by('id')[0:3]
    cat = Category.objects.annotate(post_count=Count('category'))
    
    context = {
        'post' : post,
        'recent': recent,
        'popular' : popular,
        'main_post' : Main_post,
        'cat' : cat,
        'latest':latest,

    }
    return render(request, "ty.html", context)

def blog_detail(request, slug):
    category = Category.objects.all()
    post = get_object_or_404(Blog, blog_slug = slug)

    context = {
        "category":category,
        "post":post
    }

    return render(request, 'blog_detail.html', context)

def category(request, slug):
       blog_cat = Category.objects.all()
       cat = Category.objects.filter(slug=slug)
       context = {
       'cat' : cat,    
       'blog_cat' : blog_cat,              
       'active_category' :slug,
       }

        
       return render(request, 'category.html', context)