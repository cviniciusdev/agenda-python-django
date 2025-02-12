from contact.models import Contact
from django.shortcuts import get_object_or_404, redirect, render
from django.db.models import Q
from django.core.paginator import Paginator
from contact.forms import ContactForm
from django.urls import reverse



# Create your views here.
def create(request):
    form_action = reverse('contact:create')
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES, request.FILES)

        context = {
            'site_title': 'Criar contatos - ',
            'form': form,
            'form_action': form_action,
        }

        if form.is_valid():
            contact = form.save()
            return redirect('contact:update', contact_id=contact.pk)
    
        return render(
            request,
            'contact/create.html',
            context,
        )

    context = {
        'site_title': 'Criar contatos - ',
        'form': ContactForm(),
        'form_action': form_action,
    }
    
    return render(
        request,
        'contact/create.html',
        context,
    )

def update(request, contact_id):
    contact = get_object_or_404(
        Contact, pk=contact_id, show=True
    )

    form_action = reverse('contact:update', args=(contact_id,))

    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES, instance=contact)

        context = {
            'site_title': 'Criar contatos - ',
            'form': form,
            'form_action': form_action,
        }

        if form.is_valid():
            contact = form.save()
            return redirect('contact:update', contact_id=contact.pk)
    
        return render(
            request,
            'contact/create.html',
            context,
        )

    context = {
        'site_title': 'Criar contatos - ',
        'form': ContactForm(instance=contact),
        'form_action': form_action,
    }
    
    return render(
        request,
        'contact/create.html',
        context,
    )


def delete(request, contact_id):
    contact = get_object_or_404(
        Contact, pk=contact_id, show=True
    )
    confirmation = request.POST.get('confirmation', 'no')
    
    print(confirmation)
    if confirmation == 'yes':
        contact.delete()
        return redirect('contact:index')

    return render(
        request,
        'contact/contato.html',
        {
            'contact': contact,
            'confirmation': confirmation,
        }
    )

    # contact.delete()