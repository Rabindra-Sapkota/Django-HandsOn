from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse('<p>Reached Till View</p>')


def customer_info(request, customer_id):
    return HttpResponse(f'<p>Trying to search for: {customer_id}</p>')
