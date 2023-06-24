from django import forms

from recipes.recipeApp.models import Recipe


class RecipeBaseForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = '__all__'


class RecipeCreateForm(RecipeBaseForm):
    pass


class RecipeEditForm(RecipeBaseForm):
    pass


class RecipeDeleteForm(RecipeBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.disabled = True

