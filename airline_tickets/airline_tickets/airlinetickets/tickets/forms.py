from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from .models import Flyes, SoldTickets

class AddFlyghtForm(forms.ModelForm):
    class Meta:
        model = Flyes
        fields = '__all__'


class SearchFlyForm(forms.Form):
    arrival = forms.CharField(required=False, max_length=100)
    departure = forms.CharField(required=False, max_length=100)
    arrival_date = forms.DateField(required=False)
    departure_date = forms.DateField(required=False)
    price = forms.FloatField(required=False)

class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form'}))
    first_name = forms.CharField(label='Имя', widget=forms.TextInput(attrs={'class': 'form'}))
    last_name = forms.CharField(label='Фамилию', widget=forms.TextInput(attrs={'class': 'form'}))
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'first_name', 'last_name')

class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form'}))



