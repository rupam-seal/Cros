from django.shortcuts import render
from django.shortcuts import render, redirect
from django.views.decorators.cache import cache_control
from django.contrib.auth.models import User

from apps.core.models import *

from apps.core.decorators import allowed_user

from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required(login_url='login')
@allowed_user(allowed=['admin', 'staff'])
def staff(request):
    user = request.user.username

    if user == 'admin':
        staffs = User.objects.all()
    else:
        staff = Staff.objects.get(name=user)
        seller = Order.objects.filter(seller=staff)
        customerList = []
        for i in seller:
            customerList.append(i.customer.name)

        customers = [*set(customerList)]

        staffs = []

        for i in customers:
            staffs.append(Customer.objects.get(name=i))

        print(staffs)

    context = {
        'navbar': 'staffs',
        'staffs': staffs,
    }

    return render(request, 'staff.html', context)
