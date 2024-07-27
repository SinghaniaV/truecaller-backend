from django import forms
from django.core.validators import RegexValidator

class UserRegisterForm(forms.Form):
    """Form for Registration."""

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

    password = forms.CharField(widget=forms.PasswordInput())
    email = forms.EmailField(required=False)  # Make email optional
    first_name = forms.CharField(max_length=64)
    last_name = forms.CharField(max_length=64)

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
