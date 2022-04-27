from datetime import datetime

from django.shortcuts import render
from django.http import HttpResponse

from meetings.models import Meeting

# Create your views here.
def welcome(request):
    # return HttpResponse("Welcome to the Meeting Planner!")
    # return render(request, "website/welcome.html")
    return render(request, "website/welcome.html",
                  {"num_meetings": Meeting.objects.count()})

def date(request):
    return HttpResponse("This page was server at " + str(datetime.now()))

def about(request):
    return HttpResponse("Project created by @aayerdesp")