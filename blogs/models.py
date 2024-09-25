from django.db import models
from autoslug import AutoSlugField
from django.utils.text import slugify
import textwrap  # For generating clean excerpts
# Create your models here.
from django.utils import timezone

class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from="name", unique=True,null=True,default=None)

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.name)
            self.slug = f"{base_slug}"
        super().save(*args,**kwargs)    
    def __str__(self) -> str:
        return self.name
class Blog(models.Model):

    STATUS = {
        ('0','DRAFT'),
        ('1','PUBLISH')
    }

    SECTION = {
        ('Recent','Recent'),
        ('Publish','Publish'),
        ('Trending','Trending')
    }
    id = models.AutoField(primary_key=True) 
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=100)
    image = models.ImageField(upload_to="images")
    content = models.TextField()
    category = models.ForeignKey(Category, related_name='category', on_delete=models.CASCADE)
    blog_slug = AutoSlugField(populate_from='title', unique=True, null=True, default=None)
    date = models.DateField(auto_now_add=True)
    status = models.CharField(choices=STATUS, max_length=1,default=0)
    section = models.CharField(choices=SECTION, max_length=100, default="Recent")
    main_post = models.BooleanField(default=False)

    def excerpt(self, char_limit=100):
        # Shorten the content to the specified character limit, adding '...' if needed
        return textwrap.shorten(self.content, width=char_limit, placeholder="...")

    def __str__(self):
        return f"{self.title} ({self.category.name}) ({self.id})"
    

class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    post = models.ForeignKey(Blog, related_name='comments', on_delete=models.CASCADE)
    blog_id = models.IntegerField(blank=True, null=True)  # Add this field to store the Blog ID
    name = models.CharField(max_length=100)
    email = models.EmailField()
    website = models.URLField(blank=True, null=True)
    comment = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='replies')

    def save(self, *args, **kwargs):
        # Automatically set the blog_id when saving a comment
        if self.post:
            self.blog_id = self.post.id
        super().save(*args, **kwargs)

    def __str__(self):
        return f'Comment ID {self.id} on Blog Post ID {self.blog_id} by {self.name}: {self.comment[:20]}'