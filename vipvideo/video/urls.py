#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-10-10 13:37
# @Author  : Vassago
# @File    : urls.py
# @Software: PyCharm

from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:url>', views.parse_video, name='parse_video')
]