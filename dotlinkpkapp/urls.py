from django.urls import path
from . import views

urlpatterns = [
    path('', views.dot_link_pk, name='dotlink_pk'),
]
