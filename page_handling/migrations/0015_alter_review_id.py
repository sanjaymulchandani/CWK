# Generated by Django 4.2.2 on 2023-07-10 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page_handling', '0014_alter_review_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]