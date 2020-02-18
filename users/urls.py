# from django.conf.urls import url
from django.urls import path

from users.views.login_view import sign_in
from users.views.logout_view import sign_out

app_name = 'users'

urlpatterns = [
    path('', sign_in, name="login"),
    path('logout/', sign_out, name="logout"),
]
