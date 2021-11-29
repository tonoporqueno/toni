from pathlib import Path
from django.urls.conf import path
from .views import about
app_name = 'about'
urlpatterns = [
    path('', about, name='about')
]
