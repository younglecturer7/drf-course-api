from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render
from debug_toolbar.toolbar import debug_toolbar_urls


def home(request):
    x = 7+3
    y = 0+8
    result = x*y
    return render(request, "home.html", {"result" : result})


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path("core/", include("core.urls"))
] + debug_toolbar_urls()
