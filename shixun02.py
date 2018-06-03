# -*- coding: utf-8 -*-
"""
Created on Sun Jun  3 09:45:12 2018

@author: lenovo
"""

city=input('请输入城市：')
import urllib.request as r
url='http://api.openweathermap.org/data/2.5/forecast?q=mianyang,cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996'
info=r.urlopen(url.format('city')).read().decode('utf-8','ignore')
import json
data=json.loads(info)
print('天气情况：'+data['list'][2]['weather'][0]['description'])
print ('当前温度：'+str(data['list'][1]['main']['temp'])+'华氏度')
print('气压：'+str(data['list'][1]['main']['pressure']))
print('未来天气状况：') 
for i in range(4): 
  print('第'+str(i+1)+'天天气：') 
  print(data['list'][(i+1)*8]['dt_txt'])
  print('天气情况：'+data['list'][(i+1)*8]['weather'][0]['description'])
  print('温度：'+str(data['list'][(i+1)*8]['main']['temp'])+'华氏度')
  print('气压：'+str(data['list'][(i+1)*8]['main']['pressure']))