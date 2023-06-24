from django import template
from gamesPlay.profileApp.models import Profile

register = template.Library()


@register.simple_tag
def get_user_profile():
    return Profile.objects.first()