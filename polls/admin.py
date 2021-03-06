from django.contrib import admin
from .models import Question, Choice

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
     date_hierarchy = 'pub_date'
     
     fieldsets = [
          (None,               {'fields': ['question_text']}),
          ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
     ]
     inlines = [ChoiceInline]
     
     list_display = ('question_text', 'pub_date', 'was_published_recently')

     Question.was_published_recently.admin_order_field = 'pub_date'
     Question.was_published_recently.boolean = True
     Question.was_published_recently.short_description = 'Published recently?'

     list_filter = ('pub_date',)
     search_fields = ('question_text',)
     ordering = ('-pub_date',)

# Register your models here.
admin.site.register(Question, QuestionAdmin)
