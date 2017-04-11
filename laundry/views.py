from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Machine, Queue_Entry
from django.contrib.auth.decorators import login_required
from .forms import UserForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

# Create your views here.

def home_page(request):
    return render(request, 'laundry/home_page.html')

def hall_page(request, hall):
    hall_machine = Machine.objects.filter(hall__exact = hall)
    return render(request, 'laundry/hall_page.html', {'halls': hall_machine})

def user_new(request):
	if request.method == "POST":
		form = UserForm(request.POST)
		if form.is_valid():
			new_user = User.objects.create_user(**form.cleaned_data)
			login(request, new_user)
			return redirect('home_page')
	else:
		form = UserForm()
	return render(request, 'laundry/user_edit.html', {'form':form})

def user_login(request):
	username = request.POST['username']
	password = request.POST['password']
	user = authenticate(request, username=username, password=password)
	if user is not None:
		login(request,user)
		return redirect('home_page')
	else:
		return #error message, invalid login