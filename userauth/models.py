from django.db import models

# Create your models here.

class registerContent(models.Model):
    main_title = models.TextField()
    secondary_title = models.TextField()
    student_stats = models.CharField(max_length=200)
    main_image = models.ImageField()
    avatar_img_1 = models.ImageField()
    avatar_img_2 = models.ImageField()
    avatar_img_3 = models.ImageField()
    avatar_img_4 = models.ImageField()

class loginContent(models.Model):
    main_title = models.TextField()
    secondary_title = models.TextField()
    student_stats = models.CharField(max_length=200)
    main_image = models.ImageField()
    avatar_img_1 = models.ImageField()
    avatar_img_2 = models.ImageField()
    avatar_img_3 = models.ImageField()
    avatar_img_4 = models.ImageField()
