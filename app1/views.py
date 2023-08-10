from django.shortcuts import render

# Create your views here.
from app1.models import *
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
class School_list(ListView):
    model=School
    context_object_name='slo'

class School_detail(DetailView):
    model=School
    context_object_name='sdo'

class School_create(CreateView):
    model=School
    fields='__all__'

class School_update(UpdateView):
    model=School
    fields='__all__'

class School_delete(DeleteView):
    model=School
    context_object_name='sdo'
    success_url=reverse_lazy('School_list')
    
