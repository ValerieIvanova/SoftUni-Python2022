from django.shortcuts import render, redirect

from notes.noteApp.forms import ProfileCreateForm, NoteCreateForm, NoteEditForm, NoteDeleteForm
from notes.noteApp.models import ProfileModel, NoteModel


# Create your views here.
def index(request):
    profile = ProfileModel.objects.first()
    if not profile:
        form = ProfileCreateForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect("index")

        context = {
            "form": form
        }
        return render(request, "home-no-profile.html", context)

    else:
        notes = NoteModel.objects.all()
        context = {
            "notes": notes.order_by('pk')
        }
        return render(request, "home-with-profile.html", context)


def add_note(request):
    form = NoteCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("index")
    context = {
        "form": form
    }

    return render(request, "note-create.html", context)


def edit_note(request, pk):
    note = NoteModel.objects.get(pk=pk)
    form = NoteEditForm(request.POST or None, instance=note)
    if form.is_valid():
        form.save()
        return redirect("index")

    context = {
        "form": form,
        "note": note
    }
    return render(request, "note-edit.html", context)


def delete_note(request, pk):
    note = NoteModel.objects.get(pk=pk)
    form = NoteDeleteForm(request.POST or None, instance=note)
    if form.is_valid():
        note.delete()
        return redirect("index")

    context = {
        "form": form,
        "note": note
    }
    return render(request, "note-delete.html", context)


def details_note(request, pk):
    note = NoteModel.objects.get(pk=pk)
    context = {
        "note": note
    }
    return render(request, "note-details.html", context)


def profile(request):
    notes = NoteModel.objects.all()
    context = {
        "notes": notes.count()
    }
    return render(request, "profile.html", context)


def delete_profile(request):
    profile_to_delete = ProfileModel.objects.first()
    notes = NoteModel.objects.all()
    profile_to_delete.delete()
    notes.delete()
    return redirect("index")