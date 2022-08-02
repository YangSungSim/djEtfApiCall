from django.urls import URLPattern, path
from .views import * 

urlpatterns = [
    path('<name>/<int:start_date>/<int:end_date>', search2, name='search'),   #postman에서 데이터 집어넣을때
    path('go/', search_from_page, name='search_from_page'),   #웹페이지에서 파라미터 입력후 집어넣을때
    path('', inputForm, name='inputForm'),
]