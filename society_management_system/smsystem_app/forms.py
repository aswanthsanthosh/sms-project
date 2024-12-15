from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import CustomUser, Seller, Buyer, HouseDetails, Society, BookingRequest, Message



class LoginForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'password1', 'password2')

class SellerForm(forms.ModelForm):
    class Meta:
        model = Seller
        fields = "__all__"
        exclude = ["user"]

class BuyerForm(forms.ModelForm):
    class Meta:
        model = Buyer
        fields = "__all__"
        exclude = ["user"]

class HouseDetailsForm(forms.ModelForm):
    class Meta:
        model = HouseDetails
        fields = "__all__"

class SocietyForm(forms.ModelForm):
    class Meta:
        model = Society
        fields = "__all__"

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ["message_text"]
