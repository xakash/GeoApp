from django.urls import path

from . import views as gisview

app_name = 'gis_app'

urlpatterns = [
    path('map/<int:pk>', gisview.WeatherDataView.as_view(), name='mapView'),
    path('', gisview.DataListView.as_view(), name='listView'),
]