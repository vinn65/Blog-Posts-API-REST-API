from django.shortcuts import render, get_object_or_404, redirect
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
    comments = Comment.objects.filter(blog_id = post.id).order_by('-date')

    context = {
        "category":category,
        "post":post,
        'comments':comments
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

def add_comment(request,slug):
     
    if request.method == 'POST':
        post = get_object_or_404(Blog, blog_slug = slug)
        name = request.POST.get('InputName')
        email = request.POST.get('InputEmail')
        website = request.POST.get('InputWeb')
        comment_text = request.POST.get('InputComment')
        parent_id = request.POST.get('parent_id')
        parent_comment = None
        
        if parent_id:
            parent_comment = get_object_or_404(Comment, id=parent_id)

        Comment.objects.create(
            post= post,
            name=name,
            email=email,
            website=website,
            comment=comment_text,
            parent=parent_comment
        )
        return redirect("blog_detail",slug=post.blog_slug)
    return redirect('blog_detail')