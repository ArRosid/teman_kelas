import imp
from django.shortcuts import render
from django.views.generic.edit import CreateView, DeleteView
from django.views.generic.list import ListView
from teman.models import Teman
# Create your views here.


class TemanCreateView(CreateView):
    model = Teman
    fields = ["nama", "umur", "alamat", "foto"]
    success_url = "/"



class TemanListView(ListView):
    model = Teman


class TemanDeleteView(DeleteView):
    model = Teman
    success_url = "/"