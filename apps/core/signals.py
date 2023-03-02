from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import *

from django.contrib.auth.models import User, Group


@receiver(post_save, sender=User)
def CreateUser(sender, instance, created, **kwargs):
    if created:
        group = Group.objects.get(name='staff')
        instance.groups.add(group)

        username = instance.username

        staff = Staff(user=instance, name=instance.username,
                      email=instance.email)
        staff.save()

        print('profile created for ' + username)


@receiver(post_save, sender=User)
def UpdateUser(sender, instance, created, **kwargs):
    if created == False:
        username = instance.username
        print('profile updated for ' + username)
