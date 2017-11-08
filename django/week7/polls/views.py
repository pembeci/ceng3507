from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, Http404
from .models import Question
from django.template import loader

"""
def index(request):
    all_questions = Question.objects.order_by("-pub_date")[:3]
    result = ""
    result += "<ul>"
    for q in all_questions:
        result += "<li><a href='{}'>{}</a></li>"\
                      .format(q.id,q.question_text)
    result += "</ul>"
    print(result)
    return HttpResponse(result)


def index(request):
    all_questions = Question.objects.order_by("-pub_date")[:3]
    template = loader.get_template("polls/index.html")
    context = { "questions" : all_questions }
    return HttpResponse(template.render(context,request))
"""

def index(request):
    all_questions = Question.objects \
                     .filter(active=True) \
                     .order_by("-pub_date")[:7]
    context = { "questions" : all_questions }
    return render(request, "polls/index.html", context)

def hello_page(request):
    return HttpResponse("Another hello worldddddd.")

def hello_page2(request, username):

    return HttpResponse("Hmmmm. Hello <b>"+username+"</b>")

def second(request):
    return HttpResponse("Second page.")  
    
def detail(request, q_id):
    """
    question = get_object_or_404(Question, pk=q_id)
    html_result = "<h2>{}</h2>".format(question.question_text)
    return HttpResponse(html_result)
    try:
        question = Question.objects.get(pk=q_id)
    except Question.DoesNotExist:
        raise Http404("Questin not found.")
    """
    question = get_object_or_404(Question, pk=q_id)
    print(question.choice_set.all())
    return render(request, "polls/detail.html",
                  {'question': question})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)    
