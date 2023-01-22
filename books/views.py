from django.shortcuts import render
from django.views.generic import *
from .models import *


# Create your views here.
class BookListView(ListView):
    model = Book
    template_name = "book_list.html"
    context_object_name = "book_list"
