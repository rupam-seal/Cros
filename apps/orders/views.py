from django.shortcuts import render, redirect
from apps.core.models import *

from apps.core.decorators import allowed_user

from django.contrib.auth.decorators import login_required


# Create your views here.
# --------- ORDERS --------- #


@login_required(login_url='login')
@allowed_user(allowed=['admin'])
def orders(request):
    orders = Order.objects.all()
    orders_pending_count = Order.objects.filter(status='Pending').count()
    orders_paid_count = Order.objects.filter(status='Paid').count()

    context = {
        'navbar': 'orders',
        'orders': orders,
        'orders_pending_count': orders_pending_count,
        'orders_paid_count': orders_paid_count,
    }

    return render(request, 'orders.html', context)


@login_required(login_url='login')
@allowed_user(allowed=['admin'])
def ordersPaid(request):
    orders = Order.objects.filter(status='Paid')
    order_count = orders.count()

    context = {
        'orders': orders,
        'navbar': 'orders',
        'order_count': order_count,
    }

    return render(request, 'ordersPaid.html', context)


@login_required(login_url='login')
@allowed_user(allowed=['admin'])
def ordersPending(request):
    orders = Order.objects.filter(status='Pending')
    order_count = orders.count()

    context = {
        'orders': orders,
        'navbar': 'orders',
        'order_count': order_count,
    }

    return render(request, 'ordersPending.html', context)


# ---------- Remove Order ---------- #


def removeOrder(request, pk):
    order = Order.objects.get(id=pk)
    order.delete()

    order_item = order.item
    order_item_quantity = order.quantity

    item = Item.objects.get(name=order_item)
    item.quantity = item.quantity + order_item_quantity

    item.save()

    return redirect('orders')

# ---------- Remove Item ---------- #
