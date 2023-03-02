from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
    GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Others', 'Others'),
    )

    profile_image = models.ImageField(
        default='person.png', null=True, blank=True)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    phone = models.IntegerField(default=0, null=True)
    gender = models.CharField(max_length=200, null=True, choices=GENDER)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name


class Staff(models.Model):
    GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Others', 'Others'),
    )

    profile_image = models.ImageField(
        default='person.png', null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    phone = models.IntegerField(default=0, null=True)
    gender = models.CharField(max_length=200, null=True, choices=GENDER)

    def __str__(self):
        return self.name


class Category(models.Model):
    STATUS = (
        ('High', 'High'),
        ('Low', 'Low'),
    )

    name = models.CharField(max_length=200, null=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name


class Item(models.Model):
    name = models.CharField(max_length=200, null=True)
    price = models.IntegerField(default=0, null=True)
    quantity = models.IntegerField(default=0, null=True)
    category = models.ForeignKey(
        Category, null=True, on_delete=models.SET_NULL)
    tag = models.ForeignKey(Tag, null=200, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    STATUS = (
        ('Paid', 'Paid'),
        ('Pending', 'Pending'),
    )

    customer = models.ForeignKey(
        Customer, null=True, on_delete=models.SET_NULL)
    seller = models.ForeignKey(Staff, on_delete=models.SET_NULL, null=True)
    item = models.ForeignKey(Item, null=True, on_delete=models.SET_NULL)
    price = models.IntegerField(default=0, null=True)
    quantity = models.IntegerField(default=0, null=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return str(self.customer)
