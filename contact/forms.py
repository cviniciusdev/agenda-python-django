from typing import Any, Dict
from django import forms
from django.core.exceptions import ValidationError
from contact.models import Contact
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(
        required=True,
        min_length=3,
        # error_messages={
        #     'required': 'Erro do RegisterForms em Forms'
        # }
    )
    last_name = forms.CharField(
        required=True,
        min_length=3,
    )
    email = forms.EmailField()

    class Meta:
        model = User
        fields = (
            'first_name', 'last_name', 'email', 'username', 'password1', 'password2',
        )

    def clean_email(self):
        email = self.cleaned_data.get('email')

        if User.objects.filter(email=email).exists():
            self.add_error(
                'email',
                ValidationError('O e-mail informado já existe', code='invalid')
            )

class ContactForm(forms.ModelForm):
    
    picture = forms.ImageField(
        widget=forms.FileInput(
            attrs={
                'accept': 'image/*'
            }
        )
    )

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)

    #     self.fields['first_name'].widget.attrs.update({
    #         'class': 'classe-a classe-b',
    #         'placeholder': 'Informe um nome INIT',
    #     })

    # first_name = forms.CharField(
    #     widget=forms.TextInput(
    #         attrs={
    #             'class': 'classe-a classe-b',
    #             'placeholder': 'Nome',
    #         }
    #     ),
    #     label='Primeiro nome',
    #     help_text='Texto de ajuda para seu usuário',
    # )

    class Meta:
        model = Contact
        fields = (
            'picture', 'first_name', 'last_name', 'phone',
            'email', 'description', 'category', 
        )

        # widgets = {
        #     'first_name': forms.TextInput(
        #         attrs={
        #             'class': 'classe-a classe-b',
        #             'placeholder': 'Informe um nome',
        #         }
        #     )
        # }



    def clean(self):
        cleaned_data = self.cleaned_data
        first_name = self.cleaned_data.get('first_name')
        last_name = self.cleaned_data.get('last_name')

        if first_name == last_name:
            msg = ValidationError(
                'Primeiro nome não pode ser igual ao segundo nome',
                code='invalid'
            )

            self.add_error('first_name', msg)
            self.add_error('last_name', msg)
            
            # MENSAGEM EM UM CAMPO = self.add_error(
            #     'first_name',
            #     ValidationError(
            #         'Primeiro nome não pode ser igual ao segundo nome',
            #         code='invalid'
            #     )
            # )

        # self.add_error(
        #     'first_name',
        #     ValidationError(
        #         'Mensagem de erro',
        #         code='invalid'
        #     )
        # )
        # self.add_error(
        #     'first_name',
        #     ValidationError(
        #         'Mensagem de erro 2',
        #         code='invalid'
        #     )
        # )

        return super().clean()
    
    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        if first_name == 'ABC':
            self.add_error(
                'first_name',
                ValidationError(
                    'Veio do add_error',
                    code='invalid'
                )
            )
        return first_name