from django.shortcuts import render
from django.views import generic

from .models import Category, Entry

# Create your views here.
class CategoryDetail(generic.DetailView):
    model = Category
    template_name = 'weblog/detail.html'
    

class EntryIndex(generic.IndexView):
    model = Entry
    template_name = 'weblog/entry_index.html'
