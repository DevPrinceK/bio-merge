from django.urls import path
from .views import *

app_name = 'biomerge'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('update-type', UpdateDBSelectionView.as_view(), name='update_type'),
    path('load-data', LoadDataView.as_view(), name='load_data'),
    path('api-results', APIResultsView.as_view(), name='api_results'),
    path('file-results', FileResultsView.as_view(), name='file_results'),
    path('general-search', GeneralSearch.as_view(), name='general_search'),
    path('about-seq', DisplaySequenceView.as_view(), name='about_seq'),
]
