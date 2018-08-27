# coding=utf-8

import sys
import os
import socket
import hashlib
import urllib2
import json
import time
import weixinRun
reload(sys)
sys.setdefaultencoding("utf-8")


def sendInfo(title,content1,content2,remark):

    try:
        print 'sendTextInfo'
        post_data = {
                    "touser":'owmz2w6UGRbjLqEPGB8AWa2nK5rw',
                    "template_id":"TAwWy-Am9SnHUAfKVhMnzTIUWMFPQyvwuDNbZx0plM4",
                    "data":{
                        "first": {
                            "value":title,
                            "color":"#173177"
                        },
                        "keyword1":{
                            "value":content1,
                            "color":"#173177"
                        },
                        "keyword2": {
                            "value":content2,
                            "color":"#173177"
                        },
                        "remark":{
                            "value":remark,
                            "color":"#173177"
                        }
                    }
        }
        file = open('weixinToken.txt')
        accessToken=file.read()
        requrl = "https://api.weixin.qq.com/cgi-bin/message/template/send?access_token="+accessToken
        print requrl
        headers = {'Content-Type': 'application/json'}
        request = urllib2.Request(url=requrl, headers=headers, data=json.dumps(post_data))
        response = urllib2.urlopen(request)
        jsonResult=json.load(response)
        print jsonResult
        #return jsonResult['msgid']


    except Exception,e:

        print("send wx info error")
        print(e)


