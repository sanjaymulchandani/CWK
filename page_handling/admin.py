from django.contrib import admin
from .models import *
from .views import export_to_excel

# Register your models here.

export_to_excel.short_description = "Export to Excel"


@admin.register(WorkshopRegistration)
class WorkshopRegistrationAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'mobile_number', 'gender', 'date_of_birth', 'city', 'workshop']
    actions = [export_to_excel]
@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['name', 'content', 'display']
    list_editable = ['display']

admin.site.register([Logo, heroBanner, PromoBanner, ClienteleImage, AdBanner,
                     Author, workshopCategory, allWorkshop, About, Social, Blog, ContactContent])
