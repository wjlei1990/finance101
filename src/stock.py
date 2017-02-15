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
import matplotlib.pyplot as plt


TRADING_DAYS = 250


class DailyStock(object):
    def __init__(self, data=None, name="UNKNOWN"):
        """
        :param data: data is the array of stock price. Because in python,
        copy is shallow copy, so it is very efficient. However, if you
        want the data to keep intact, please make a copy of the original
        data.
        :type data: numpy.ndarray
        :param name: stock name
        :type name: str
        """
        self.data = data
        self.name = name

    def price_return(self, start=0, end=-1):
        """ Cumulative return """
        return self.data[end] / self.data[start] - 1.0

    def volatility(self, start=0, end=-1):
        """
        :return: the anualized volatility of a stock.
            the dimension of returned volatility will be
            (len(self.data) - 2)
        """
        if end == -1:
            # end = -1 is a corner case here since (end+1) will be 0
            end = len(self.data) - 1

        daily_change = \
            np.diff(self.data[start:(end+1)]) / self.data[start:end]
        std = np.std(daily_change)
        vol = np.sqrt(TRADING_DAYS) * std
        return vol

    def draw_down(self, start=0, end=-1):
        min_price = np.min(self.data[start:end])
        return (min_price - self.data[start]) / self.data[start]

    def sharpe(self, start=0, end=-1):
        if end < 0:
            end = end + len(self.data)
        ndays = end - start + 1
        annual_return = \
            (1 + self.price_return()) ** (float(TRADING_DAYS) / ndays) - 1
        vol = self.volatility()
        return annual_return / vol

    def plot(self):
        plt.figure()
        plt.plot(self.data)
        plt.title(self.name)
        plt.xlabel("days")
        plt.ylabel("stock price")
        plt.show()
