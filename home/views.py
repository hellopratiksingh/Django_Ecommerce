from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime
from home.models import *
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.http import JsonResponse
import json
import requests

# Create your views here.
def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def services(request):
    return render(request, 'services.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        message = request.POST.get('message')
        contact = Contact(name=name, phone=phone, email=email, message=message, date= datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent')
    return render(request, 'contact.html')


def bicycles(request):
    cycles = bicycle.objects.all()
    return render(request, 'bicycles.html', {'cycles' : cycles})


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 == password2:
            if User.objects.filter(username = username).exists():
                messages.error(request, 'Username Already Exists')
                return redirect('register')
            elif User.objects.filter(email = email).exists():
                messages.error(request, 'Email Already Exists')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password = password1)
                user.save()
                messages.success(request, 'Your Account has been Successfully registered')
                return redirect('login')
        else:
            messages.error(request, 'Password not matching')
            return redirect('register')
    else:
        return render(request, 'register.html')


def login(request):
    return render(request, 'login.html')


def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()

    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0}

    return render(request, 'cart.html')


def updateItem(request):
    data = json.loads(request.body)
    cycleId = data['cycleId']
    action = data['action']
    print('Action:', action)
    print('cycle:', cycleId)

    return JsonResponse('Item was added', safe=False)
