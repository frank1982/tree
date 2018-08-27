#!/usr/bin/python
# coding=utf-8

import urllib2
import urllib
import json
import sys
import time


_weixinToken=''
SETTINGS={

    'WEIXIN_ID':'gh_250953953f8a', #公众号微信ID
    'APPID':'wx0e2dc591178fa325',
    'SECRET':'3820685afb55088c32a565a0fb2f64c3',

}

#获取access_token
#http请求方式: GET
#https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=APPID&secret=APPSECRET
def getAccessToken():#每2个小时执行一次

    ACCESS_TOKEN_URL="https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=%s&secret=%s" %(SETTINGS['APPID'],SETTINGS['SECRET'])
    req = urllib2.Request(ACCESS_TOKEN_URL)
    res_data = urllib2.urlopen(req)
    res_data2 = res_data.read().decode("utf-8-sig")
    res = json.loads(res_data2)
    #print res
    access_token=res['access_token']
    file = open('weixinToken.txt', 'w')
    file.write(access_token)
    return access_token


if __name__ == '__main__':

    while True:

        getAccessToken()
        time.sleep(7200)

