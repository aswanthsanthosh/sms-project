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
    path('view_houses_for_admin/<int:id>', views.view_houses_for_admin, name='view_houses_for_admin'),
    path('view_booking_request_admin', views.view_booking_request_admin, name='view_booking_request_admin'),
    path('handle_request_admin_approve/<int:id>', views.handle_request_admin_approve, name='handle_request_admin_approve'),
    path('handle_request_admin_reject/<int:id>', views.handle_request_admin_reject, name='handle_request_admin_reject'),


    #buyer
    path('view_sellers_for_buyer', views.view_sellers_for_buyer, name='view_sellers_for_buyer'),
    path('view_society_buyer', views.view_society_buyer, name='view_society_buyer'),
    path('view_houses_for_buyer/<int:id>', views.view_houses_for_buyer, name='view_houses_for_buyer'),
    path('book_a_house/<int:id>', views.book_a_house, name='book_a_house' ),
    path('view_booking_request_buyer', views.view_booking_request_buyer, name='view_booking_request_buyer'),
    path('view_messages_for_buyer/<int:id>', views.view_messages_for_buyer, name='view_messages_for_buyer'),
    path('view_chat_room_for_buyer', views.view_chat_room_for_buyer, name='view_chat_room_for_buyer'),

    #seller
    path('view_buyers_for_seller', views.view_buyers_for_seller, name='view_buyers_for_seller'),
    path('view_society_seller', views.view_society_seller, name='view_society_seller'),
    path('add_house', views.add_house, name='add_house'),
    path('view_house', views.view_house, name='view_house'),
    path('view_booking_request_seller', views.view_booking_request_seller, name='view_booking_request_seller'),
    path('handle_request_seller_approve/<int:id>', views.handle_request_seller_approve, name='handle_request_seller_approve'),
    path('handle_request_seller_reject/<int:id>', views.handle_request_seller_reject, name='handle_request_seller_reject'),
    path('view_messages_for_seller/<int:id>', views.view_messages_for_seller, name='view_messages_for_seller'),
    path('view_chat_room_for_seller', views.view_chat_room_for_seller, name='view_chat_room_for_seller')





    
]