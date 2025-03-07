from django.shortcuts import render
from django.http import HttpResponseNotFound,HttpResponse, HttpResponseRedirect

# Create your views here.

def pageIndex(request):
    response_data = "<h1>Welcome to myPage!</h1> <p>Click <a href=\"/challenges\">here</a> to view the challenges.</p>"
    return HttpResponse(response_data)
