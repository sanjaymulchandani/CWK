from django.urls import path
from userauth.views import login_request, register_request

urlpatterns = [
		path('login/', login_request, name ='login_request'),
		path('register/', register_request, name ='register_request'),

]
