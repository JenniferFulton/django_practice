# Generated by Django 2.2 on 2021-12-19 21:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books_authors_app', '0003_author_notes'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='desc',
            new_name='description',
        ),
    ]