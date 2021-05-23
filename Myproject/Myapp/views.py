from django.shortcuts import render
from django.http import HttpResponse
from .models import Book
#Create your views here.
def index(request):
    book_list=Book.objects.all()
    context={
        "book_list":book_list
    }
    return render(request,"Myapp/index.html",context)


def detail(request,id):
    return HttpResponse("This is my book number %s" %id)    

