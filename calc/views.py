from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


# Here we are handling the request by rendering the home.html and dynamically putting content in it by {{}}
def home(request):
    # return HttpResponse('<h1>whats up</h!>')
    return render(request, 'home.html', {'name': 'prashu'})

def add(request):
    val1  = int(request.GET['num1'])
    val2  = int(request.GET['num2'])
    res = val1 + val2
    return render(request, 'result.html', {'result' : res})