from .models import allWorkshop, workshopCategory, Logo

def workshop_titles(request):
    categories = workshopCategory.objects.all()
    workshops = allWorkshop.objects.all()
    return {'workshop_titles': workshops, 'categories': categories}

def logo_main(request):
    website_logo = Logo.objects.all()
    return {'website_logo': website_logo}