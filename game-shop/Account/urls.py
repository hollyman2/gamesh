from django.urls import path, include
from .views import RegistrationAPIView, LoginAPIView


urlpatterns = [
    path('default/', include('allauth.urls')),
    path('api/', RegistrationAPIView.as_view()),
    path('api/login', LoginAPIView.as_view()),
]
