from django.shortcuts import render
from order.models import Food
from django.views.generic import ListView, DetailView 

class OrderLV(ListView):
    model = Food