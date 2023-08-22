# Generated by Django 4.2.2 on 2023-07-01 14:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('page_handling', '0004_rename_trendingworkshop_allworkshop_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('photo', models.ImageField(upload_to='uploads/')),
                ('designation', models.TextField(max_length=500)),
            ],
        ),
        migrations.RemoveField(
            model_name='allworkshop',
            name='author_name',
        ),
        migrations.RemoveField(
            model_name='allworkshop',
            name='author_photo',
        ),
        migrations.AddField(
            model_name='allworkshop',
            name='trending',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='allworkshop',
            name='author',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='page_handling.author'),
        ),
    ]
