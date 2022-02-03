from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Blue
# Create your views here.

class Add(CreateView):
    model = Blue
    fields = ('title','contenet','app_name')
    template_name = "add.html"
    success_url = '/blue/'