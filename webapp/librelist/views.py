# Create your views here.
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render_to_response
from librelist.models import Domain, MailingList, Subscription


def list_domains(request):
    domains = Domain.objects.all()
    return render_to_response("domains/list.html", {"domains": domains})


def list_lists(request, domain):
    lists = MailingList.objects.filter(domain__name=domain).all()
    return render_to_response("lists/list_for_domain.html",
            {"domain_name": domain,
             "lists": lists,
            })


def list_my_subscriptions(request):
    subscriptions = Subscription.objects.filter(user=request.user)
    return render_to_response("lists/list_my_subscriptions.html",
            {"subscriptions": subscriptions,
            })

