from django.contrib import admin
from smsystem_app.models import Seller, Buyer, HouseDetails, Society, BookingRequest, Message


# Register your models here.

admin.site.register(Seller)
admin.site.register(Buyer)
admin.site.register(HouseDetails)
admin.site.register(Society)
admin.site.register(BookingRequest)
admin.site.register(Message)

