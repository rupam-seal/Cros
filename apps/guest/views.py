from django.shortcuts import render

from .data import data

# Create your views here.


def guestDashboard(request):

    getData = data[0]

    context = {
        # 'labels': labels,
        # 'order_data': order_data,
        # 'stock_data': stock_data,

        'total_stock': getData['total_stock'],
        'total_order': getData['total_order'],
        'paid_order': getData['paid_order'],
        'pending_order': getData['pending_order'],

        'navbar': 'dashboard',
    }

    return render(request, 'dashboard.html', context)
