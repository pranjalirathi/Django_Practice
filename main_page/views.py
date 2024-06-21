from django.shortcuts import render
from .models import Destination

# Create your views here.

def index(request):
    
    #creating the object 
    dest1 = Destination();
    dest2 = Destination();
    dest3 = Destination();

    #passing the values
    dest1.name = "Rawatbhata"
    dest1.desc = "The power plant city"
    dest1.img = 'destination_1.jpg'
    dest1.price = 700

    dest2.name = "Kota"
    dest2.desc = "The study city"
    dest2.img = 'destination_2.jpg'
    dest2.price = 800

    dest3.name = "Chittor"
    dest3.desc = "The fort city"
    dest3.img= 'destination_3.jpg'
    dest3.price = 900

    dests = [dest1, dest2, dest3]

    return render(request, "index.html", {'dests': dests})
