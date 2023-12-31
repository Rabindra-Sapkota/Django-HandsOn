from django.urls import path
from . import views

urlpatterns = [ 
    # path('', views.home, name='home'), 
    path('', views.CustomerView.as_view(), name='home'),
    path('customer_info/<int:pk>/', views.CustomerDetailView.as_view(), name='customer_info'),
    path('register', views.CustomerCreateView.as_view(), name='customer_registration'),
    path('add_employee', views.addemployee, name='add_employee'),
]