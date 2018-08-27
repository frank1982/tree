# -*- coding: utf-8 -*
import os
import pexpect
import sys
from selenium import webdriver

if __name__ == '__main__':

    print 'wall start...'

    # 在mac terminal 执行指令,开启chrome调试iOS safari
    child = pexpect.spawn('ios_webkit_debug_proxy -f chrome-devtools://devtools/bundled/inspector.html')
    child.logfile = sys.stdout
    child.expect('Listing devices on :9221')#不加不会等！
    while (1):
        pass


    # start chome by selenium
    #driver = webdriver.Chrome('/Users/developer/Desktop/devTools/chromedriver')
    #driver.get("http://localhost:9222/")

    

    #在mac terminal 执行指令
    #child = pexpect.spawn('ssh root@47.75.6.252')
    #child.logfile = sys.stdout
    #child.expect('password:')#不加不会等！
    #child.sendline('Xuyinan0907')
    #child.expect('#')

    #BundleId = com.apple.SafariViewService + +++应用的名称 = SafariViewService版本号 = 1.0
    #BundleId = com.apple.mobilesafari + +++应用的名称 = Safari版本号 = 11.0