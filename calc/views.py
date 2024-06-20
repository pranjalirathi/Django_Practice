from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


# Here we are handling the request by rendering the home.html and dynamically putting content in it by {{}}
def home(request):
    # return HttpResponse('<h1>whats up</h!>')
    return render(request, 'home.html', {'name': 'prashu'})

def add(request):
    val1  = int(request.POST['num1'])
    val2  = int(request.POST['num2'])
    res = val1 + val2
    return render(request, 'result.html', {'result' : res})


#HTTP METHODS
#GET: whenever we want to fetch something from the server and we also have to pass some data on the server
#to not show the query parameters on the address bar, we have to use the post method'''
#POST: Whenever we want to send some data on the server