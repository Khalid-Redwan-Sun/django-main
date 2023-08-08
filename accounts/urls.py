<<<<<<< HEAD
from django.urls import path, include
=======
from django.urls import path
>>>>>>> 4c91c8f0505e05f4b243f31cc1871d4815965e58

from .views import SignUpView


urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
<<<<<<< HEAD

    # paypal URL
    path('paypal/' , include('paypal.standard.ipn.urls')),

    # #payment Success
    # path('payment-completed/' , payment_completed_view , name='payment-completed'),

    # #payment Failed
    # path('payment-failed/' , payment_completed_view , name='payment-failed'),


=======
>>>>>>> 4c91c8f0505e05f4b243f31cc1871d4815965e58
]