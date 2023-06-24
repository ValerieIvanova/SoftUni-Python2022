from django.shortcuts import render, redirect

from online_library.bookApp.models import Book
from online_library.profileApp.forms import ProfileEditForm, ProfileDeleteForm
from online_library.profileApp.templatetags.get_profile import get_user_profile


# Create your views here.
def profile_page(request):
    return render(request, 'profile/profile.html')


def profile_edit(request):
    form = ProfileEditForm(request.POST or None, instance=get_user_profile())
    if form.is_valid():
        form.save()
        return redirect('profile-page')

    context = {
        'form': form
    }
    return render(request, 'profile/edit-profile.html', context)


def profile_delete(request):
    profile = get_user_profile()
    form = ProfileDeleteForm(request.POST or None, instance=profile)
    if form.is_valid():
        books = Book.objects.all()
        profile.delete()
        books.delete()
        return redirect('home-page')

    context = {
        'form': form
    }
    return render(request, 'profile/delete-profile.html', context)
