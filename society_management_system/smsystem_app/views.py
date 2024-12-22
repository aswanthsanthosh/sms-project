from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SellerForm, BuyerForm, LoginForm, HouseDetailsForm, SocietyForm, MessageForm
from .models import Society,Buyer, Seller, HouseDetails, BookingRequest, Message, CustomUser
from django.urls import reverse
from django.db.models import Q

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
    houses = HouseDetails.objects.filter(seller__user=request.user)
    return render(request, 'view_houses.html', {'houses': houses})

def view_houses_for_buyer(request, id):
    society = Society.objects.get(id=id)
    houses = HouseDetails.objects.filter(society=society)
    return render(request, 'view_houses_for_buyer.html', {'houses': houses})


def book_a_house(request, id):
    print(request.user)
    print(Buyer.objects.all())
    buyer = Buyer.objects.get(user=request.user)
    house = HouseDetails.objects.get(id=id)
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    if not BookingRequest.objects.filter(
            house=house, buyer=buyer).exists():
        BookingRequest.objects.create(
            house=house,
            buyer=buyer,
            seller=house.seller
        )
    return redirect(reverse('view_houses_for_buyer', kwargs={'id': house.society.id}))

def view_booking_request_buyer(request):
    requests = BookingRequest.objects.filter(
        buyer__user=request.user
    )
    return render(request, 'view_requests_buyer.html', {'booking': requests})

def view_chat_room_for_buyer(request):
    msgs = Message.objects.filter(Q(sender=request.user)|
                                  Q(reciever=request.user))
    msg__senders = set(
        list(msgs.values_list('sender__id', flat=True))+
        list(msgs.values_list('reciever__id', flat=True))
        )
    users = Seller.objects.filter(user__in=msg__senders)
    return render(request, 'chatroom_lay_for_buyer.html', {'messages': users} )

def view_messages_for_buyer(request, id):
    message_form = MessageForm()
    if request.method == 'POST':
        reciever = CustomUser.objects.get(id=id)
        snd_name = Buyer.objects.get(user=request.user).name
        rec_name = Seller.objects.get(user=reciever).name
        message_form = MessageForm(request.POST)
        message = message_form.save(commit=False)
        message.sender = request.user
        message.reciever = reciever
        message.sender_name = snd_name
        message.reciever_name = rec_name
        message.save()
        return redirect(reverse('view_messages_for_buyer', kwargs={'id': id}))
    messages = Message.objects.filter(
        (Q(sender__id=id, reciever=request.user.id) |
     Q(reciever=id, sender__id=request.user.id))
        ).order_by("-created_at")
    print("id", id)
    print(request.user.id)
    print("user", request.user)
    print(messages.values_list('sender', 'reciever'))
    return render(request, 'chatroom.html', {'messages': messages, 'message_form': message_form} )





def view_booking_request_seller(request):
    requests = BookingRequest.objects.filter(
        seller__user=request.user
    )
    return render(request, 'view_requests_seller.html', {'booking': requests})

def view_chat_room_for_seller(request):
    msgs = Message.objects.filter(Q(sender=request.user)|
                                  Q(reciever=request.user))
    msg__senders = set(
        list(msgs.values_list('sender__id', flat=True))+
        list(msgs.values_list('reciever__id', flat=True))
        )
    users = Buyer.objects.filter(user__in=msg__senders)
    return render(request, 'chatroom_lay_for_seller.html', {'messages': users} )

def view_messages_for_seller(request, id):
    message_form = MessageForm()
    if request.method == 'POST':
        reciever = CustomUser.objects.get(id=id)
        snd_name = Seller.objects.get(user=request.user).name
        rec_name = Buyer.objects.get(user=reciever).name
        message_form = MessageForm(request.POST)
        message = message_form.save(commit=False)
        message.sender = request.user
        message.reciever = reciever
        message.sender_name = snd_name
        message.reciever_name = rec_name
        message.save()
        return redirect(reverse('view_messages_for_seller', kwargs={'id': id}))
    messages = Message.objects.filter(
        (Q(sender__id=id, reciever=request.user.id) |
     Q(reciever=id, sender__id=request.user.id))
        ).order_by("-created_at")
    return render(request, 'chatroom_seller.html', {'messages': messages, 'message_form': message_form} )

def handle_request_seller_approve(request, id):
    booking = BookingRequest.objects.get(
        id=id
    )
    booking.status = 'approved'
    booking.save()
    return redirect('view_booking_request_seller')

def handle_request_seller_reject(request, id):
    booking = BookingRequest.objects.get(
        id=id
    )
    booking.status = 'rejected'
    booking.save()
    return redirect('view_booking_request_seller')


def view_houses_for_admin(request, id):
    society = Society.objects.get(id=id)
    houses = HouseDetails.objects.filter(society=society)
    return render(request, 'view_houses_for_admin.html', {'houses': houses})

def view_booking_request_admin(request):
    requests = BookingRequest.objects.all()
    return render(request, 'view_requests_admin.html', {'booking': requests})

def handle_request_admin_approve(request, id):
    booking = BookingRequest.objects.get(
        id=id
    )
    booking.status = 'approved'
    booking.save()
    return redirect('view_booking_request_admin')

def handle_request_admin_reject(request, id):
    booking = BookingRequest.objects.get(
        id=id
    )
    booking.status = 'rejected'
    booking.save()
    return redirect('view_booking_request_admin')