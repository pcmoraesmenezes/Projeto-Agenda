from django.shortcuts import render, get_object_or_404, redirect
from contact.models import Contact
from django.db.models import Q
from django.core.paginator import Paginator
# from django.http import Http404
# Create your views here.


def index(request):
    contacts = Contact.objects \
        .filter(show=True)\
        .order_by('-id')

    paginator = Paginator(contacts, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    # print(contacts.query)

    context = {
        'page_obj': page_obj,
        'site_tittle': 'Contatos - '
    }

    return render(
        request,
        'contact/index.html',
        context
    )


def contact(request, contact_id):
    single_contact = get_object_or_404(
        Contact, pk=contact_id, show=True
        )
    # single_contact = Contact.objects.filter(pk=contact_id).first()
    # if single_contact is None:
    #     raise Http404()
    # print(contacts.query)

    site_tittle = f'{single_contact.first_name} {single_contact.last_name} - '

    context = {
        'contact': single_contact,
        'site_tittle': site_tittle
    }

    return render(
        request,
        'contact/contact.html',
        context
    )


def search(request):
    search_value = request.GET.get('q', '').strip()
    if search_value == '':
        return redirect('contact:index')

    contacts = Contact.objects \
        .filter(show=True)\
        .filter(
            Q(first_name__icontains=search_value) |
            Q(last_name__icontains=search_value) |
            Q(phone__icontains=search_value) |
            Q(email__icontains=search_value)
        )\
        .order_by('-id')
    paginator = Paginator(contacts, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    # print(contacts.query)

    context = {
        'page_obj': page_obj,
        'site_tittle': 'Search - ',
        'search_value': search_value,
    }

    return render(
        request,
        'contact/index.html',
        context
    )
