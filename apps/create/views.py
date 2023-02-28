from django.shortcuts import render, redirect

from django.contrib import messages  # import messages

from apps.core.models import *

from .forms import CategoryForm, ItemForm, OrderForm, TagForm
from apps.core.decorators import allowed_user

from django.contrib.auth.decorators import login_required

from apps.core.models import Item


# Create your views here.


@login_required(login_url='login')
@allowed_user(allowed=['admin'])
def create(request):
    itemForm = ItemForm()
    categoryForm = CategoryForm()
    tagForm = TagForm()
    orderForm = OrderForm()

    if request.method == 'POST':
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
                messages.success(request, "not enough item on the stock")
            else:
                items.quantity = items.quantity-quantity
                items.save()

            orderForm.save()
            return redirect('orders')

    context = {
        'navbar': 'create',
        'itemform': itemForm,
        'categoryForm': categoryForm,
        'tagForm': tagForm,
        'orderForm': orderForm,
    }

    return render(request, 'create.html', context)
