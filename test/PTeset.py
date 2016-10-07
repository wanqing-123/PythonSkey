#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

print 'Python OS'

jsonstr = {"key1": "value1", "key2": "value2"}
print json.dumps(jsonstr)

def mainf():
    print 'main'

if __name__ == '__main__':
    mainf()
