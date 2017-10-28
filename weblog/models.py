from datetime import datetime

from django.db import models
from django.contrib.auth.models import User

from markdown import markdown
from tagging.fields import TagField

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=250,
                             help_text="Maximum 250 characters.")
    slug = models.SlugField(unique=True,
                            help_text="Suggested value automatically generated from title. Must be unique.")
    description = models.TextField()

    class Meta:
        verbose_name_plural = "Categories"
        ordering = ['title']

    def __str__(self):          # __unicode__ in python 2
        return self.title

    def get_absolute_url():
        return reverse('weblog:category-detail', slug=self.slug)
###########################################################################

class Entry(models.Model):
    LIVE_STATUS = 1
    DRAFT_STATUS = 2
    HIDDEN_STATUS = 3
    STATUS_CHOICES = (
        (LIVE_STATUS, 'Live'),
        (DRAFT_STATUS, 'Draft'),
        (HIDDEN_STATUS, 'Hidden'),
    )

    # core fields
    title = models.CharField(max_length=250)
    pub_date = models.DateTimeField(default=datetime.now)
    excerpt = models.TextField(blank=True)
    body = models.TextField()

    # fields to store generated HTML
    excerpt_html = models.TextField(editable=False, blank=True)
    body_html = models.TextField(editable=False, blank=True)

    # metadata
    slug = models.SlugField(unique_for_date='pub_date')
    author = models.ForeignKey(User)
    ebable_comments = models.BooleanField(default=True)
    featured = models.BooleanField(default=False)   
    status = models.IntegerField(choices=STATUS_CHOICES, default=LIVE_STATUS)

    # categories
    categories = models.ManyToManyField(Category)
    tags = TagField()

    class Meta:
        verbose_name_plural = "Entries"
        ordering = ['-pub_date']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.body_html = markdown(self.body)
        self.excerpt_html = markdown(self.excerpt)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return "/weblog/%s/%s/" % (self.pub_date.strftime("%Y/%b/%d").lower(), self.slug)
