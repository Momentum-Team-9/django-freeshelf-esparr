from django.contrib import admin
from .models import Book, Category, User, Author

# Register your models here.
admin.site.register(Book)
admin.site.register(Category)
admin.site.register(User)
admin.site.register(Author)

