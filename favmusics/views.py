from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Customer
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
'''
def home(request):
    customers = Customer.objects.all()
    return render(request, 'favmusics/home.html', {"customers": customers})
'''
class HomeView(TemplateView):
    template_name = 'favmusics/home.html'
    extra_context = 'customers'

"""
@login_required(login_url='/admin')
def customer_info(request, customer_id):
    try:
        customer = Customer.objects.get(id=customer_id)
    except Customer.DoesNotExist:
        raise Http404('Customer not found')
    return render(request, 'favmusics/customer_detail.html', {'customer': customer})
"""
class DetailView(LoginRequiredMixin, TemplateView):
    template_name = 'favmusics/customer_detail.html'
    extra_content = 'customer'
    login_url = 'admin/'
