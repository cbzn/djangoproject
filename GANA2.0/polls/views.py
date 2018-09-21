from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.template import loader
from .models import Question

def index(request):
    lastest_questions_lst = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': lastest_questions_lst}
          # render(request object, template name, optional dictionary)
          # Returns an HttpResponse object of the given template rendered
          # with the given context.
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    # The get_object_or_404() function takes a Django model as its
    # first argument and an arbitrary number of keyword arguments,
    # which it passes to the get() function of the model’s manager
    # get_list_or_404() uses filter()
    question = get_object_or_404(Question,pk=question_id)

    return render(request, "polls/detail.html", {'question': question})

def results(request, question_id):
    return HttpResponse("You're looking at the results of question %s." % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)    