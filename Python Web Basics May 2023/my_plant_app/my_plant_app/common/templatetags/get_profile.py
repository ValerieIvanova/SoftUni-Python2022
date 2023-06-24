
from django import template
from my_plant_app.profile_app.models import Profile

register = template.Library()


@register.simple_tag
def get_user_profile():
    return Profile.objects.first()
