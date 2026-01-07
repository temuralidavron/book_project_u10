from django.shortcuts import render, redirect

from book.forms import BookForm
from book.models import Book


# Create your views here.
def get_book(request):
    books=Book.objects.all()
    context={
        'books':books
    }
    return render(request,"book/list.html",context)


def create_book(request):
    if request.method=='POST':
        form=BookForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect("book-list")
    else:
        form=BookForm()
    return render(request,"book/create.html",{'form':form})


def detail_book(request,pk):
    book=Book.objects.filter(pk=pk).first()
    # context={
    #     'book':book
    # }
    return render(request,"book/detail.html",{'book':book})