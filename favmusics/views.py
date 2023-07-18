from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Customer
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView

# Create your views here.
'''
# Function Based
def home(request):
    customers = Customer.objects.all()
    return render(request, 'favmusics/home.html', {"customers": customers})


# Template View
class HomeView(TemplateView):
    template_name = 'favmusics/home.html'
    extra_context = {"customers": Customer.objects.all()}

  
# Function Based
@login_required(login_url='/admin')
def customer_info(request, customer_id):
    try:
        customer = Customer.objects.get(id=customer_id)
    except Customer.DoesNotExist:
        raise Http404('Customer not found')
    return render(request, 'favmusics/customer_detail.html', {'customer': customer})


# Tempalte View
class DetailView(LoginRequiredMixin, TemplateView):
    template_name = 'favmusics/customer_detail.html'
    login_url = '/admin'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        customer_id = self.kwargs['customer_id']
        customer = Customer.objects.get(id=customer_id)
        context["customer"] = customer
        return context
'''

# Generic View
class CustomerView(ListView):
    model = Customer
    # Default Template name: customer_list.html
    template_name = 'favmusics/home.html'
    context_object_name = "customers"   # Name of parameter in template html


class CustomerDetailView(LoginRequiredMixin, DetailView):
    model = Customer
    template_name = 'favmusics/customer_detail.html'
    context_object_name = 'customer'
    login_url = '/admin'
