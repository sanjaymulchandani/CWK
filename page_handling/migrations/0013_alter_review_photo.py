# Generated by Django 4.2.2 on 2023-07-10 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page_handling', '0012_alter_review_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/'),
        ),
    ]
