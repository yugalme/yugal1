# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.


from django.http import HttpResponse
import logging
logger = logging.getLogger('loggly_logs')

def index(request):
    logger.info('Hi, Welcome to Loggly.')
    try:
        raise KeyError
    except Exception:
        logger.exception('Booking exception: City: Bora Bora, French Polynesia Hotel: Le Meridien')
        
    print("hello")
    return HttpResponse("Hello, world. You're at the polls index.")


"""def index(request):
    logger.info('Hi, Welcome to Loggly.')
    a = []
    try:
        a[5]
    except Exception as e:
        logger.exception(e)
        raise e

    print("hello")
    return HttpResponse("Hello, world. You're at the polls index.")"""



def test1():
    raise Exception('Booking exception: City: Bora Bora, French Polynesia Hotel: Le Meridien')

def test2():
    test1()
