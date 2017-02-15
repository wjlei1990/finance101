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
from utils import generate_synthetic_stock_daily_price


def test1():
    stock = generate_synthetic_stock_daily_price(s0=100, ndays=250)
    stock.name = "Stock Banana"
    stock.plot()

    print("Price return: %f" % stock.price_return())
    print("Volatility: %f" % stock.volatility())
    print("draw_down: %f" % stock.draw_down())
    print("sharpe: %f" % stock.sharpe())


if __name__ == "__main__":
    test1()
