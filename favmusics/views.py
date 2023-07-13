from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Customer

# Create your views here.
def home(request):
    customers = Customer.objects.all()
    return render(request, 'home.html', {"customers": customers})


def customer_info(request, customer_id):
    try:
        customer = Customer.objects.get(id=customer_id)
    except Customer.DoesNotExist:
        raise Http404('Customer not found')
    return render(request, 'customer_detail.html', {'customer': customer})
