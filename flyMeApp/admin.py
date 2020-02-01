# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from django.db.models.functions import Trunc
from django.utils.translation import ugettext_lazy as _
from .models import  Ticket, Booking

admin.site.site_header = 'Fly Me To The Moon Admin Page'

# Register your models here.

admin.site.register(Ticket)
admin.site.register(Booking)