# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json
import requests
import datetime
from .models import Location
from django.shortcuts import render

from django.views.generic import DetailView


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

        fetch_url = requests.get(
            'https://api.weather.gov/points/39.7456,-97.0892'
        )
        re_str = json.dumps(fetch_url.json(),
                                sort_keys=True,
                                indent=4)
            # print(re_str)
        resp_dict = json.loads(re_str)
            # print(resp_dict)
        final_url=resp_dict['properties']['forecastGridData']

        data = requests.get(final_url)

        data_str = json.dumps(data.json(),
                                sort_keys=True,
                                indent=4)
        data_dict = json.loads(data_str)
        now = datetime.datetime.now()
        date = (now.strftime("%Y-%m-%d"))
        time = (now.strftime("%H"))
        print(time)
        currentTime = date + "T" + time + ":00:00+00:00/PT1H"
        print(currentTime)

        temp_list=(data_dict['properties']['temperature']['values'])

        humidity_list=(data_dict['properties']['relativeHumidity']['values'])

        keyVal = []
        keyVal.append(currentTime)

        temp_val = {'type': 'temperature'}

        # result_temp = (list(filter(lambda d:d['validTime'] in keyVal, temp_list)))[0]
        # result_temp.update(temp_val)

        humid_val = {'type': 'humidity'}
        result_humidity = (list(filter(lambda d:d['validTime'] in keyVal, humidity_list)))[0]
        result_humidity.update(humid_val)

        # final_result = result_temp, result_humidity
        # json_data = json.dumps(final_result, indent=4)

        # context['weather_data'] = json_data
        return context