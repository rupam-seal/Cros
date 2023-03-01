from django.shortcuts import render, redirect
from apps.core.models import *

from apps.core.decorators import allowed_user

from django.contrib.auth.decorators import login_required


# Create your views here.
# --------- ORDERS --------- #


@login_required(login_url='login')
@allowed_user(allowed=['admin', 'staff'])
def orders(request):
    user_id = request.user.username
    if user_id == 'admin':
        orders = Order.objects.all()
    else:
        user = Staff.objects.get(name=user_id)
        orders = Order.objects.filter(seller=user)

    orders_pending_count = orders.filter(status='Pending').count()
    orders_paid_count = orders.filter(status='Paid').count()

    context = {
        'navbar': 'orders',
        'orders': orders,
        'orders_pending_count': orders_pending_count,
        'orders_paid_count': orders_paid_count,
    }

    return render(request, 'orders.html', context)


@login_required(login_url='login')
@allowed_user(allowed=['admin', 'staff'])
def ordersPaid(request):
    user_id = request.user.username
    if user_id == 'admin':
        paid_orders = Order.objects.filter(status='Paid')
    else:
        user = Staff.objects.get(name=user_id)

        orders = Order.objects.filter(seller=user)
        paid_orders = orders.filter(status='Paid')

    paid_order_count = paid_orders.count()

    context = {
        'orders': paid_orders,
        'navbar': 'orders',
        'order_count': paid_order_count,
        'items_count': paid_order_count,
    }

    return render(request, 'ordersPaid.html', context)


@login_required(login_url='login')
@allowed_user(allowed=['admin', 'staff'])
def ordersPending(request):
    user_id = request.user.username
    if user_id == 'admin':
        pending_orders = Order.objects.filter(status='Pending')
    else:
        user = Staff.objects.get(name=user_id)

        orders = Order.objects.filter(seller=user)
        pending_orders = orders.filter(status='Pending')

    pending_order_count = pending_orders.count()

    context = {
        'orders': pending_orders,
        'navbar': 'orders',
        'order_count': pending_order_count,
        'items_count': pending_order_count,
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
