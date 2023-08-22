from django.db import models
import uuid

# Create your models here.

class Logo(models.Model):
    logo_light = models.ImageField(upload_to='uploads/')
    logo_dark = models.ImageField(upload_to='uploads/')

class heroBanner(models.Model):
    banner_title = models.TextField(max_length=100)
    banner_description = models.TextField(max_length=500)
    banner_image = models.ImageField(upload_to='uploads/')
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.banner_title

class PromoBanner(models.Model):
    title = models.TextField()
    image = models.ImageField(upload_to='uploads/')

    def __str__(self):
        return self.title

class ClienteleImage(models.Model):
    image_1 = models.ImageField(upload_to='uploads/', blank=True)
    image_2 = models.ImageField(upload_to='uploads/', blank=True)
    image_3 = models.ImageField(upload_to='uploads/', blank=True)
    image_4 = models.ImageField(upload_to='uploads/', blank=True)
    image_5 = models.ImageField(upload_to='uploads/', blank=True)
    image_6 = models.ImageField(upload_to='uploads/', blank=True)
    image_7 = models.ImageField(upload_to='uploads/', blank=True)
    image_8 = models.ImageField(upload_to='uploads/', blank=True)
    image_9 = models.ImageField(upload_to='uploads/', blank=True)
    image_10 = models.ImageField(upload_to='uploads/', blank=True)

class AdBanner(models.Model):
    image = models.ImageField(upload_to='uploads/', blank=True)
    small_title= models.TextField()
    main_title = models.TextField()

class Author(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='uploads/')
    designation = models.TextField(max_length=500)

    def __str__(self):
        return self.name

class workshopCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class allWorkshop(models.Model):
    title = models.TextField(max_length=100)
    description = models.TextField(max_length=500)
    old_price = models.CharField(max_length=20, default=None)
    new_price = models.CharField(max_length=20)
    duration = models.CharField(max_length=10)
    image = models.ImageField(upload_to='uploads/')
    date_created = models.DateTimeField(auto_now_add=True)
    trending = models.BooleanField(default=False)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, default=None)
    category = models.ForeignKey(workshopCategory, on_delete=models.CASCADE, null=False, blank=False)

    def __str__(self):
        return self.title

class WorkshopRegistration(models.Model):
    workshop = models.ForeignKey(allWorkshop, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    mobile_number = models.CharField(max_length=15, default=None)
    gender = models.CharField(choices=(("Female", "Female"),
                                       ("Male", "Male"),
                                       ("Other", "Other"),
                                       ), default='Select', max_length=10)
    date_of_birth = models.DateField(default=None)
    city = models.CharField(max_length=200, default=None)

class About(models.Model):
    main_title = models.TextField(max_length=500)
    our_goal = models.TextField(max_length=150)
    about_short_description = models.TextField(max_length=500)
    about_title = models.TextField(max_length=200)
    about_long_description = models.TextField(max_length=1500)
    bullet_point_1 = models.TextField(max_length=100)
    bullet_point_2 = models.TextField(max_length=100)
    bullet_point_3 = models.TextField(max_length=100)
    bullet_point_4 = models.TextField(max_length=100)
    about_image_1 = models.ImageField(upload_to='uploads/')
    about_image_2 = models.ImageField(upload_to='uploads/')
    about_image_3 = models.ImageField(upload_to='uploads/')
    about_image_4 = models.ImageField(upload_to='uploads/')
    author_image = models.ImageField(upload_to='uploads/')


class Review(models.Model):
    name = models.CharField(max_length=100)
    content = models.TextField(max_length=500)
    photo = models.ImageField(upload_to='uploads/', null=False, blank=False)
    display = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Social(models.Model):
    facebook = models.TextField()
    twitter = models.TextField()
    instagram = models.TextField()
    threads = models.TextField()
    linkedin = models.TextField()

class ContactContent(models.Model):
    address = models.TextField()
    contact_number = models.IntegerField()
    email = models.EmailField()
    image = models.ImageField(upload_to='uploads/')
    def __str__(self):
        return self.address

class ContactForm(models.Model):
    name = models.CharField(max_length=100, blank=False)
    email = models.EmailField(blank=False)
    message = models.TextField(blank=False)

class Blog(models.Model):
    title = models.CharField(max_length=100)
    summary = models.TextField(max_length=250)
    content = models.TextField()
    image = models.ImageField(upload_to='blog/images')
    user_name = models.TextField(max_length=150)
    user_photo = models.ImageField(upload_to='blog/images', blank=True)
    is_visible = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
