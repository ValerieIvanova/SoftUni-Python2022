from django.shortcuts import render, redirect

from .forms import RecipeCreateForm, RecipeEditForm, RecipeDeleteForm
from .models import Recipe


# Create your views here.
def create_recipe(request):
    form = RecipeCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('index')

    context = {
        'form': form
    }
    return render(request, 'create.html', context)


def edit_recipe(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    form = RecipeEditForm(request.POST or None, instance=recipe)
    if form.is_valid():
        form.save()
        return redirect('index')

    context = {
        'form': form,
        'recipe': recipe
    }
    return render(request, 'edit.html', context)


def delete_recipe(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    form = RecipeDeleteForm(request.POST or None, instance=recipe)
    if form.is_valid():
        recipe.delete()
        return redirect('index')

    context = {
        'form': form,
        'recipe': recipe
    }

    return render(request, 'delete.html', context)


def details_recipe(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    ingredients = recipe.ingredients.split(',')
    context = {
        'recipe': recipe,
        'ingredients': ingredients
    }
    return render(request, 'details.html', context)


def index(request):
    all_recipes = Recipe.objects.all()
    context = {
        'all_recipes': all_recipes
    }
    return render(request, 'index.html', context)
