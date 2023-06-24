from django.forms import forms


def capital_letter_validator(value):
    if not value[0].isupper():
        raise forms.ValidationError('Your name must start with a capital letter!')


def all_letters_validator(value):
    if not value.isalpha():
        raise forms.ValidationError('Plant name should contain only letters!')