# coding=utf-8

import weixinRun
import weixinNotice
from flask import Flask
from flask import render_template
import datetime

app = Flask(__name__)

@app.route('/index')
def index():

    return render_template('index.html')

@app.route('/heartbeat')
def heartbeat():

    nowTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # 现在
    weixinNotice.sendInfo("app心跳检测", "app is alive",nowTime, "tree")
    return 'server received'

if __name__ == '__main__':

    app.run(host='0.0.0.0')
