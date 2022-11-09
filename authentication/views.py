from django.shortcuts import render, redirect
from django.views.decorators.cache import cache_control

from core.decorators import unautheticated_user
from core.forms import CreateUserForm

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
            print('User is created successfully')
            return redirect('dashboard')

    context = {
        'form':form,
    }

    return render(request, 'authentication/register.html', context)

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

    return render(request, 'authentication/login.html')

# LOGOUT USER
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def logoutUser(request):
    logout(request)
    return redirect('login')