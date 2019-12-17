from django import forms
from django.core.exceptions import ValidationError

from eventex.subscriptions.models import Subscription


class SubscriptionForm(forms.ModelForm):
    def clean_name(self):
        name = self.cleaned_data['name']
        words = (word.capitalize() for word in name.split())
        return ' '.join(words)

    def clean(self):
        super(SubscriptionForm, self).clean()
        if (
                not self.cleaned_data.get('email') and
                not self.cleaned_data.get('phone')
        ):
            raise ValidationError('Informe seu e-mail ou telefone.')
        return self.cleaned_data

    class Meta:
        model = Subscription
        fields = [
            'name',
            'cpf',
            'email',
            'phone',
        ]
