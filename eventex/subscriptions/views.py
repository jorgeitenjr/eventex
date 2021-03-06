from django.conf import settings
from django.contrib import messages
from django.core import mail
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, resolve_url as r
from django.template.loader import render_to_string

from eventex.subscriptions.forms import SubscriptionForm
from eventex.subscriptions.models import Subscription


def create(request):
    form = SubscriptionForm(request.POST)
    if not form.is_valid():
        return render(request, 'subscriptions/subscription_form.html', {'form': form})

    subscription = form.save()

    _send_email('Confirmação de inscrição', settings.DEFAULT_FROM_EMAIL, form.cleaned_data['email'],
                'subscriptions/subscription_email.txt', form.cleaned_data)

    Subscription.objects.create(**form.cleaned_data)
    messages.success(request, 'Inscrição realizada com sucesso!')
    return HttpResponseRedirect(r('subscriptions:detail', subscription.pk))


def new(request):
    if request.method == 'POST':
        return create(request)
    return empty_form(request)


def empty_form(request):
    return render(
        request,
        'subscriptions/subscription_form.html',
        {
            'form': SubscriptionForm()
        }
    )


def detail(request, pk):
    subscription = get_object_or_404(Subscription, pk=pk)
    return render(request, 'subscriptions/subscription_detail.html', {
        'subscription': subscription
    })


def _send_email(subject, from_, to, template_name, context):
    body = render_to_string(template_name, context)
    mail.send_mail(subject, body, from_, [from_, to])
