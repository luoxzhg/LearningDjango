from django.db import models
from django.contrib import auth

import datetime

# Create your models here.
class Category(models.Model):
    "content category"
    label = models.CharField(max_length=50, blank=True)
    slug = models.SlugField()

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.label

# Create story model
STATUS_CHOICES = (
    (1, "Needs Edit"),
    (2, "Needs Approval"),
    (3, "Published"),
    (4, "Archived"),
)
VIEWABLE_STATUS = (3, 4)
# Create a StoryManager, only return published story
class PublishedStoryManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status__in=VIEWABLE_STATUS)

class Story(models.Model):
    "content for our site, generally corresponding to a page"
    
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    category=models.ForeignKey(Category)
    markdown_content = models.TextField()
    html_content = models.TextField(editable=False)
    
    owner = models.ForeignKey(auth.models.User)
    status = models.IntegerField(choices=STATUS_CHOICIES, default=1)
    created = models.DateTimeField(default=datetime.datetime.now)
    modified = models.DateTimeField(default=datetime.datetime.now)

    admin_objects = models.Manager()
    objects = ViewableManager()
   
    class Meta:
        ordering = ['modified']
        verbose_name_plural = 'stories'
        default_manager_name = 'admin_objects'

    @models.permalink
    def get_absolute_url(self):
        return ('cms-story', (), {'slug': self.slug})
