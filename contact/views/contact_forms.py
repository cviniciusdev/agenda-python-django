from contact.models import Contact
from django.shortcuts import get_object_or_404, redirect, render
from django.db.models import Q
from django.core.paginator import Paginator

# Create your views here.
def create(request):

    context = {
        'site_title': 'Criar contatos - '
    }
    
    return render(
        request,
        'contact/create.html',
        context,
    )