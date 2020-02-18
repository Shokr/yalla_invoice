from django.contrib import messages
from django.contrib.auth import logout
from django.shortcuts import redirect


def sign_out(request):

    if request.user.is_authenticated:
        logout(request)
        messages.success(request, 'You have successfully logged out! Login again!')

    return redirect('users:login')
