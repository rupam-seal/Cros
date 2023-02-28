from django.shortcuts import render, redirect

from apps.core.models import *

from apps.core.decorators import allowed_user

from django.contrib.auth.decorators import login_required
# Create your views here.
# --------- CATEGORY --------- #


@login_required(login_url='login')
@allowed_user(allowed=['admin'])
def category(request):
    categories = Category.objects.all()
    category_count = categories.count()

    context = {
        'navbar': 'category',
        'categories': categories,
        'category_count': category_count,
    }

    return render(request, 'category.html', context)


@login_required(login_url='login')
@allowed_user(allowed=['admin'])
def items(request, pk):
    category = Category.objects.get(id=pk)

    items = Item.objects.filter(category=category)
    items_count = items.count()

    context = {
        'navbar': 'category',
        'items': items,
        'items_count': items_count,
    }

    return render(request, 'items.html', context)


def removeItem(request, pk):
    item = Item.objects.get(id=pk)
    item.delete()
    return redirect('category')
