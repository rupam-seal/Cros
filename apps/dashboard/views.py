from django.shortcuts import render
from django.views.decorators.cache import cache_control

from apps.core.models import *

from apps.core.decorators import admin_only

from django.contrib.auth.decorators import login_required


# Create your views here.

# -------- DASHBOARD ---------- #


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='navigation')
@admin_only
def dashboard(request):
    orders = Order.objects.all()
    items = Item.objects.all()

    total_order = orders.count()
    paid_order = orders.filter(status='Paid').count()
    pending_order = orders.filter(status='Pending').count()

    # counting total stock from items model
    # each item has different stocks count
    total_stock = 0
    for item in items:
        total_stock += item.quantity

    # data for charts
    # jan-dac
    labels = ['Jan', 'Feb', 'Mar', 'Apr',
              'May', 'Jun', 'Jul', 'Aug', 'Sep',
              'Oct', 'Nov', 'Dec']

    # 0 is how many orderd is placed on particular month
    # if no order is placed the default value is 0
    order_data = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    # getting month number when orders are placed
    for order in orders:
        # get month number from date_created
        date = order.date_created.month - 1
        quantity = order.quantity
        # adding '1' to data list on particular index
        # we are getting the index from above date variable
        order_data[date] += quantity

    stock_data = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    for item in items:
        date = item.date_created.month - 1
        stock_data[date] += item.quantity

    context = {
        'labels': labels,
        'order_data': order_data,
        'stock_data': stock_data,
        'orders': orders,
        'total_stock': total_stock,
        'total_order': total_order,
        'paid_order': paid_order,
        'pending_order': pending_order,

        'navbar': 'dashboard',
    }

    return render(request, 'dashboard.html', context)
