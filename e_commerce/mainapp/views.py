from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import Contact, Products, Cart
from django.contrib.auth.decorators import login_required
# Create your views here.

def home(req):
    products = Products.objects.all()

    return render(req, 'index.html', {'products': products})

def contact(req):
    if req.method == 'POST':
        name = req.POST['name']
        email = req.POST['email']
        subject = req.POST['subject']
        messsage = req.POST['message']
        contact = Contact(name=name, email=email, subject=subject, message=messsage)
        contact.save()
        return redirect('home')
    return render(req, 'contact.html')
@login_required
def cart(req):
    if req.method == 'POST':
        id = req.POST['product_id']
        product = get_object_or_404(Products, id=id)
        cart_item, created = Cart.objects.get_or_create(user=req.user, product= product)
        if not created:
            cart_item.quant += 1
            cart_item.save()
    return JsonResponse({"message": "Added to cart", "quantity": cart_item.quant})
@login_required(login_url='auth/login')
def cart_view(req):
    cart_products = Cart.objects.filter(user=req.user)
    return render(req, 'cart.html', {'carts': cart_products})