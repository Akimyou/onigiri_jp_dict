#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys
import main

if len(sys.argv) > 1:
    query = sys.argv[1]
else:
    query = ''

if query:
    print main.get(query)
else:
    main.clean()
