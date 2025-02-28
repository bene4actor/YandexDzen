from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import RegisterView, LogOutView, AllAccountView

urlpatterns = [
    path("account_register/", RegisterView.as_view(), name='account_register'),
    path("account/token", TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('account/token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('logout/', LogOutView.as_view(), name='logout'),
    path('account/', AllAccountView.as_view(), name='account')
]