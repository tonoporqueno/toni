from pathlib import Path
from django.urls.conf import path
from .views import sintac
app_name = 'sintactico'
urlpatterns = [
    path('', sintac, name='sintactico')
]
