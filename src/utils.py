#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
"""
Stock price implementation

:copyright:
    Wenjie Lei (wjlei1990@gmail.com), 2017
:license:
    UNDERTERMINED YET
"""
from __future__ import print_function, division, absolute_import
import numpy as np
from stock import DailyStock


def generate_synthetic_stock_daily_price(
        s0=100, ndays=250, interest_rate=0.001, sigma=0.1):
    data = np.zeros(ndays)
    data[0] = s0
    random_values = np.random.normal(0, sigma, ndays)
    for i in range(1, ndays):
        ds = data[i-1] * (interest_rate + sigma * random_values[i])
        data[i] = data[i-1] + ds

    return DailyStock(data=data)
