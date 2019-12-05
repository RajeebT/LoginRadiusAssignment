from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import get_object_or_404,render,redirect
from django.urls import reverse
from .models import Candidates
from django.http import Http404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import  login_required


def indexView(request):
     return render(request,'polls/index.html')
@login_required()

def dashboardView(request):
    latest_question_list =Candidates.objects.order_by('Name')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

def registerView(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_url')
    else:
        form= UserCreationForm()

    return render(request,'polls/register.html',{'form':form})

def results(request, question_id):
    VoteAcquired = get_object_or_404(Candidates, pk=question_id)
    response = "You voted for %s."
    return HttpResponse(response % VoteAcquired)

def detail(request, question_id):
    question = get_object_or_404(Candidates, pk=question_id)
    try:
        selected_choice = question
    except (KeyError, Candidates.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/index.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(selected_choice.id,)))











