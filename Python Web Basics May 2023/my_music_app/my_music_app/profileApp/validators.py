from django.core.exceptions import ValidationError


def alnum_underscore_validator(value):
    for char in value:
        if not (char.isalnum() or char == '_'):
            raise ValidationError(
                "Ensure this value contains only letters, numbers, and underscore."
            )