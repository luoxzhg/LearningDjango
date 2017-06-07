from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.db.models import Count

from .models import Choice, Question

# Create your views here.
##def index(request):
##    latest_question_list = Question.objects.order_by('-pub_date')[:5]
##    return render(request, 'polls/index.html', {
##            'latest_question_list': lastest_question_list,
##        })
##
##def detail(request, question_id):
##    question=get_object_or_404(Question, pk=question_id)
##    return render(request, 'polls/detail.html', {'question': question})
##
##def results(request, question_id):
##    question = get_object_or_404(Question, pk=question_id)
##    return render(request, 'polls/results.html', {'question': question})
def _get_queryset():
    "only return all questions that published with choices"
    return Question.objects.filter(
               pub_date__lte = timezone.now()
           ).annotate(Count('choice')).filter(
               choice__count__gt = 0
           )


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        "return the last five published questions."
        return _get_queryset().order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
##    model = Question
    template_name = 'polls/detail.html'
    
    def get_queryset(self):
        "excludes any question that aren't published yet"
        return _get_queryset()

class ResultsView(DetailView):
##    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form
        return render(request, 'polls/detail.html',
                      {
                          'question': question,
                          'error_message': "You didn't select a choice.",
                      })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted tiwce
        # if a user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question_id,)))
