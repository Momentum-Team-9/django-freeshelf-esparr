from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator


class User(AbstractUser):
    def __repr__(self):
        return f"<User username={self.username}>"

    def __str__(self):
        return self.username

class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=75)

    class Meta:
        verbose_name_plural = "categories"

    def __repr__(self):
        return f"<Category name={self.name}>"
    
    def __str__(self):
        return self.name
class Book(models.Model):
    year_regex = RegexValidator(
        regex=r'^\d{4}$',
        message="Published year must be entered in the format: 'XXXX'.")
    title = models.CharField(max_length=255, null=True, blank=True)
    author = models.CharField(max_length=255, null=True, blank=True)
    publisher = models.CharField(max_length=255, null=True, blank=True)
    year_published = models.CharField(max_length=4,
                            validators=[year_regex],
                            null=True,
                            blank=True)
    description = models.TextField(null=True, blank=True)
    url = models.URLField(null=True, blank=True)
    image_url = models.URLField(null=True, blank=True)
    categories = models.ManyToManyField(Category, related_name="book")
    created_at = models.DateTimeField(auto_now_add=True)
    favorited_by = models.ManyToManyField(User, related_name="fav_books", null=True, blank=True)

    def __repr__(self):
        return f"<Book title={self.title}>"
    
    def __str__(self):
        return f"{self.title}, {self.author}, {self.year_published}"
    


