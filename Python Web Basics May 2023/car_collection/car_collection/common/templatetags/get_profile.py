from django import template
from car_collection.car_profile.models import Profile

register = template.Library()


@register.simple_tag
def get_user_profile():
    return Profile.objects.first()