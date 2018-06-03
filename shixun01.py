# -*- coding: utf-8 -*-
"""
Created on Sat Jun  2 15:06:12 2018

@author: lenovo
"""

#a=["1","2","3","4","5","6","7"]
#for i in a:
#    if i=="6":
#        print ("今天是{}".format(i))




#字典dict
#person={"name":"doujie",
#        "long":"180",
#        "sex":"girl",
#        "age":"13"}
#print (person)
#print (person["name"])
#print (person["long"])
#print (person["sex"])
#print (person["age"])




#xue={'name':'薛子谦',
#     'songs':['演员','动物世界'],
#     '昵称':'xiaoxue',
#     '朋友年龄':[47,34,23,56,43]}
#songs=xue['songs']
#print (songs)
#print ("歌曲数量:"+str(len(songs)))
#print(max(xue['朋友年龄']))




#weather={'地点':'乐山',
#         '温度':[25,28,30,31,27],
#         '情况':['多云','转晴','晴','阵雨','小雨'],
#         '时间':'周六'}
#print ("情况数量"+str(len(weather['情况'])))
#print (weather['情况'])
#print (max(weather['温度']))





city_pinyin=input("请输入城市拼音：")
address='http://api.openweathermap.org/data/2.5/weather?q={}&mode=json&units=metric&lang=zh_cn&APPID=6a67ed641c0fda8b69715c43518b6996'
print(address.format(city_pinyin))
#1、看当前城市天气，2、查看其它城市天气，3、保存当前城市天气
print ("欢迎使用全球天气app")
print ("1、看当前城市天气，2、查看其它城市天气，3、保存当前城市天气")
menno=input("请输入菜单：")

if menno=='1':
    print("1、看当前城市天气")
if menno=='2':
    print("2、查看其它城市天气")
if menno=='3':
    print("3、保存当前城市天气")
     
import urllib.request as r
address='http://api.openweathermap.org/data/2.5/weather?q={}&mode=json&units=metric&lang=zh_cn&APPID=6a67ed641c0fda8b69715c43518b6996'
info=r.urlopen(address.format(city_pinyin)).read().decode('utf-8','ignore')
#print(info)
#json(dict)格式工具包
import json
data=json.loads(info)
data['main']['temp']
print('当前温度：'+str(data['main']['temp']))
print('天气情况：'+str(data['weather'][0]['description']))
print('气压：'+str(data['main']['pressure']))




