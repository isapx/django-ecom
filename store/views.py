from django.shortcuts import redirect, render
from .models import Product, Category
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
from django import forms


def category_summary(request):
    categories = Category.objects.all()
    return render(request, 'category_summary.html', {"categories": categories})

def category(request, foo):
    #reemplazamos guion con espacios
    foo = foo.replace('-',' ')
    # obtenemos la categoria de la url
    try:
        #buscamos la categoria
        category = Category.objects.get(name=foo)
        products = Product.objects.filter(category=category)
        return render(request, 'category.html', {'products': products, 'category': category})
    except:
        messages.success(request,("Esta categoria no existe"))
        return redirect('home')

def product(request, pk):
    product = Product.objects.get(id=pk)
    return render(request,'product.html',{'product':product})


def home(request): #esta es la view que se llama de urls.py
    products = Product.objects.all()
    return render(request,'home.html',{'products':products}) #este home.html se busca en el directorio Templates que hay que crear

def about(request):
    return render(request,'about.html',{})

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        #aqui usamos la funcion authenticate de django para hacer el login
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ("Acceso exitoso!"))
            return redirect('home')
        else:
            messages.success(request, ("Hubo un error, intenta de nuevo"))
            return redirect('login')
    else:
        return render(request,'login.html',{})


def logout_user(request):
    logout(request)
    messages.success(request, ("Logout exitoso!"))
    return redirect('home')

def register_user(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            #logueamos al usuario
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("Registro exitoso!"))
            return redirect('home')
        else:
            messages.success(request, ("Hubo un problema con el registro, intenta de nuevo!"))
            return render(request,'register.html',{})
    else:
        return render(request,'register.html',{'form':form})