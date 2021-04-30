from django.http import HttpResponse
 
def hello(request):
    return HttpResponse("Hello world ! ")
	
	
from django.shortcuts import render
 
def index(request):
    return render(request, 'index.html')
	
	
def signin(request):
    return render(request, 'signin.html')
	
def book(request):
    return render(request, 'book.html')
	
def event(request):
    return render(request, 'event.html')
	
def room(request):
    return render(request, 'room.html')
	
