from django.urls import path 
from . import views
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)


# URL config
urlpatterns = [
  # path('', views.main),
  path('login/', views.login),
  path('signup/', views.signup)
]