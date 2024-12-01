from django.urls import path, include
from smsystem_app import views

urlpatterns = [
    path('', views.home, name='home'),
    path('admin_home/', views.admin_home, name='admin_home'),
    path('login_view',views.loginview,name='login_view'),
    path('logout_view',views.logout_view,name='logout_view'),

    path('seller_register', views.seller_register, name='seller_register'),
    path('buyer_register', views.buyer_register, name='buyer_register'),
    path('buyer_home/', views.buyer_home, name='buyer_home'),
    path('seller_home/', views.seller_home, name='seller_home'),
    path('add_society', views.add_society, name='add_society'),
    path('view_society', views.view_society, name='view_society'),
    path('view_buyers', views.view_buyers, name='view_buyers'),
    path('view_sellers', views.view_sellers, name='view_sellers'),


    #buyer
    path('view_sellers_for_buyer', views.view_sellers_for_buyer, name='view_sellers_for_buyer'),
    path('view_society_buyer', views.view_society_buyer, name='view_society_buyer'),

    #seller
    path('view_buyers_for_seller', views.view_buyers_for_seller, name='view_buyers_for_seller'),
    path('view_society_seller', views.view_society_seller, name='view_society_seller'),
    path('add_house', views.add_house, name='add_house'),
    path('view_house', views.view_house, name='view_house'),




    
]