from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models

# Create your models here.


class CustomUserManager(BaseUserManager):
    def create_user(self, username, email=None, password=None, **extra_fields):
        if email:
            email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self.create_user(username, email, password, **extra_fields)


USER_TYPE_CHOICES = (
        ('admin', 'Admin'),
        ('seller', 'seller'),
        ('buyer', 'buyer'),
    )

class CustomUser(AbstractUser):
    user_type = models.CharField(
        max_length=10, choices=USER_TYPE_CHOICES
    )

    objects = CustomUserManager()

class Seller(models.Model):
    user =  models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='selleruser',null=True,blank=True)
    name = models.CharField(max_length=100)
    address = models.TextField()
    phone_number = models.CharField(max_length=20)
    email = models.EmailField(null=True, blank=True)
    location = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self) -> str:
        return self.name

class Buyer(models.Model):
    user =  models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='buyeruser',null=True,blank=True)
    name = models.CharField(max_length=100)
    address = models.TextField()
    phone_number = models.CharField(max_length=20)
    email = models.EmailField(null=True, blank=True)

    def __str__(self) -> str:
        return self.name

class Society(models.Model):
    name = models.CharField(max_length=100)
    number_of_houses = models.IntegerField()

    def __str__(self) -> str:
        return self.name

SELLING_TYPE = (('rent', 'rent'),
                ('sell', 'sell'))

HOUSE_TYPE = (('house', 'house'),
                ('villa', 'villa'),
                ('apartment', 'apartment'),
                ('apartment', 'apartment'),
                ('bungalow', 'bungalow')
                )

class HouseDetails(models.Model):
    house_name = models.CharField(max_length=100)
    house_number = models.CharField(max_length=20)
    society = models.ForeignKey(
        Society, 
        related_name='house',
        on_delete=models.CASCADE,
        null=True, blank=True
    ) 
    selling_type = models.CharField(
        choices=SELLING_TYPE,
        max_length=20
    )
    house_type = models.CharField(
        choices=HOUSE_TYPE,
        max_length=20
    )
    location = models.CharField(max_length=100)
    address = models.TextField()
    seller = models.ForeignKey(
        Seller, 
        related_name='house',
        on_delete=models.CASCADE,
        null=True, blank=True
    ) 

    def __str__(self) -> str:
        return self.house_name
    
STATUS = (('approved', 'approved'),
                ('rejected', 'rejected'),
                ('pending', 'pending'))

class BookingRequest(models.Model):
    seller = models.ForeignKey(
        Seller, on_delete=models.CASCADE,
    )
    buyer = models.ForeignKey(
        Buyer, on_delete=models.CASCADE,
    )
    house = models.ForeignKey(
        HouseDetails, on_delete=models.CASCADE,
    )
    status = models.CharField(
        choices=STATUS,
        max_length=20,
        null=True, blank=True,
        default='pending'
    )


class Message(models.Model):
    sender = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE,
        related_name='message_sender'
    )
    reciever = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE,
        related_name='message_reciever'
    )
    sender_name = models.CharField(
        max_length=100, null=True, blank=True
    )
    reciever_name = models.CharField(
        max_length=100, null=True, blank=True
    )
    message_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
