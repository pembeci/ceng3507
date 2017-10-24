from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import Question


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
    
def hello_page(request):
    return HttpResponse("Another hello world.")  
    
def second(request):
    return HttpResponse("Second page.")  
    
def detail(request, q_id):
    question = get_object_or_404(Question, pk=q_id)
    html_result = "<h2>{}</h2>".format(question.question_text)
    return HttpResponse(html_result)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)    
