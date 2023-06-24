from django import forms

from fruitipedia.fruitApp.models import Fruit


class FruitCreateForm(forms.ModelForm):
    class Meta:
        model = Fruit
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Fruit Name'}),
            'image_url': forms.URLInput(attrs={'placeholder': 'Fruit Image URL'}),
            'description': forms.Textarea(attrs={'placeholder': 'Fruit Description'}),
            'nutrition': forms.Textarea(attrs={'placeholder': 'Nutrition Info'}),
        }

        labels = {f'{field}': "" for field in widgets}


class FruitEditForm(forms.ModelForm):
    class Meta:
        model = Fruit
        fields = '__all__'


class FruitDeleteForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.disabled = True

    class Meta:
        model = Fruit
        fields = [
            'name',
            'image_url',
            'description',
        ]
