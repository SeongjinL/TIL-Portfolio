from django.urls import path
from django.urls.conf import include
# view와 연결
from . import views

urlpatterns = [
  path('login/', views.login),
]
