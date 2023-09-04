from django import forms
from django.core.exceptions import ValidationError
from . import models


class ContactForm(forms.ModelForm):
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'classe-a classe-b',
                'placeholder': 'Escreva aqui',
            }
        ),
        label="Primeiro Nome",
        help_text="Texto de ajuda para o usuario"
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = models.Contact
        fields = (
            'first_name', 'last_name', 'phone',
            'email', 'description', 'category'
        )

    def clean(self):
        cleaned_data = self.cleaned_data
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')

        if first_name == last_name:
            self.add_error(
                'first_name', ValidationError(
                    'Primeiro nome não pode ser igual ao segundo',
                    code='invalid'
                )

            )
        # self.add_error(
        #     None,
        #     ValidationError(
        #         'Mensagem de erro',
        #         code='invalid'
        #     )

        # )
        return super().clean()

    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')

        return first_name
