from django.shortcuts import render
from django.http import JsonResponse
import json
from .models import *

# Create your views here.
def index(request):
    meals = Meal.objects.all()
    ctx = {'meals': meals}
    return render(request, 'index.html', ctx)
def menu(request):
    meals = Meal.objects.all()
    ctx = {'meals': meals}
    return render(request, 'menu.html', ctx)
def about(request):
    ctx = {}
    return render(request, 'about.html', ctx)
def book(request):
    ctx = {}
    return render(request, 'book.html', ctx)

def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order,  created = Order.objects.get_or_create(customer = customer,complete=False)
        items = order.orderitem_set.all()
    else:

        items = []
        order = {'get_cart_total':0, 'get_cart_items':0}

    ctx = {'items':items, 'order':order }
    return render(request, 'cart.html', ctx)

def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer = customer,complete=False)
        items = order.orderitem_set.all()
    else:

        items = []
        order = {'get_cart_total':0, 'get_cart_items':0}

    ctx = {'items':items, 'order':order }
    return render(request, 'checkout.html', ctx)

def updateItem(request):
    data = json.loads(request.body)
    mealId = data['mealId']
    action = data['action']

    print('action', action)
    print('mealId', mealId)

    customer = request.user.customer
    meal = Meal.objects.get(id=mealId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    orderItem, created = OrderItem.objects.get_or_create(order=order, meal=meal)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)
    
    orderItem.save()
    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('Item was added', safe=False)