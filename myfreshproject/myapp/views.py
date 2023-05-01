from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .models import *
from .forms import SignUpForm, ImageForm


# Create your views here.
def register(request):
    form = UserCreationForm()
    return render(request, 'register.html', {'form': form})


def index(request):
    return render(request, 'index.html')


def blog(request):
    return render(request, 'blog.html')


def about(request):
    return render(request, 'about.html')


def accesories(request):
    return render(request, 'accesories.html')


def contact(request):
    return render(request, 'contact.html')

def profile(request):
    return render(request, 'contact.html')

def add_product(request):  
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        print('the form')
        print(form.errors)
        if form.is_valid():
            print('I am valid')
            form.save()
            return redirect('products')
        else:
            return render(request, 'add_product.html', {'form': form})
    else:
        return render(request, 'add_product.html', {'form': ImageForm})
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        
        if form.is_valid():
            print(form.data)
            User = form.save()

            login(request, User)

            return redirect("../''")
    else:
        form =SignUpForm()
    
    return render(request, 'signup.html', {'form': form})

def products(request):
    products = Product.objects.all()
    return render(request, 'products.html', {'products' :products})
    
