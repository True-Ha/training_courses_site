from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin

from django.shortcuts import render, redirect


from django.views.generic import DetailView, ListView, UpdateView

from .permissions import PaymentPermissionsMixin

from .models import Training


class TabataPageView(ListView):
    model = Training
    template_name = 'app/train_list.html'
    context_object_name = 'train_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['train_list'] = Training.objects.all().order_by('id')
        return context



def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


class TrainingsDaysView(PaymentPermissionsMixin, DetailView):
    model = Training
    template_name = 'app/train_detail.html'
    context_object_name = "train"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        days_week = self.kwargs['slug']
        days_week = days_week[0]
        context['header_week'] = Training.objects.filter(name__contains='mon').order_by('id')
        context['day_list'] = Training.objects.filter(name__contains=days_week)
        return context


