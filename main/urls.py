<<<<<<< HEAD
<<<<<<< HEAD
=======
"""
URL configuration for main project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))

"""

>>>>>>> 37c8de4e6d889e676bff40b3af33b47307371d3d
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render
from debug_toolbar.toolbar import debug_toolbar_urls


def home(request):
    x = 7+3
    y = 0+8
    result = x*y
    return render(request, "home.html", {"result" : result})

=======

from django.contrib import admin
from django.urls import path
from debug_toolbar.toolbar import debug_toolbar_urls
>>>>>>> developer

urlpatterns = [
<<<<<<< HEAD
    path('admin/', admin.site.urls),
<<<<<<< HEAD
    path('', home),
    path("core/", include("core.urls"))
] + debug_toolbar_urls()
=======
    path("admin/", admin.site.urls),
]
>>>>>>> 37c8de4e6d889e676bff40b3af33b47307371d3d
=======
] + debug_toolbar_urls()  # Include debug toolbar URLs
>>>>>>> developer
