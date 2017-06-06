#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import json
import codecs

tmp_path = './_tmp'
tmp_file_path = tmp_path + '/.tmp'

if not os.path.exists(tmp_path):
    os.mkdir(tmp_path)

def set (tmp):
    tmp_file = codecs.open(tmp_file_path, 'w+', 'utf-8')
    try:
        tmp_file_w_con = json.dumps(tmp).decode('unicode-escape')
    except Exception as e:
        tmp_file_w_con = ''
    tmp_file.write(tmp_file_w_con)
    tmp_file.close()

def get ():
    try:
        tmp_file = codecs.open(tmp_file_path, 'r', 'utf-8')
    except Exception as e:
        tmp_file = codecs.open(tmp_file_path, 'w+', 'utf-8')

    tmp_file_con = tmp_file.read()
    tmp_file.close()

    try:
        tmp = json.loads(tmp_file_con)
    except Exception as e:
        tmp = {}

    return tmp
