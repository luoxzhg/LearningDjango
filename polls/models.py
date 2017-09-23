import datetime
from django.utils import timezone
from django.db import models
from django.db.models import Count

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date publised')

    def __str__(self):
        return self.question_text
    
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    def published():
        "only return all questions that published with choices"
        return Question.objects.filter(
                   pub_date__lte = timezone.now()
               ).annotate(Count('choice')).filter(
                   choice__count__gt = 0
               )

class Choice(models.Model):
    question    = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes       = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


class Person(models.Model):
    first  = models.CharField(max_length=100)
    middle = models.CharField(max_length=100, blank=True)
    last   = models.CharField(max_length=100)

    def __str__(self):
        return '%s %s %s' % (self.first, self.middle, self.last)

