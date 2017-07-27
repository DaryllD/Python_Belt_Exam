from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^create$', views.create, name="create"),
    url(r'^wishlist$', views.wishlist, name="dashboard"),
    url(r'^register$', views.register, name="register"),
    url(r'^login$', views.login, name="login"),
    url(r'^$', views.index, name="main"),
        ]
