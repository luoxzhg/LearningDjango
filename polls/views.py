from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Choice, Question
from .forms import PersonForm, SimplePerson

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

##replaced by Question.published()
##def _get_queryset():
##    "only return all questions that published with choices"
##    return Question.objects.filter(
##               pub_date__lte = timezone.now()
##           ).annotate(Count('choice')).filter(
##               choice__count__gt = 0
##           )


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        "return the last five published questions."
        return Question.published().order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
##    model = Question
    template_name = 'polls/detail.html'
    
    def get_queryset(self):
        "excludes any question that aren't published yet"
        return Question.published()

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
        selected_choice.votes += 1      # F() expression
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted tiwce
        # if a user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question_id,)))

##def _get_form(request, formclass):
##    if request.method == 'POST':
##        return formclass(request.POST)
##    else:
##        return formclass()
    
##def person(request):
##    if request.method == 'POST':
##        p = SimplePerson(request.POST)
##        if p.is_valid():
##            return HttpResponseRedirect(reverse('index'))
##    else:
##        p = SimplePerson()
##    return render(request, 'polls/person.html', {'form': p})
def personform(request):
    p = SimplePerson(request.POST if request.method == 'POST' else None)
    if p.is_valid():
        return redirect(reverse('polls:index'))
    
    return render(request, 'polls/person.html', {'form': p})
