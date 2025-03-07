from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('contact', views.contact, name='contact'),
    path('add-to-cart/', views.cart, name='add_to_cart'),
    path('cart_list_view', views.cart_view, name='cart_list_view'),
]