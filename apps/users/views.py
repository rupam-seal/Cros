from django.shortcuts import render
from django.shortcuts import render, redirect

from .forms import CustomerForm, StaffForm

from apps.core.models import *

from apps.core.decorators import allowed_user

from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required(login_url='login')
@allowed_user(allowed=['admin', 'staff'])
def users(request):
    user = request.user.username

    """
        USER VIEW CONTAINER
    """
    if user == 'admin':
        users = Staff.objects.all()
    else:
        # get current staff using current username
        staff = Staff.objects.get(name=user)
        # filter all customer that current staff sold
        seller = Order.objects.filter(seller=staff)
        # empty list to append all filterd customer name
        customerList = []
        for i in seller:
            # appending the customer name
            customerList.append(i.customer.name)

        # removing duplicate staff name
        customers = [*set(customerList)]

        # empty list to add customer object
        users = []

        # iterate through customers str names
        for i in customers:
            # appending customer object using customer str name
            users.append(Customer.objects.get(name=i))

    """
    FORM CONTAINER
    """
    if user == 'admin':
        userForm = StaffForm()

        if request.method == "POST":
            userForm = StaffForm(request.POST)
            if userForm.is_valid:
                userForm.save()
                return redirect('users')
    else:
        userForm = CustomerForm()

        if request.method == "POST":
            userForm = CustomerForm(request.POST)
            if userForm.is_valid:
                userForm.save()
                return redirect('users')

    context = {
        'navbar': 'users',
        'users': users,
        'userForm': userForm,
    }

    return render(request, 'users.html', context)
