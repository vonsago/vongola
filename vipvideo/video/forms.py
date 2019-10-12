#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-10-10 16:18
# @Author  : Vassago
# @File    : forms.py
# @Software: PyCharm

from django import forms


class UrlForm(forms.Form):
    your_url = forms.CharField(label='Your url', max_length=1000)
