from django import forms

from my_plant_app.plant_app.models import Plant


class PlantBaseForm(forms.ModelForm):
    class Meta:
        model = Plant
        fields = '__all__'
        labels = {
            'plant_type': 'Type',
            'image_url': 'Image URL',
        }


class PlantCreateForm(PlantBaseForm):
    pass


class PlantEditForm(PlantBaseForm):
    pass


class PlantDeleteForm(PlantBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.disabled = True
