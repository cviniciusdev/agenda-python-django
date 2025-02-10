from contact.models import Contact
from django.shortcuts import render
from django.db.models import Q
from django.core.paginator import Paginator
from contact.forms import ContactForm



# Create your views here.
def create(request):
    if request.method == 'POST':
        context = {
            'site_title': 'Criar contatos - ',
            'form': ContactForm(request.POST),
        }
    
        return render(
            request,
            'contact/create.html',
            context,
        )

    context = {
        'site_title': 'Criar contatos - ',
        'form': ContactForm(),
    }
    
    return render(
        request,
        'contact/create.html',
        context,
    )