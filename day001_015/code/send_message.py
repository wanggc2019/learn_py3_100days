#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
网络编程

网络应用开发  发送短信
"""
import urllib.parse
import http.client
import json


def main():
    host = "106.ihuyi.com"
    sms_send_uri = "/webservice/sms.php?method=Submit"
    # 下面的参数需要填入自己注册的账号和对应的密码
    # 用户名和密码 查看用户名请登录用户中心->验证码、通知短信->帐户及签名设置->APIID、APIKEY
    # mobile 填写要发动信息得手机号
    params = urllib.parse.urlencode({'account': 'APIID', 'password': 'APIKEY',
                                     'content': '您的验证码是：147258。请不要把验证码泄露给其他人。', 'mobile': 'my phone number', 'format': 'json'})
    print(params)
    headers = {'Content-type': 'application/x-www-form-urlencoded', 'Accept': 'text/plain'}
    conn = http.client.HTTPConnection(host, port=80, timeout=30)
    conn.request('POST', sms_send_uri, params, headers)
    response = conn.getresponse()
    response_str = response.read()
    jsonstr = response_str.decode('utf-8')
    print(json.loads(jsonstr))
    conn.close()


if __name__ == '__main__':
    main()
