"""grouptraveltracker_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from allauth.account.views import confirm_email
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('apps.trips.urls')),
    path('/registration/', include('rest_auth.registration.urls')),
    path('rest-auth/', include('rest_auth.urls')),
    path('registration/account-confirm-email/(?P<key>.+)/$', confirm_email, name='account_confirm_email'),
    path('accounts/', include('allauth.urls')),
]


# USER registration:
# POST /rest-auth/registration/
# {
#   "email": "test@test.com",
#   "password1": "ujmik,ol.",
#   "password2": "ujmik,ol."
# }
# This will send out verification email with account confirmation URL looking like 
# this: /accounts-rest/registration/account-confirm-email/MQ:1iU6Li:17ruSRLybL38zXvc91no26v2YGw/

# User login- Login is denied before user confirms his email.
# POST /rest-auth/login/
# {
#   "email": "test@test.com",
#   "password": "ujmik,ol."
# }

# POST /rest-auth/password/change/
# {
#   "new_password1": ".lo,kimju",
#   "new_password2": ".lo,kimju"
# }