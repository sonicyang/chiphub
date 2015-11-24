"""chiphub URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
import chatroom.views as chatroom
import digikey.views as digikey
import login.views as login
import main.views as main

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    # Misc
    url(r'^$', main.index),
    url(r'^faq/$', main.faq),
    url(r'^exchange/$', main.exchange),
    url(r'^about_us/$', main.about_us),

    # ChatRoom
    url(r'^append/$', chatroom.append),
    url(r'^retreive/$', chatroom.retreive),
    url(r'^chatroom/$', chatroom.chatroom),

    # Login
    url(r'^profile/$', login.profile),
    url(r'^update_profile/$', login.update_profile),

    url(r'^islogin/$', login.isLogin),
    url(r'^logout/$', login.logout),

    # Google OAuth
    url(r'^google_login/$', login.google_login),
    url(r'^google_callback/$', login.google_callback),

    # Digikey
    url(r'^progress/$', digikey.progress),
    url(r'^order/$', digikey.order_page),
    url(r'^order_digikey/$', digikey.order_digikey),
    url(r'^price_digikey/$', digikey.get_digikey_price),
    url(r'^rally_digikey/$', digikey.get_current_rally),
    url(r'^list_digikey/$', digikey.get_user_orders),
    url(r'^pay_digikey/$', digikey.apply_paying_info),
]
