from django.urls import path
from .views import *

app_name = 'biomerge'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('update-type', UpdateDBSelectionView.as_view(), name='update_type'),
]
