from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import models, forms

def addBook(request):
    form = forms.bookForm()
    
    if request.method == 'POST':
        form = forms.bookForm(request.POST , request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')

    return render(request, 'add.html', {'form': form})


def home(request):
    books = models.book.objects.all()
    return render(request , 'home.html' , {'books': books})


def updateBook(request , id=id):
    book  = models.book.objects.get(id=id)
    form = forms.bookForm(instance=book)
    if request.method == 'POST':
        form = forms.bookForm(request.POST , request.FILES , instance=book)
        if form.is_valid():
            form.save()
            return redirect('home')
    
    return render(request , 'add.html' , {'form': form , "edit": True})


def deleteBook(request , id=id):
    book = models.book.objects.get(id=id)
    book.delete()
    return redirect('home')
