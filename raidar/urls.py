from django.conf.urls import url

from . import views

urlpatterns = [
        url(r'user', views.user, name = "user"),
        url(r'login', views.login, name = "login"),
        url(r'logout', views.logout, name = "logout"),
        url(r'register', views.register, name = "register"),
        url(r'upload', views.upload, name = "upload"),
        url(r'^$', views.index, name = "index"),
]