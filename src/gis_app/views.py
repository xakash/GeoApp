# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json
from django.db import models
import requests
import datetime
from .models import Location
from .utils import get_temperature
from django.utils import timezone

from django.views.generic import DetailView, ListView


class DataListView(ListView):
    template_name = 'list.html'
    model = Location
    context_object_name = 'list_data'

    def get_queryset(self):
        queryset = self.model.objects.all()
        return queryset

    def get_context_data(self, **kwargs):
        context = super(DataListView, self).get_context_data(**kwargs)

        context["list_data"] = self.get_queryset()

        return context


class WeatherDataView(DetailView):
    template_name = 'map.html'
    model = Location
    context_object_name = 'location_data'

    def get_queryset(self):
        pk_ = self.kwargs.get('pk')
        queryset = self.model.objects.filter(pk=pk_)
        return queryset

    def get_context_data(self, **kwargs):
        context = super(WeatherDataView, self).get_context_data(**kwargs)

        context["location_data"] = self.get_queryset()
        data = self.get_queryset()
        for data in data:
            print(data.id, data.location)
            lat = str(data.location.y)
            lon = str(data.location.x)
        lat= lat
        lon = lon
      
        fetch_url = requests.get(
            'https://api.weather.gov/points/'+lat+','+lon
        )
        re_str = json.dumps(fetch_url.json(),
                                sort_keys=True,
                                indent=4)
            # print(re_str)
        resp_dict = json.loads(re_str)
            # print(resp_dict)
        final_url=resp_dict['properties']['forecastGridData']
        print(final_url)
        data = requests.get(final_url)
        # print(data)
        data_str = json.dumps(data.json(),
                                sort_keys=True,
                                indent=4)
        data_dict = json.loads(data_str)

        now = timezone.now()
        date = (now.strftime("%Y-%m-%d"))
        time = (now.strftime("%H"))

        
        currentTime = date + "T" + time + ":00:00+00:00/PT1H"
        currentTime2 = date + "T" + time + ":00:00+00:00/PT2H"
        currentTime3 = date + "T" + time + ":00:00+00:00/PT3H"
            

        print(currentTime)
        print(currentTime2)
       
        temp_list=(data_dict['properties']['temperature']['values'])
        humidity_list=(data_dict['properties']['relativeHumidity']['values'])
        # print(humidity_list)
        # print(temp_list)
        keyVal = []
        keyVal.append(currentTime)
        keyVal.append(currentTime2)
        keyVal.append(currentTime3)
     
        result_temp = (list(filter(lambda d:d['validTime'] in keyVal, temp_list)))
        print(result_temp)
        temperature = [item['value'] for item in result_temp]
        final_temp = ""

        for i in temperature:
            final_temp += str(round(i,2))

        # result_temp.update(temp_val)

        # humid_val = {'type': 'humidity'}
        result_humidity = (list(filter(lambda d:d['validTime'] in keyVal, humidity_list)))
        humidity = [item['value'] for item in result_humidity]
        final_humid = ""

        for i in humidity:
            final_humid += str(round(i,2))

        context['temperature'] = final_temp
        context['humidity'] = final_humid

        
        return context