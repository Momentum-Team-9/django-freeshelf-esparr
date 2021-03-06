# Generated by Django 3.2.6 on 2021-08-19 12:17

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0009_auto_20210819_1127'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='author',
        ),
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='year_published',
            field=models.CharField(blank=True, max_length=4, null=True, validators=[django.core.validators.RegexValidator(message="Published year must be entered in the format: 'XXXX'.", regex='^\\d{4}$')]),
        ),
        migrations.DeleteModel(
            name='Author',
        ),
    ]
