from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render

from users.forms.login_form import LoginForm


def sign_in(request):

    if request.method == "POST":
        form = LoginForm(request.POST)

        if form.is_valid():

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            if username is not None and len(username) >= 4:

                # authenticate the user. If the user object is not None,
                # it means the user exists in the system. Then if the password
                # check passes, the user is logged in and redirected to their
                # dashboard.
                user = authenticate(username=username, password=password)
                if user is not None:
                    user.check_password(password)
                    login(request, user)

                    messages.success(request, "You've been successfully logged in! ")
                    return redirect('invoice:index')
                else:
                    messages.warning(request, "Username and/or password does not exist")
        else:
            messages.warning(request, "Username and/or password contains invalid data")
    else:
        if request.user.is_authenticated:
            return redirect('invoice:index')

        # For a GET request, create a login form ad pass it
        # to the login page for rendering.
        form = LoginForm()

    # render the login page along with the form
    return render(request, "users/login.html", {'login_form': form, 'title': 'Sign In'})
