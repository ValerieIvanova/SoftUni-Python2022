from django import forms

from notes.noteApp.models import ProfileModel, NoteModel


class ProfileCreateForm(forms.ModelForm):
    class Meta:
        model = ProfileModel
        fields = '__all__'


class NoteBaseForm(forms.ModelForm):
    class Meta:
        model = NoteModel
        fields = '__all__'


class NoteCreateForm(NoteBaseForm):
    pass


class NoteEditForm(NoteBaseForm):
    pass


class NoteDeleteForm(NoteBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.disabled = True
