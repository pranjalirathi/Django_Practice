from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.





def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            messages.info(request, 'invalid credentials')
            return redirect('login')
    else:
        return render(request, 'login.html')




#We will be using the samefunction for both the ways that sis for fetching the html page and for sending the data as well thats why we are returning the page below and we have specified taht if the method is post which means if we are getting the data fromthe html page then what to do and if not then what to do;
#Thats why the get and post will be having in logic acc to it
#jab ham sirf register.html ko call karte hai then we are sending a get request
#jab ham us page se data submit karte hai then we are submitting it as post request
#so the url is same, just the request method is being changed
#we already have teh mdoel object in the django framework thats why we do not have to create one and we will directly push into the database so import user and auth

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name  = request.POST['last_name']
        username   = request.POST['username']
        password1  = request.POST['password1']
        password2  = request.POST['password2']
        email      = request.POST['email'] 

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, "username taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "email taken")
                return redirect('register')
            else:
                user = User.objects.create_user(username = username,password = password1, email=email, last_name = last_name, first_name = first_name)
                user.save();
                print('user craeted successfully')
                return redirect('login')
        else:
            messages.info(request, 'password not matching')
            return redirect('register')
        return redirect('/');

    else:
        return render(request, 'register.html')
