# Generated by Django 4.2.2 on 2023-07-01 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page_handling', '0002_trendingworkshop_author_name_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='trendingworkshop',
            old_name='price',
            new_name='new_price',
        ),
        migrations.AddField(
            model_name='trendingworkshop',
            name='old_price',
            field=models.CharField(default=None, max_length=20),
        ),
    ]