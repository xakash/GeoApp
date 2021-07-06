# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin
from .models import Location


@admin.register(Location)
class LocationAdmin(OSMGeoAdmin):
    list_display = ('name', 'location')
    
