from django.shortcuts import render
from apps.core.decorators import allowed_user

from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required(login_url='login')
@allowed_user(allowed=['staff'])
def staffDashboard(request):
    return render(request, 'staffDashboard.html')
