from django.urls import URLPattern, path
from .views import * 

urlpatterns = [
    path('<name>/<int:start_date>/<int:end_date>', search, name='search'),
    path('', inputForm, name='inputForm'),
]