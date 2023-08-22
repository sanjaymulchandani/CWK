from django import forms
from .models import allWorkshop, Author, WorkshopRegistration, Review, ContactForm
from django.contrib.admin.widgets import AdminDateWidget
from django.forms.widgets import NumberInput
from django.forms.fields import DateField


class allWorkshopForm(forms.ModelForm):
    class Meta:
        model = allWorkshop
        fields = '__all__'

    author = forms.ModelChoiceField(queryset=Author.objects.all())


class WorkshopRegistrationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['workshop'].widget.attrs.update(
            {'class': 'form-control w-50'},
        )
        self.fields['name'].widget.attrs.update(
            {'class': 'form-control w-50', 'placeholder': 'Full name'},
        )
        self.fields['email'].widget.attrs.update(
            {'class': 'form-control w-50', 'placeholder': 'Email address'},
        )
        self.fields['mobile_number'].widget.attrs.update(
            {'class': 'form-control w-50', 'placeholder': 'Mobile number', 'type': 'number'},
        )
        self.fields['gender'].widget.attrs.update(
            {'class': 'form-control w-50'},
        )
        self.fields['date_of_birth'].widget.attrs.update(
            {'class': 'form-control w-50'},
        )
        self.fields['city'].widget.attrs.update(
            {'class': 'form-control w-50', 'placeholder': 'City'},
        )

    class Meta:
        model = WorkshopRegistration
        fields = ['workshop', 'name', 'email', 'mobile_number', 'gender', 'date_of_birth', 'city']


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = '__all__'


class ContactFormCustomized(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update(
            {'class': 'form-control form-control-lg', 'placeholder': 'Name'},
        )
        self.fields['email'].widget.attrs.update(
            {'class': 'form-control form-control-lg', 'placeholder': 'example@email.com'},
        )
        self.fields['message'].widget.attrs.update(
            {'class': 'form-control form-control-lg', 'placeholder': 'Write your message'},
        )

    class Meta:
        model = ContactForm
        fields = ['name', 'email', 'message']
