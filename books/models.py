from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db.models.fields import DateTimeField


class User(AbstractUser):
    def __repr__(self):
        return f"<User username={self.username}>"

    def __str__(self):
        return self.username

class Books(models.Model):
    year_regex = RegexValidator(
        regex=r'^\d{4}$',
        message="Album year must be entered in the format: 'XXXX'.")
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
    created_at = models.DateTimeField(auto_now_add=True)
