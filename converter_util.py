#!/usr/bin/python
# -*- coding: UTF-8 -*-

import json
import hashlib

payload = {}

def converte (data):
    for word in data['2']:
        c_word = {
            'title': _first(word['0']),
            'subtitle': ''.join(word['5']) + '\t' + '%s  %d-%d  %s' % (_first(word['1']),
                word['3'], word['2'], _first(word['4'])),
            'audio': _first(word['6']),
            'type': {}
        }
        c_word['uid'] = _hash_json(c_word)
        payload[c_word['uid']] = c_word
        for btype in word['9']:
            for explain in btype['1']:
                c_type = {
                    'title': _first(btype['0']),
                    'subtitle': _first(explain['0']),
                    'example': {}
                }
                c_type['uid'] = _hash_json(c_type)
                c_word['type'][c_type['uid']] = c_type
                for g_exp in explain['1']:
                    for exp in g_exp:
                        c_exp = {
                            'audio': ''
                        }
                        for index in range(0, len(exp)):
                            if index == 0:
                                c_exp['title'] = exp[index]
                            if index == 1:
                                c_exp['subtitle'] = exp[index]
                        c_exp['uid'] = _hash_json(c_exp)
                        c_type['example'][c_exp['uid']] = c_exp
                for exp in explain['2']:
                    c_exp = {
                        'audio': ''
                    }
                    for index in range(0, len(exp)):
                        if index == 0:
                            c_exp['title'] = exp[index]
                        if index == 1:
                            c_exp['subtitle'] = exp[index]
                        if index == 2:
                            c_exp['audio'] = exp[index]
                    c_exp['uid'] = _hash_json(c_exp)
                    c_type['example'][c_exp['uid']] = c_exp

    if not payload.keys():
        raise Exception

    return payload

def _stringify_json (json_data, decode = False):
    tmp = json.dumps(json_data)
    if decode:
        tmp = tmp.decode('unicode-escape')
    return tmp

def _hash_json (json_data):
    tmp = _stringify_json(json_data)
    return hashlib.md5(tmp).hexdigest()

def _first (list):
    if len(list) > 0:
        return list[0]
    return ''

def _big_type_get_title (big_type):
    _print_json(big_type)

def _print_json (json_data):
    print _stringify_json(json_data, True)
