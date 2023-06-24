import http.client
from random import choice

from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect

# Create your views here.

# without render
# def show_departments(request, *args, **kwargs):
#     body = f'path: {request.path}, args={args}, kwargs={kwargs}'
#     print(request.method)
#     print(request.GET)
#     print(request.get_port())
#     print(request.get_host())
#     print(request.headers)
#     return HttpResponse(body)


def show_departments(request, *args, **kwargs):
    context = {
        'page_title': 'Departments',
        'method': request.method,
        'order_by': request.GET.get('order_by', 'name')
    }
    return render(request, 'departments/all.html', context)


def show_department_details(request, department_id):
    body = f'path: {request.path}, id: {department_id}'
    return HttpResponse(body)


def redirect_to_first_department(request):
    possible_order_by = ['name', 'age', 'id']
    order_by = choice(possible_order_by)
    # to = f"/departments/?order_by={order_by}"

    return redirect('show department details', department_id=13)


def show_not_found(request):
    status_code = 404
    # return HttpResponseNotFound('This is not found')
    # return HttpResponse('Error', status=status_code)
    # raise Http404('Not found!')
    values = []
    return HttpResponse(values[0])

