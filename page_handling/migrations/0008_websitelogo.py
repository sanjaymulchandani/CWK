# Generated by Django 4.2.2 on 2023-07-01 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page_handling', '0007_workshopregistration_city_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='websiteLogo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_logo', models.ImageField(upload_to='uploads/')),
                ('secondary_logo', models.ImageField(upload_to='uploads/')),
                ('backup_logo', models.ImageField(upload_to='uploads/')),
            ],
        ),
    ]
