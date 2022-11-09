from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import *

from django.contrib.auth.models import User, Group

import collections
import functools
import operator

class UpdateQuantity():
    def __init__(self):
        lst = []
        items = Item.objects.all()
        category = Category.objects.all()

        if items is not None:
            for i in items:
                dlist = {i.category.name:i.quantity}
                lst.append(dlist)

                # sum the values with same keys
                res = dict(functools.reduce(operator.add,
                                            map(collections.Counter, lst)))

                for r in res:
                    for c in category:
                        if  r == c.name:
                            c.quantity = res[r]
                            c.save()


@receiver(post_save, sender=Item)
def CreateItem(sender, instance, created, **kwargs):
    if created:
        UpdateQuantity()

@receiver(post_delete, sender=Item)
def DeleteItem(sender, instance, *args, **kwargs):
    UpdateQuantity()

@receiver(post_save, sender=Item)
def UpdateItem(sender, instance, created, **kwargs):
    if created == False:
        UpdateQuantity()

@receiver(post_save, sender=User)
def CreateUser(sender, instance, created, **kwargs):
    if created:
        group = Group.objects.get(name='customer')
        instance.groups.add(group)

        Customer.objects.create(user=instance, name=instance.username, email=instance.email)

        username = instance.username
    
        print('profile created for ' + username)

@receiver(post_save, sender=User)
def UpdateUser(sender, instance, created, **kwargs):
    if created == False:
        username = instance.username
        instance.customer.save()
        print('profile updated for ' + username)


# @receiver(post_save, sender=Customer)
# def CreateCustomer(sender, instance, created, **kwargs):
#     if created:
#         user = User.objects.create_user(name=instance.username, email=instance.email)
#         user.save()
#         print('success')