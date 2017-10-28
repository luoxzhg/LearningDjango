from django.shortcuts import render, redirect
from django.contrib.flatpages.models import FlatPage

# Create your views here.
def search(request):
    query = request.GET.get('q')
    results = []
    keyword_results = []
    if query:
        keyword_results = FlatPage.objects.filter(
            searchkeyword__keyword__in=query.split()).distinct()
        if keyword_results.count() == 1:
            return redirect(keyword_results[0])
        
        results = FlatPage.objects.filter(content__icontains=query)
    return render(request, 'search/search.html',
                  {'query': query,
                   'results':results,
                   'keyword_results': keyword_results})

