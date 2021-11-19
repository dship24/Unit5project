from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .models import *
from .forms import OrderForm, CreateUserForm, CreateProductForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user, allowed_users, admin_only
from django.contrib.auth.models import Group

@unauthenticated_user
def registerPage(request):
    if request.user.is_authenticated:
        return redirect('admin')
    else:
        form = CreateUserForm()
        if request.POST:
            form = CreateUserForm(request.POST)
            if form.is_valid():
                user = form.save()
                group = Group.objects.get(name="customer")
                user.groups.add(group)
                name = form.cleaned_data['username']
                email = form.cleaned_data['email']
                password = form.cleaned_data['password2']
                customer = Customer(name=name, email=email, password=password)
                customer.save()
                messages.success(request, "Account created!")
                return redirect('login')
        context = {"form":form}
        return render(request, 'register.html', context)


@unauthenticated_user
def loginPage(request):
    if request.user.is_authenticated:
        return redirect('admin')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)
        
            if user is not None:
                login(request, user)
                return redirect('admin')
            else:
                messages.info(request, "Username OR Password is incorrect!")

        context = {}
        return render(request, 'login.html', context)

    
def logoutUser(request):
    logout(request)
    return redirect('home')

@login_required(login_url="login")
@admin_only
def admin_page(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()
    products = Item.objects.all()
    total_customers = customers.count()
    total_orders = orders.count()
    delivered = orders.filter(status='Delivered').count()
    delivering = orders.filter(status='Out for delivery').count()
    pending = orders.filter(status='Pending').count()

    context = {'orders':orders, 'customers':customers, 'total_orders':total_orders, 'total_customers': total_customers, 'delivered':delivered, 'delivering':delivering, 'pending':pending, 'products':products}
    return render(request, 'admin.html', context)


@login_required(login_url="login")
def user(request):
    products = Item.objects.all()
    context = {'products':products}
    return render(request, 'user.html', context)


@login_required(login_url='login')
@admin_only
def update_product(request, name):
    product = Item.objects.get(name=name)
    form = CreateProductForm()
    if request.POST:
        form = CreateProductForm(request.POST)
        if form.is_valid():
            product = Item.objects.get(name=name)
            name = form.cleaned_data['name']
            price = form.cleaned_data['price']
            category = form.cleaned_data['category']
            description = form.cleaned_data['description']
            link = form.cleaned_data['img_link']
            product.name = name
            product.price = price
            product.category = category
            product.description = description
            product.img_link = link
            product.save()
            return redirect('admin')
    context = {"form":form, "product":product}
    return render(request, 'update_product.html', context)

@login_required(login_url='login')
@admin_only
def create_product(request):
    form = CreateProductForm()
    if request.POST:
        form = CreateProductForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            price = form.cleaned_data['price']
            category = form.cleaned_data['category']
            description = form.cleaned_data['description']
            link = form.cleaned_data['img_link']
            product = Item(name=name, price=price, category=category, description=description, img_link=link)
            product.save()
            return redirect('admin')
    context = {"form":form}
    return render(request, 'create_product.html', context)


@login_required(login_url='login')
def delete_order(request, id):
    order = Order.objects.filter(id=id)
    order.delete()
    return redirect('admin')

def home(request):
    products = Item.objects.all()
    context = {'products': products}
    return render(request, 'home.html', context)


@login_required(login_url='login')
def user_orders(request, name):
    customer = Customer.objects.get(name=name)
    orders = Order.objects.filter(customer=customer)
    total_orders = orders.count()
    delivered = orders.filter(status='Delivered').count()
    context = {'orders': orders, 'total_orders': total_orders, 'delivered':delivered}
    return render(request, 'user_orders.html', context)


@login_required(login_url='login')
@admin_only
def delete_product(request, name):
    product = Item.objects.filter(name=name)
    product.delete()
    return redirect('admin')


@login_required(login_url='login')
@admin_only
def update_order(request, id, status):
    order = Order.objects.get(id=id)
    order.status = status
    order.save()
    return redirect('admin')


@login_required(login_url='login')
def order_item(request, name):
    user = Customer.objects.get(name=request.user)
    product = Item.objects.get(name=name)
    order = Order(customer = user, item = product, status="Pending")
    order.save()
    messages.success(request, "Your order has been placed!")
    return redirect('user')
