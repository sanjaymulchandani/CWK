# Generated by Django 4.2.2 on 2023-07-10 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page_handling', '0010_about_clientele_review'),
    ]

    operations = [
        migrations.CreateModel(
            name='Logo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo_light', models.ImageField(upload_to='uploads/')),
                ('logo_dark', models.ImageField(upload_to='uploads/')),
            ],
        ),
    ]
