# Generated by Django 4.2.2 on 2023-07-01 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page_handling', '0006_workshopregistration'),
    ]

    operations = [
        migrations.AddField(
            model_name='workshopregistration',
            name='city',
            field=models.CharField(default=None, max_length=200),
        ),
        migrations.AddField(
            model_name='workshopregistration',
            name='date_of_birth',
            field=models.DateField(default=None),
        ),
        migrations.AddField(
            model_name='workshopregistration',
            name='gender',
            field=models.CharField(choices=[('Female', 'Female'), ('Male', 'Male'), ('Other', 'Other')], default='Select', max_length=10),
        ),
        migrations.AddField(
            model_name='workshopregistration',
            name='mobile_number',
            field=models.CharField(default=None, max_length=15),
        ),
    ]
