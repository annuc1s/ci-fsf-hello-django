from django.shortcuts import render, HttpResponse

# Create your views here.
#takes a http request from the user and return a http response to the user that says hello
def say_hello(request):
    return HttpResponse("Hello!")