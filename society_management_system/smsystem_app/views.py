from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SellerForm, BuyerForm, LoginForm, HouseDetailsForm, SocietyForm
from .models import Society,Buyer, Seller, HouseDetails

# Create your views here.

def home(request):
    return render(request, 'home.html')

def admin_home(request):
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    return render(request, 'admin_home.html')

def buyer_home(request):
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    return render(request, 'buyer_home.html')

def seller_home(request):
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    return render(request, 'seller_home.html')


def logout_view(request):
    logout(request)
    return redirect('/')


def loginview(request):
    if request.method == 'POST':
        print("kkkkkkkkkkk")
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_staff:
                return redirect('admin_home')
            if hasattr(user, 'buyeruser'):
                return redirect('buyer_home')
            if hasattr(user, 'selleruser'):
                return redirect('seller_home')
        else:
            print("hereeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee")
            messages.info(request, 'invalid credentials')
    print("jjjjjjjjjjjjjjjjjjjjjjjjjj")
    return render(request, 'login.html')


def seller_register(request):
    login_form = LoginForm()
    seller_form = SellerForm()
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        seller_form = SellerForm(request.POST)
        if login_form.is_valid() and seller_form.is_valid():
            user = login_form.save(commit=False)
            user.user_type = 'seller'
            user.save()
            seller = seller_form.save(commit=False)
            seller.user = user
            seller.save()
            messages.info(request, 'Seller Registered Successful')
            return redirect('seller_register')
    return render(request, 'seller_register.html', {'login_form': login_form, 'seller_form': seller_form})

def buyer_register(request):
    login_form = LoginForm()
    buyer_form = BuyerForm()
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        buyer_form = BuyerForm(request.POST)
        if login_form.is_valid() and buyer_form.is_valid():
            user = login_form.save(commit=False)
            user.user_type = 'buyer'
            user.save()
            buyer = buyer_form.save(commit=False)
            buyer.user = user
            buyer.save()
            messages.info(request, 'buyer Registered Successful')
            return redirect('buyer_register')
    return render(request, 'buyer_register.html', {'login_form': login_form, 'buyer_form': buyer_form})

def add_society(request):
    form = SocietyForm()
    if request.method == 'POST':
        form = SocietyForm(request.POST)
        form.save()
        messages.info(request, 'Society Successful')
        return redirect('view_society')
    return render(request, 'add_society.html', {'society_form': form})

def view_society(request):
    societies = Society.objects.all()
    return render(request, 'view_society.html', {'socities': societies})

def view_buyers(request):
    buyers = Buyer.objects.all()
    return render(request, 'buyers_view_admin.html', {'buyers': buyers})

def view_sellers(request):
    sellers = Seller.objects.all()
    return render(request, 'sellers_view_admin.html', {'sellers': sellers})

def view_society_buyer(request):
    societies = Society.objects.all()
    return render(request, 'view_society_buyer.html', {'socities': societies})

def view_society_seller(request):
    societies = Society.objects.all()
    return render(request, 'view_society_seller.html', {'socities': societies})

def view_buyers_for_seller(request):
    buyers = Buyer.objects.all()
    return render(request, 'buyers_view.html', {'buyers': buyers})

def view_sellers_for_buyer(request):
    sellers = Seller.objects.all()
    return render(request, 'sellers_view.html', {'sellers': sellers})

def add_house(request):
    form = HouseDetailsForm()
    if request.method == 'POST':
        form = HouseDetailsForm(request.POST)
        form.save()
        return redirect('view_house')
    return render(request, 'add_house.html', {'house_form': form})
    
def view_house(request):
    houses = HouseDetails.objects.all()
    return render(request, 'view_houses.html', {'houses': houses})