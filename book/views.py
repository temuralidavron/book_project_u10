from django.shortcuts import render, redirect

from account.permission import required_user, admin_required
from book.forms import BookForm
from book.models import Book


# Create your views here.
def get_book(request):
    books=Book.objects.all()
    context={
        'books':books
    }
    return render(request,"book/list.html",context)

@admin_required
def create_book(request):
    if request.method=='POST':
        form=BookForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect("book-list")
    else:
        form=BookForm()
    return render(request,"book/create.html",{'form':form})

@required_user
def detail_book(request,pk):
    book=Book.objects.filter(pk=pk).first()
    # context={
    #     'book':book
    # }
    return render(request,"book/detail.html",{'book':book})