from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Machine, Queue_Entry
from django.contrib.auth.decorators import login_required

# Create your views here.

def home_page(request):
    return render(request, 'laundry/home_page.html')

def hall_page(request, hall):
    hall_machine = Machine.objects.filter(hall__exact = hall)
    return render(request, 'laundry/hall_page.html', {'machines': hall_machine})
