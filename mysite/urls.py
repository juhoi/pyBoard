from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse


def index(request):
    return HttpResponse('Hello, pyBoard~!')


urlpatterns = [
    path('admin/', admin.site.urls),
    #juhoi.kim
    path('', index),
    path('board/', include('board.urls')),
]
