from django.core.exceptions import ValidationError


def rating_validator(value):
    if not 0.1 <= value <= 5.0:
        raise ValidationError('Rating must be between 0.1 and 5.0.')
