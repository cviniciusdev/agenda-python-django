from django.shortcuts import render
from contact.models import Contact
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    contacts = Contact.objects \
        .filter(show=True) \
        .order_by('-id')
    
    paginator = Paginator(contacts, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'site_title': 'Contatos - '
    }
    
    return render(
        request,
        'contact/index.html',
        context,
    )

# Create your views here.
def contato(request, contact_id):
    single_contact = Contact.objects.get(pk=contact_id, show=True)

    site_title = f'{single_contact.first_name} {single_contact.last_name} - '
    print(site_title)

    context = {
        'contact': single_contact,
        'site_title': site_title,
    }
    return render(
        request,
        'contact/contato.html',
        context,
    )


def search(request):
    search_value = request.GET.get('q', '').strip()

    if search_value == '':
        return redirect('contact:index')
    
    contacts = Contact.objects \
        .filter(show=True) \
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

    
    site_title = 'Search'

    context = {
        'page_obj': page_obj,
        'site_title': site_title,
    }
    return render(
        request,
        'contact/index.html',
        context,
    )