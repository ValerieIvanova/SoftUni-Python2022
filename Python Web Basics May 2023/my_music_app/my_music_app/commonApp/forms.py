from django import forms

from my_music_app.profileApp.models import Profile


class ProfileCreateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = (
            'username',
            'email',
            'age',
        )
