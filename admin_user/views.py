from django.shortcuts import render, redirect
from django.views.decorators.cache import cache_control
from django.contrib.auth.models import User, Group

from django.contrib import messages #import messages

from core.models import *

from core.forms import CategoryForm, ItemForm, OrderForm, TagForm
from core.decorators import admin_only, allowed_user

from django.contrib.auth.decorators import login_required

from django.http import JsonResponse
from core.models import Item

def search_result(request):
    res = None
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        series = request.POST.get('series')
        query_se = Item.objects.filter(name__icontains=series)

        if len(query_se) > 0 and len(series) > 0:
            data = []
            for pos in query_se:
                items = {
                    'pk':pos.pk,
                    'name':pos.name,
                }
                data.append(items)
            res = data
        else :
            res = "not found"
        
        return JsonResponse({'data':res})
    return JsonResponse({})

    
'''
    -------- ADMIN ---------
'''

# -------- DASHBOARD ---------- #
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='login')
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
        'labels':labels,
        'order_data':order_data,
        'stock_data':stock_data,
        'orders':orders,
        'total_stock':total_stock,
        'total_order':total_order,
        'paid_order':paid_order,
        'pending_order':pending_order,

        'navbar':'dashboard',
    }

    return render(request, 'admin/dashboard.html', context)

# --------- ORDERS --------- #
@login_required(login_url='login')
@allowed_user(allowed=['admin'])
def orders(request):
    orders = Order.objects.all()
    orders_pending_count = Order.objects.filter(status='Pending').count()
    orders_paid_count = Order.objects.filter(status='Paid').count()
    
    
    context = {
        'navbar':'orders',
        'orders':orders,
        'orders_pending_count':orders_pending_count,
        'orders_paid_count':orders_paid_count,
    }

    return render(request, 'orders/orders.html', context)

@login_required(login_url='login')
@allowed_user(allowed=['admin'])
def ordersPaid(request):
    orders = Order.objects.filter(status='Paid')
    order_count = orders.count()

    context = {
        'orders':orders,
        'navbar':'orders',
        'order_count':order_count,
    }

    return render(request, 'orders/ordersPaid.html', context)

@login_required(login_url='login')
@allowed_user(allowed=['admin'])
def ordersPending(request):
    orders = Order.objects.filter(status='Pending')
    order_count = orders.count()

    context = {
        'orders':orders,
        'navbar':'orders',
        'order_count':order_count,
    }

    return render(request, 'orders/ordersPending.html', context)

# --------- CATEGORY --------- #
@login_required(login_url='login')
@allowed_user(allowed=['admin'])
def category(request):
    categories = Category.objects.all()
    category_count = categories.count()

    context = {
        'navbar':'category',
        'categories':categories,
        'category_count':category_count,
    }

    return render(request, 'admin/category.html', context)

# ---------- ITEMS ---------- #
@login_required(login_url='login')
@allowed_user(allowed=['admin'])
def items(request, pk):
    category = Category.objects.get(id=pk)
    
    items = Item.objects.filter(category=category)
    items_count = items.count()

    context = {
        'navbar':'category', 
        'items':items,
        'items_count':items_count,
    }

    return render(request, 'admin/items.html', context)

# ----------- CUSTOMERS ---------- #
@login_required(login_url='login')
@allowed_user(allowed=['admin'])
def customers(request):
    customers = Customer.objects.all()

    # username = request.POST.get('username')
    # email = request.POST.get('email')
    # password = request.POST.get('password')
    # confirmPassword = request.POST.get('confirmPassword')

    # if password != confirmPassword:
    #     print('Password didnt match')
    # else:
    #     print('--------------------------')
    #     user = User.objects.create_user(username=username, password=password, email=email)
    #     print('--------------------------')
    #     group = Group.objects.get(name='customer')
    #     print('--------------------------')
    #     user.groups.add(group)
    #     print('--------------------------')
    #     user.save()
    #     print('--------------------------')
    #     u = User.objects.get(username=username)
        
    
    #     customer = Customer(name=username, email=email, user=u)
    #     customer.save()
    #     return redirect('dashboard')



    context = {
        'navbar':'customers',
        'customers':customers,
    }

    return render(request, 'admin/customers.html', context)

# ---------- CREATE ---------- #
@login_required(login_url='login')
@allowed_user(allowed=['admin'])
def create(request):
    itemForm = ItemForm()
    categoryForm = CategoryForm()
    tagForm = TagForm()
    orderForm = OrderForm()


    if request.method  == 'POST':
        itemForm = ItemForm(request.POST)
        categoryForm = CategoryForm(request.POST)
        tagForm = TagForm(request.POST)
        orderForm = OrderForm(request.POST)

        if itemForm.is_valid():
            itemForm.save()
            return redirect('category')

        if categoryForm.is_valid():
            categoryForm.save()
            return redirect('category')

        if tagForm.is_valid():
            tagForm.save()
            return redirect('dashboard')
        
        if orderForm.is_valid():
            item = orderForm.cleaned_data['item']
            quantity = orderForm.cleaned_data['quantity']

            items = Item.objects.get(name=item)
            if (items.quantity - quantity) == 0:
                messages.success(request, "not enough item on the stock" )
            else:
                items.quantity = items.quantity-quantity
                items.save()

            orderForm.save()
            return redirect('orders')

    context = {
        'navbar':'create',
        'itemform':itemForm,
        'categoryForm':categoryForm,
        'tagForm':tagForm,
        'orderForm':orderForm,
    }

    return render(request, 'admin/create.html', context)

# ---------- REPORT ---------- #
# @login_required(login_url='login')
# @allowed_user(allowed=['admin'])
# def message(request):
#     context = {
#         'navbar':'message',
#     }

#     return render(request, 'admin/message.html', context)

'''
    --------- COMMON ----------
'''
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
def removeItem(request, pk):
    item = Item.objects.get(id=pk)
    item.delete()
    return redirect('category')

