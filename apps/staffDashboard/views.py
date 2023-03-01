from django.shortcuts import render
from apps.core.decorators import allowed_user

from django.contrib.auth.decorators import login_required

from apps.core.models import *

# Create your views here.


'''
    -------- STAFF ----------
'''


@login_required(login_url='login')
@allowed_user(allowed=['staff'])
def staffDashboard(request):
    user_id = request.user.username

    user = Staff.objects.get(name=user_id)

    orders = Order.objects.filter(seller=user)
    total_orders = orders.count()
    orders_pending = orders.filter(status='Pending')
    orders_pending_count = orders_pending.count()
    orders_paid = orders.filter(status='Paid')
    orders_paid_count = orders_paid.count()

    total_cash = 0
    for cash in orders_paid:
        total_cash += cash.price*cash.quantity

    context = {
        'navbar': 'dashboard',
        'orders': orders,
        'total_orders': total_orders,
        'orders_pending_count': orders_pending_count,
        'orders_paid_count': orders_paid_count,
        'total_cash': total_cash,
    }

    return render(request, 'staffDashboard.html', context)
