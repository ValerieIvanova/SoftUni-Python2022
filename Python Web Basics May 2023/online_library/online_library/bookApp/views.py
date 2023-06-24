from django.shortcuts import render, redirect

from online_library.bookApp.forms import BookAddForm, BookEditForm
from online_library.bookApp.models import Book
from online_library.profileApp.forms import ProfileCreateForm
from online_library.profileApp.models import Profile


# Create your views here.
def home_page(request):
    profile = Profile.objects.first()
    if not profile:
        form = ProfileCreateForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('home-page')

        context = {
            'form': form
        }
        return render(request, 'home-no-profile.html', context)

    else:
        books = Book.objects.all()
        context = {
            'books': books.order_by('pk')
        }

        return render(request, 'home-with-profile.html', context)


def add_book(request):
    form = BookAddForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home-page')
    context = {
        'form': form
    }
    return render(request, 'book/add-book.html', context)


def edit_book(request, pk):
    book = Book.objects.get(pk=pk)
    form = BookEditForm(request.POST or None, instance=book)
    if form.is_valid():
        form.save()
        return redirect('home-page')
    context = {
        'form': form,
        'book': book
    }
    return render(request, 'book/edit-book.html', context)


def delete_book(request, pk):
    book = Book.objects.get(pk=pk)
    book.delete()
    return redirect('home-page')


def details_book(request, pk):
    book = Book.objects.get(pk=pk)
    context = {
        'book': book
    }
    return render(request, 'book/book-details.html', context)
