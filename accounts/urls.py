from django.urls import path, include

from .views import SignUpView


urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),

    # paypal URL
    path('paypal/' , include('paypal.standard.ipn.urls')),

    # #payment Success
    # path('payment-completed/' , payment_completed_view , name='payment-completed'),

    # #payment Failed
    # path('payment-failed/' , payment_completed_view , name='payment-failed'),


]