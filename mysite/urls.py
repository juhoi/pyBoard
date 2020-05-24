from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

from board.views import base_views


urlpatterns = [
    path('admin/', admin.site.urls),
    #juhoi.kim
    path('', base_views.index, name='index'),
    path('board/', include('board.urls')),
    path('common/', include('common.urls')),
]
