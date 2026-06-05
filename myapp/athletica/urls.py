from django.urls import path
from .views import LandingPageView

app_name = 'athletica_ai'

urlpatterns = [
    path('', LandingPageView.as_view(), name='landing'),
]