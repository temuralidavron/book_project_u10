from django.urls import path
from .views import get_book, create_book

urlpatterns=[
    path("",get_book,name="book-list"),
    path("create/",create_book,name="book-create"),

]