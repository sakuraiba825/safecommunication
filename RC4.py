#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/30 12:10
# @Author  : 谢雨童
# @Site    : 
# @File    : RC4.py
# @Software: PyCharm
import base64

def get_message():
    print("输入信息:")
    s = input()
    return s

def get_key():
    print("输入秘钥")
    key = input()
    return key

#初始化s盒
def init_box(key):
    s_box = list(range(256))
    j = 0
    for i in range(256):
        j = (j + s_box[i] + ord(key[i % len(key)])) % 256  #ord()返回ASCII码值
        s_box[i], s_box[j] = s_box[j], s_box[i]
    return s_box

def ex_encrypt(plain, box):#加密

    res = []
    i = j = 0
    for s in plain:
        i = (i + 1) % 256
        j = (j + box[i]) % 256
        box[i], box[j] = box[j], box[i]  #//交换s[x]和s[y]
        t = (box[i] + box[j]) % 256
        k = box[t]
        res.append(chr(ord(s) ^ k))  #chr() 用一个范围在 range（256）内的（就是0～255）整数作参数，返回一个对应的字符。
    cipher = "".join(res)
    s=str(base64.b64encode(cipher.encode('utf-8')), 'utf-8')

     # base64的目的也是为了变成可见字符
    print("加密后经过base64编码后的输出:")
    print(s)

    return s

def ex_decrypt(plain, box):#解密

    plain = base64.b64decode(plain)
    plain = bytes.decode(plain)

    res = []
    i = j = 0
    for s in plain:
        i = (i + 1) % 256
        j = (j + box[i]) % 256
        box[i], box[j] = box[j], box[i]
        t = (box[i] + box[j]) % 256
        k = box[t]
        res.append(chr(ord(s) ^ k))
    cipher = "".join(res)

     # base64的目的也是为了变成可见字符
    print("解密后经过base64编码后的输出:")
    print(cipher)

    return cipher

def encrypt():
    message = get_message()
    key = get_key()
    box = init_box(key)
    ex_encrypt(message, box)

if __name__ == '__main__':
       while True:
           encrypt()

