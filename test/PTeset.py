#!/usr/bin/env python
# -*- coding: utf-8 -*-
# by ayalamih on Oct. 7, 2016

import json

jsonstr = {"key1": "value1", "key2": "value2"}
print json.dumps(jsonstr)

def mainf():
    print 'main'

if __name__ == '__main__':
    mainf()

mainf()
print '__name__ 值:', __name__
