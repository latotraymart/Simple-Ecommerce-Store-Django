from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from store. models import Customer
from .forms import RegisterUserForm


# Create your views here.

def login_user(request):
	if request.method == "POST":
	    username = request.POST['username']
	    password = request.POST['password']
	    user = authenticate(request, username=username, password=password)
	    if user is not None:
	    	 # Redirect to a success page.
	        login(request, user)
	        return redirect ('stores')
	    else:
	        # Return an 'invalid login' error message.
	        messages.success(request, ("There Was An Error Logging In, Try  Again..."))
	        return redirect ('login')
	else:

		return render(request, 'authenticate/login.html', {})

def logout_user(request):
	logout(request)
	messages.success(request, ("You Were Logged Out..."))
	return redirect('stores')



def register_user(request):

        if request.method == 'POST':
            form = RegisterUserForm(request.POST)
            if form.is_valid(): 
                #saving the registered user
                user = form.save()
                Customer.objects.create(
                    user = user,
                    name = user.username,
                    email = user.email
                )

                username= form.cleaned_data.get('username') 
                messages.success(request, f'Your Account has been created! You can now log in')
                return redirect('login')
        else:
            form = RegisterUserForm() #creates an empty form
        return render(request, 'authenticate/register_user.html', {'form': form})

   	