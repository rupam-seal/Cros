from django.shortcuts import render, redirect
from django.views.decorators.cache import cache_control

from apps.core.decorators import unautheticated_user
from .forms import CreateUserForm

from django.contrib import messages

from django.contrib.auth import authenticate, login, logout

'''
    ---------- USER AUTHENTICATION ----------
'''

# REGISTER PAGE


@unautheticated_user
def registerPage(request):
    # Create user form
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            print(username, "===============================")
            messages.success(request, 'Account created for '+username)
            return redirect('login')

    context = {
        'form': form,
    }

    return render(request, 'register.html', context)


# LOGIN PAGE


@unautheticated_user
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def loginPage(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')

    return render(request, 'login.html')


# LOGOUT USER


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def logoutUser(request):
    logout(request)
    return redirect('login')


@unautheticated_user
def navigation(request):
    return render(request, 'navigation.html')
