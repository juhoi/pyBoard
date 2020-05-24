from django.http import HttpResponse
from django.urls import path
from django.contrib.auth import views as auth_views

from . import views


def index(request):
    return HttpResponse('Hello, pyBoard~!')


app_name = 'common'

urlpatterns = [
    path('', index),
    path('login/', auth_views.LoginView.as_view(template_name='common/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.signup, name='signup'),
]
