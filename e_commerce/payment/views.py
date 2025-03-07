import requests
import uuid
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Payment
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
@csrf_exempt
def check_payment(request):
    if request.method == "POST":
        email = request.POST.get("email")
        amount = request.POST.get("amount")
        cart_id = request.POST.get("cart_id")

        if not email or not amount:
            return JsonResponse({"error": "Email and amount are required"}, status=400)

        # ✅ Convert email string to a User instance
        user = get_object_or_404(User, email=email)
        
        reference = str(uuid.uuid4())  # Unique reference ID
        payment = Payment.objects.create(
            reference=reference,
            email=user,  
            amount=amount
        )

        return JsonResponse({"success": "Payment initiated", "reference": reference})

    return JsonResponse({"error": "Invalid request method"}, status=405)
@csrf_exempt
def verify_payment(request, reference):
    headers = {"Authorization": f"Bearer {settings.CHAPA_SECRET_KEY}"}
    
    response = requests.get(
        f"{settings.CHAPA_BASE_URL}/transaction/verify/{reference}",
        headers=headers,
    )
    
    res_data = response.json()
    
    if res_data.get("status") == "success":
        payment = Payment.objects.get(reference=reference)
        payment.status = "successful"
        payment.save()
        return JsonResponse({"message": "Payment successful"})
    
    return JsonResponse({"error": "Payment verification failed"}, status=400)
