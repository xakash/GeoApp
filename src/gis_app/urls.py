from django.urls import path

from . import views as gisview

app_name = 'gis_app'

urlpatterns = [
    path('<int:pk>', gisview.WeatherDataView.as_view()),
]