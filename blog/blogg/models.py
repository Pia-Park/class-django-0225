from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User 

# Create your models here.

class Post(models.Model):

    options = (
        ('draft', 'Draft'),
        ('published', 'Published')
    )

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    publish = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE,related_name='blog_posts')
    content = models.TextField()
    status = models.CharField(max_length=10, default='draft', choices=options)

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title
