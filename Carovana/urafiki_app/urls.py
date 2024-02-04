# urafiki_app/urls.py

from django.contrib import admin
from django.urls import path, include
from bustrack.views import custom_login  # Imports the login view from bustrack app

urlpatterns = [
    path('', custom_login, name='custom_login'),  # Empty path will redirect to the login view in bustrack app
    path('admin/', admin.site.urls),
    path('bustrack/', include('bustrack.urls')),
]

