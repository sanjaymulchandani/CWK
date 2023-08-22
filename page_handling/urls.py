from django.urls import path
from page_handling.views import *
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings

urlpatterns = [
    path('', home_view, name='home_view'),
    path('about/', about_view, name='about_view'),
    path('contact/', contact_view, name='contact_view'),
    # path('business/', business_view, name='business_view'),
    path('blogs/', blog_view, name='blog_view'),
    # path('blogs/create/', create_blog, name='create_blog'),
    path('all-workshop/', all_workshop, name='all_workshop'),
    path('workshop/<int:workshop_id>/', workshop_detail, name='workshop_detail'),
    path('create-workshop/', create_workshop, name='create_workshop'),
    path('workshop/<int:workshop_id>/register/', register_workshop, name='register_workshop'),
    path('search/', search_workshops, name='search_workshops'),
    # path('add_review/', submit_review, name='submit_review'),
    # path('category/<int:category_id>/', category_detail_view, name='category_detail'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
