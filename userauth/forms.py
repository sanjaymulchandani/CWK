from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

gender_choices = [
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Other', 'Other'),
]

language_choices = [
    ('Hindi', 'Hindi'),
    ('English', 'English'),
]


class RegisterUserForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.TextInput(
                              attrs={'class': "form-control border-0 bg-light rounded-end ps-1", 'placeholder':'Email address'}))

    first_name = forms.CharField(max_length=50, required=True, widget=forms.TextInput(
                              attrs={'class': "form-control border-0 bg-light rounded-end ps-1", 'placeholder':'First Name', 'autofocus':'autofocus'}))

    last_name = forms.CharField(max_length=50, required=True, widget=forms.TextInput(
                              attrs={'class': "form-control border-0 bg-light rounded-end ps-1", 'placeholder':'Last Name'}))

    date_of_birth = forms.DateField(required=True, widget=forms.SelectDateWidget(years=range(1980, 2024),
                                                                                 attrs={'class': "form-select border-0 bg-light rounded-end ps-1"}))

    gender = forms.CharField(widget=forms.Select(choices=gender_choices,
                                                 attrs={'class': "form-select border-0 bg-light rounded-end ps-1"}))

    mobile_number = forms.CharField(max_length=12, required=True, widget=forms.TextInput(
                              attrs={'class': "form-control border-0 bg-light rounded-end ps-1", 'placeholder':'Mobile number'}))

    language_of_choice = forms.CharField(widget=forms.Select(choices=language_choices,
                                                             attrs={'class': "form-select border-0 bg-light rounded-end ps-1"}))

    address = forms.CharField(widget=forms.Textarea(
        attrs={'class': "form-control", 'placeholder':'Address', 'rows':2, 'cols':15}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update(
            {'class': 'form-control border-0 bg-light rounded-end ps-1', 'placeholder': 'Create a username'})
        self.fields['password1'].widget.attrs.update(
            {'class': 'form-control border-0 bg-light rounded-end ps-1', 'placeholder': 'Enter your password'})
        self.fields['password2'].widget.attrs.update(
            {'class': 'form-control border-0 bg-light rounded-end ps-1', 'placeholder': 'Re-enter your password'})
        self.fields['address'].widget.attrs.update(
            {'class': 'form-control border-0 bg-light rounded-end ps-1', 'placeholder': 'Address'})
        self.fields['address'].widget.attrs.update(
            {'class': 'form-control border-0 bg-light rounded-end ps-1', 'placeholder': 'Address'})

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email','language_of_choice', 'gender', 'mobile_number','address', 'date_of_birth', 'password1', 'password2')