from django import forms

from gamesPlay.gameApp.models import Game


class GameBaseForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = '__all__'
        labels = {
            'max_level': 'Max Level',
            'image_url': 'Image URL',
        }


class GameCreateForm(GameBaseForm):
    pass


class GameEditForm(GameBaseForm):
    pass


class GameDeleteForm(GameBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.disabled = True
