#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys

sys.path.append('./lib')
sys.path.append('./lib/core')
sys.path.append('./lib/core/vendor')

import json
from core import main

import converter_util

debug = False

def get (query):
    result = main.get(query)
    payload = None
    if result:
        try:
            payload = converter_util.converte(result)
        except Exception as e:
            if debug:
                print e
    if not payload:
        return False

    return payload

def clean ():
    main.clean()
