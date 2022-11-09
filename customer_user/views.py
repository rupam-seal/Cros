from datetime import date

from django.shortcuts import render

from core.models import *

from core.decorators import allowed_user
from django.contrib.auth.decorators import login_required

'''
    -------- CUSTOMER ----------
'''

@login_required(login_url='login')
@allowed_user(allowed=['customer'])
def customerDashboard(request):
    user_id = request.user.username

    user = Customer.objects.get(name=user_id)

    orders = user.order_set.all()
    total_orders = orders.count()
    orders_pending = orders.filter(status='Pending')
    orders_pending_count = orders_pending.count()
    orders_paid = orders.filter(status='Paid')
    orders_paid_count = orders_paid.count()

    total_cash = 0
    for cash in orders_paid:
        total_cash += cash.price*cash.quantity

    context = {
        'navbar':'dashboard',
        'orders':orders,
        'total_orders':total_orders,
        'orders_pending_count':orders_pending_count,
        'orders_paid_count':orders_paid_count,
        'total_cash':total_cash,
    }

    return render(request, 'customer/customerDashboard.html', context)

@login_required(login_url='login')
@allowed_user(allowed=['customer'])
def customerOrders(request):
    user_id = request.user.username

    user = Customer.objects.get(name=user_id)

    orders = user.order_set.all()
    orders_pending_count = orders.filter(status='Pending').count()
    orders_paid_count = orders.filter(status='Paid').count()
    
    context = {
        'navbar':'customerOrders',
        'orders':orders,
        'orders_pending_count':orders_pending_count,
        'orders_paid_count':orders_paid_count,
    }

    return render(request, 'orders/orders.html', context)

@login_required(login_url='login')
@allowed_user(allowed=['customer'])
def customerOrdersPaid(request):
    user_id = request.user.username

    user = Customer.objects.get(name=user_id)

    orders = user.order_set.filter(status='Paid')
    order_count = orders.count()

    context = {
        'orders':orders,
        'navbar':'customerOrders',
        'order_count':order_count,
    }

    return render(request, 'orders/ordersPaid.html', context)

@login_required(login_url='login')
@allowed_user(allowed=['customer'])
def customerOrdersPending(request):
    user_id = request.user.username

    user = Customer.objects.get(name=user_id)

    orders = user.order_set.filter(status='Pending')
    order_count = orders.count()

    context = {
        'orders':orders,
        'navbar':'customerOrders',
        'order_count':order_count,
    }

    return render(request, 'orders/ordersPending.html', context)