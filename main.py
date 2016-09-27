# -*- coding: utf-8 -*-

import requests
import os

user_agent = {'User-agent': 'Mozilla/5.1'}
r = requests.get('http://www.zhihu.com/people/luoluo-53', headers = user_agent)

path = os.getcwd() + '/origin'
f = open(path, 'w')
f.write(r.text.encode('utf-8'))
f.close()