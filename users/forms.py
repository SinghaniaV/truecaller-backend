from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.validators import RegexValidator


class UserRegisterForm(UserCreationForm):
    """Form for Registration."""

    email = forms.EmailField(required=False)  # Make email optional
    first_name = forms.CharField(max_length=64)
    last_name = forms.CharField(max_length=64)

    # Add phone field with validation and use it as a username for uniqueness.
    phone_regex = RegexValidator(
        regex=r'^\d{10}$',
        message="Phone number must be 10 digits."
    )
    username = forms.CharField(
        validators=[phone_regex],
        max_length=10,
        required=True,
        help_text="Enter a 10-digit phone number which is used as a username."
    )

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        user.phone = self.cleaned_data["phone"]
        if commit:
            user.save()
        return user

    
    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if User.objects.filter(userprofile__phone=phone).exists():
            raise forms.ValidationError("This phone number is already in use.")
        return phone

class AddToGlobalForm(forms.Form):
    """Form for adding users to global Db."""

    first_name = forms.CharField(max_length=64)
    last_name = forms.CharField(max_length=64)
    email = forms.EmailField(required=False)

    phone_regex = RegexValidator(
        regex=r'^\d{10}$',
        message="Phone number must be 10 digits."
    )
    phone = forms.CharField(
        validators=[phone_regex],
        max_length=10,
        required=True,
        help_text="Enter a 10-digit phone number you want to save."
    )
    mark_spam = forms.BooleanField(required=False, initial=False)


class SearchForm(forms.Form):
    """Form for searching users."""

    first_name = forms.CharField(required=False, label='First Name')
    last_name = forms.CharField(required=False, label='Last Name')
    phone = forms.CharField(required=False, label='Phone')
