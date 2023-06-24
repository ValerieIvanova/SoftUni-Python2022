from django import forms

from gamesPlay.profileApp.models import Profile


class ProfileBaseForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'profile_picture': 'Profile Picture'
        }


class ProfileCreateForm(ProfileBaseForm):
    class Meta:
        model = Profile
        exclude = ['first_name', 'last_name', 'profile_picture']
        widgets = {
            'password': forms.PasswordInput()
        }


class ProfileEditForm(ProfileBaseForm):
    pass


class ProfileDeleteForm(ProfileBaseForm):
    pass
