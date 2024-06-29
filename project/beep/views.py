from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
# from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import *
from .forms import *

def event_list(request):
    events = Event.objects.all()
    return render(request, 'event_list.html', {'events': events})

def selection(request):
    model = User.objects.all()
    return render(request, 'select.html', {'users': model})

def home(request):
    user_id = request.POST.get('user_id')
    us = get_object_or_404(User, id=user_id) if user_id else None
    ev = Event.objects.all()
    at = Attendee.objects.all()
     
    return render(request, 'home.html', {'user': us,'events': ev,'attendant': at})

