from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView
from .forms import PasswordChange




@login_required
def profile(request):
    return render(request, 'user_profile.html')


def change_password(request):
    if request.method == 'POST':
        form = PasswordChange(request, 'POST')
        if form.is_valid():
            form.save()
            messages.success(request, 'Your password was successfully updated!')
            
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChange
    return render(request, 'registration/change_password.html', {
        'form': form
    })


