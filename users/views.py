from django.shortcuts import render, redirect
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.contrib.auth import login
from django.views import View

from django.views.generic import DetailView

from .models import MyUser
from .forms import UserUpdateForm


class UserView(DetailView):
    model = MyUser
    template_name = 'users/profile_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


def update_user(request):
    if request.user.is_authenticated:
        current_user = MyUser.objects.get(id=request.user.id)
        form = UserUpdateForm(request.POST or None, instance=current_user)
        if form.is_valid():
            form.save()
            login(request, current_user)
            messages.success(request, ("Профиль обновлён"))
            return redirect('home')
        return render(request, 'users/user-upgrade.html', {'form': form})
    else:
        messages.success(request, ("You must be logged"))
        return redirect('home')


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('home')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'users/change_password.html', {
        'form': form
    })