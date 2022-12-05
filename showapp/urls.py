from django.urls import path
from .views import IndexView, DataView, InputView
from . import views

app_name = 'showapp'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('input/', InputView.as_view(), name='form'),
    #path('data/', DataView.as_view(), name='data'),
    path('data/', DataView.as_view(), name='data'),
]