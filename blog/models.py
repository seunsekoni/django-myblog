from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from taggit.managers import TaggableManager
from django.conf import settings

# Create your models here.

class PublishedManager(models.Manager):
    '''
        custom manager to fetch all published posts
    '''
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='published')

class Category(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('created_at',)
        verbose_name_plural = 'Categories'

    def __str__(self) -> str:
        return f'{self.name}'

class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,
                                choices=STATUS_CHOICES,
                                default='draft')
    # explictly add objects default manager to aslo be able to use it while 
    # trying to use the custom manager
    objects = models.Manager()
    published = PublishedManager()
    tags = TaggableManager()
    category = models.ForeignKey(Category, related_name='categories', on_delete=models.DO_NOTHING)
    image = models.ImageField(upload_to='posts/%Y/%m/%d', blank=True)

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title

    def get_image_url(self):
        return f'{settings.MEDIA_URL}/{self.image}'

    def get_absolute_url(self):
        '''
            define the canonical(default) url for post resource
        '''
        return reverse('blog:post_detail',
                        args=[
                            self.publish.year,
                            self.publish.month,
                            self.publish.day,
                            self.slug
                        ]
                    )

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=45)
    email = models.EmailField()
    body = models.TextField()
    # create a field called parent id in case the comment is a reply to a comment
    comment_parent_id = models.ForeignKey('self', on_delete=models.CASCADE, related_name='replies')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created_at',)

    def __str__(self):
        return f'Comment by {self.name} on {self.post}'
