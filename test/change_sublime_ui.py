#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# by ayalamih on Oct. 12, 2016
# 

#
# 黑色
#"theme": "ayu2.sublime-theme",
#"color_scheme": "Packages/ayu/ayu.tmTheme",
#
# 亮色
#"theme": "ayu-light2.sublime-theme",
#"color_scheme": "Packages/ayu/ayu-light.tmTheme",
#

import time
import datetime

settings_path = '/Users/ayalamih/Library/Application Support/Sublime Text 3/Packages/User/Preferences.sublime-settings'
hour = (int(time.strftime("%H")))
f = open(settings_path, 'r+')
flist = f.readlines()
if hour >= 8 and hour <= 18:
    print 'daytime'
    try:
        flist[20] = '    "theme":"ayu-light2.sublime-theme",\n'
        flist[21] = '    "color_scheme":"Packages/ayu/ayu-light.tmTheme",\n'
        f = open(settings_path,'w+')
        f.writelines(flist)
    finally:
        f.close()
elif hour >= 18 and hour < 24:
    print 'sunset'
    try:
        flist[20] = '    "theme":"ayu2.sublime-theme",\n'
        flist[21] = '    "color_scheme":"Packages/ayu/ayu.tmTheme",\n'
        f = open(settings_path,'w+')
        f.writelines(flist)
    finally:
        f.close()



