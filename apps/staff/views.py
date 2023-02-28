from django.shortcuts import render
from django.shortcuts import render, redirect
from django.views.decorators.cache import cache_control
from django.contrib.auth.models import User

from apps.core.models import *

from apps.core.decorators import allowed_user

from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required(login_url='login')
@allowed_user(allowed=['admin'])
def staff(request):
    staffs = User.objects.all()
    context = {
        'navbar': 'staffs',
        'staffs': staffs,
    }

    return render(request, 'staff.html', context)
