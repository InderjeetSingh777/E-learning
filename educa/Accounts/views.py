from django.shortcuts import render

from django.shortcuts import render
from django.contrib.auth import(authenticate,get_user_model,login,logout)

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm

def user_login(request):

    if request.method == 'POST':
        # First get the username and password supplied
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Django's built-in authentication function:
        user = authenticate(username=username, password=password)
        form=AuthenticationForm(data=request.POST)
        # If we have a user
        if user:
            #Check it the account is active
            if user.is_active:
                # Log the user in.
                login(request,user)
                # Send the user back to some page.
                # In this case their homepage.
                print(request.user.role)
                if request.user.role=='Student':
                	return render(request, 'students/course/list.html', {})
                else:
                	return render(request, 'courses/manage/course/list.html', {})
            else:
                # If account is not active:
                print('yo')
                return render(request, 'registration/login.html', {'form':form})
        else:
            return render(request, 'registration/login.html', {'form':form})
    else:
        #Nothing has been provided for username or password.
        form =AuthenticationForm()
        return render(request, 'registration/login.html', {'form':form})