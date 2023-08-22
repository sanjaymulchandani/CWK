# Generated by Django 4.1.1 on 2023-07-13 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page_handling', '0017_alter_review_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdBanner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='uploads/')),
                ('small_title', models.TextField()),
                ('main_title', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ClienteleImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_1', models.ImageField(blank=True, upload_to='uploads/')),
                ('image_2', models.ImageField(blank=True, upload_to='uploads/')),
                ('image_3', models.ImageField(blank=True, upload_to='uploads/')),
                ('image_4', models.ImageField(blank=True, upload_to='uploads/')),
                ('image_5', models.ImageField(blank=True, upload_to='uploads/')),
                ('image_6', models.ImageField(blank=True, upload_to='uploads/')),
                ('image_7', models.ImageField(blank=True, upload_to='uploads/')),
                ('image_8', models.ImageField(blank=True, upload_to='uploads/')),
                ('image_9', models.ImageField(blank=True, upload_to='uploads/')),
                ('image_10', models.ImageField(blank=True, upload_to='uploads/')),
            ],
        ),
        migrations.CreateModel(
            name='PromoBanner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('image', models.ImageField(upload_to='uploads/')),
            ],
        ),
        migrations.CreateModel(
            name='Social',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facebook', models.TextField()),
                ('twitter', models.TextField()),
                ('instagram', models.TextField()),
                ('threads', models.TextField()),
                ('linkedin', models.TextField()),
            ],
        ),
    ]