# -*- coding: utf-8 -*-



import requests
import os

import encrypt

#user_agent = {'User-agent': 'Mozilla/5.1'}
#r = requests.get('http://www.zhihu.com/people/luoluo-53', headers = user_agent)

text = {
    'offset': '1',
    'limit': '20',
}
data = encrypt.gen_data(text)

url = 'http://music.163.com/weapi/v1/resource/comments/R_SO_4_26427666'

headers = {
    'Cookie': 'appver=1.5.0.75771;',
    'Referer': 'http://music.163.com/'
}

r = requests.post(url, headers = headers, data = data)

path = os.getcwd() + '/origin'
f = open(path, 'w')
f.write(r.text.encode('utf-8'))
f.close()
