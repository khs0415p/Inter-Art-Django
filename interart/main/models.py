from django.db import models
from django.contrib.auth.models import AbstractUser

# # Create your models here.

class User(AbstractUser):
    gender_choices = (
                    ("남성", "남성"),
                    ("여성", "여성"),
                )
    gender = models.CharField(choices=gender_choices, max_length=2)

    
        
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(null=True, upload_to="%Y/%m/%d", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

# class Book(models.Model):
#     """Model representing a book (but not a specific copy of a book)."""
#     title = models.CharField(max_length=200)
#     author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)

#     # Foreign Key used because book can only have one author, but authors can have multiple books
#     # Author as a string rather than object because it hasn't been declared yet in the file.
#     summary = models.TextField(max_length=1000, help_text='Enter a brief description of the book')
#     isbn = models.CharField('ISBN', max_length=13, help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')

#     # ManyToManyField used because genre can contain many books. Books can cover many genres.
#     # Genre class has already been defined so we can specify the object above.
#     genre = models.ManyToManyField(Genre, help_text='Select a genre for this book')

#     def __str__(self):
#         """String for representing the Model object."""
#         return self.title

#     def get_absolute_url(self):
#         """Returns the url to access a detail record for this book."""
#         return reverse('book-detail', args=[str(self.id)])