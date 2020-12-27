"""HobbyHunt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from accounts.views import index, logout, login, registration, user_profile
from django.views.generic import RedirectView
from django.views.static import serve
from .settings import MEDIA_ROOT
from accounts import urls as accounts_urls
from accounts.views import index
from accounts.views import home
from hobby_product import urls as urls_hobby_product
from cart import urls as urls_cart
from home import urls as urls_home
from search import urls as urls_search
from about import urls as urls_about
from checkout import urls as urls_checkout
from summer_course import urls as urls_summer
from django.views import static
from .settings import MEDIA_ROOT


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', RedirectView.as_view(url='home/')),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),
    url(r'^$', index, name="index"),
    url(r'^accounts/', include(accounts_urls)),
    url(r'^hobby_product/', include(urls_hobby_product)),
    url(r'^cart/', include(urls_cart)),
    url(r'^checkout/', include(urls_checkout)),
    url(r'^search/', include(urls_search)),
    url(r'^about/', include(urls_about)),
    url(r'^summer/', include(urls_summer)),
    url(r'^media/(?P<path>.*)$', static.serve, {'document_root': MEDIA_ROOT}),
    url(r'^home/', include(urls_home)),
]
