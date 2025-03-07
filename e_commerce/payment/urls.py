from django.urls import path
from . import views

urlpatterns = [
    path("initiate", views.check_payment, name="initiate"),
    path("verify/<str:reference>", views.verify_payment, name="verify-payment"),
]
