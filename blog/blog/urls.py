"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from django.conf import settings

from post.views import index as post_index, register, add_post
from profiles.views import index as profiles_index
from notes.views import index2
from shop.views import products_view, product_details_view, iphone1

urlpatterns = [
    path('admin/', admin.site.urls),
    path('post/', post_index, name='post_index'),
    path('profiles/', profiles_index, name='profiles_index'),
    path('notes/', index2),
    path('register/', register, name='register'),
    # add new url for templates add_post.html
    path('add_post/', add_post, name='add_post'),
    path("api/", include("api.urls", namespace="api")),
    path("api/auth", include("rest_framework.urls", namespace="rest_framework")),
    path('', products_view, name='products_view,'),
    path('iphone1/', iphone1, name='ipone'),
    path(
        "product/<int:product_id>/", product_details_view, name="product_details_view"
    ),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    # Server static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)