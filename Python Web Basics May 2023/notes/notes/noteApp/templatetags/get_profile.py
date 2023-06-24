from django import template

from notes.noteApp.models import ProfileModel

register = template.Library()


@register.simple_tag
def get_user_profile():
    return ProfileModel.objects.first()
