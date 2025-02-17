from django.shortcuts import redirect, render
from contact.forms import RegisterForm, RegisterUpdateForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required

def register(request):
    form = RegisterForm()
    
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()            
            messages.success(request, 'Cadastro realizado com sucesso!')
            return redirect('contact:index')

    # Senha carlos.maria = '#Defe123'
    return render(
        request,
        'contact/register.html',
        {
            'form': form,
        }
    )

def login_view(request):
    # Senha carlos.maria = '#Defe123'
    form = AuthenticationForm(request)

    if request.method == 'POST':

        form = AuthenticationForm(request, request.POST)

        if form.is_valid():
            user = form.get_user()
            auth.login(request, user)
            messages.success(request, 'Login realizado com sucesso')
            return redirect('contact:index')
        
        messages.error(request, 'Login inválido')


    return render(
        request,
        'contact/login.html',
        {
            'form': form,
        }
    )

@login_required(login_url='contact:login')
def logout(request):
    auth.logout(request)
    return redirect('contact:login')


@login_required(login_url='contact:login')
def user_update(request):
    form = RegisterUpdateForm(instance=request.user)

    if request.method == 'POST':
        form = RegisterUpdateForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            messages.success(request, 'Cadastro realizado')

            return redirect('contact:user_update')

    

    return render(
        request,
        'contact/register.html',
        {
            'form': form,
        }
    )    