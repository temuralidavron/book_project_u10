from django.db import models

class Category(models.Model):
    title=models.CharField(max_length=200)

    def __str__(self): # obj nomlab qo'yish
        return self.title


class Author(models.Model):  # Navoiy id 22
    full_name=models.CharField(max_length=300)
    country=models.CharField(max_length=300)
    description=models.TextField()
    image=models.ImageField(upload_to="author")

    def __str__(self):
        return self.full_name

class Book(models.Model): # Xamsa
    title=models.CharField(max_length=500)
    isbn=models.CharField(max_length=13)
    page=models.IntegerField()
    description=models.TextField()
    price=models.IntegerField()
    quantity=models.IntegerField()
    image=models.ImageField(upload_to="book")
    author_id=models.ForeignKey(Author,on_delete=models.CASCADE,related_name="books")  # 22
    category=models.ForeignKey(Category,on_delete=models.CASCADE,related_name="book_cat")



