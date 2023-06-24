from django import forms

from fruitipedia.profileApp.models import Profile


class ProfileBaseForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = "__all__"


class ProfileCreateForm(ProfileBaseForm):
    class Meta:
        model = Profile
        fields = [
            "first_name",
            "last_name",
            "email",
            "password"
        ]
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last Name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
            'password': forms.PasswordInput(attrs={'placeholder': 'Password'})
        }

        labels = {f'{field}': "" for field in fields}


class ProfileEditForm(ProfileBaseForm):
    class Meta:
        model = Profile
        exclude = [
            'password',
            'email'
        ]
