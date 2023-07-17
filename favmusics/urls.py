from django.urls import path
from . import views

urlpatterns = [ 
    # path('', views.home, name='home'), 
    path('', views.HomeView.as_view(), name='home'),
    path('customer_info/<int:customer_id>/', views.DetailView.as_view(), name='customer_info'),
]