from django.urls import path, include
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from .views import SignUpView
from django.views.generic import TemplateView


urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/profile/', TemplateView.as_view(template_name='accounts/profile.html'), name='profile'),
    path("signup/", SignUpView.as_view(), name="templates/registration/signup"),
]
