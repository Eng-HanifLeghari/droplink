from django.urls import path
from . import views

urlpatterns = [
    path('dotlink/', views.dot_link_pk, name='dotlink_pk'),
]