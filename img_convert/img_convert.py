# sys packge
import os
import sys
import time
import string
import pickle
import threading as thread
# image handle
from PIL import Image
# web request
import requests
from bs4 import BeautifulSoup
# py tkinter GUI
import tkinter as tk

# global param
url = ["https://www.bing.com", "https://www.aliyun.com","https://www.baidu.com", "https://www.qq.com", "https://bolywi.github.io/website"]

# function package
def web_request(url):
    response = requests.get(url)
    page_content = BeautifulSoup(response.content, 'lxml')
    print(page_content)

def while_loop():
    num = 0
    while num < 100:
        num += 1
        print('==============> num:', num)
    time.sleep(0.1)

def for_loop():
    for url_v in url:
        print('====================>>>>>>' + url_v)
        web = thread.Thread(target=web_request, args=(url_v,))
        web.start()
        web.join()

def for_range_loop():
    for i in range(0, 10):
        print('value===>>>>>: ' + str(i))
    else:
        print('==============>>>Bye!')  

def handle_image(file_name):
    img = Image.open(file_name)
    print('file_name:', img.filename)
    print('format:', img.format)
    print('size:', img.size)
    print('mode', img.mode)
    color = ''
    for y in range(0, img.height):
        for x in range(0, img.width):
            rgb_img = img.convert('RGB')
            rgb = rgb_img.getpixel((x, y))
            data = rgb[0] << 16 | rgb[1] << 8 | rgb[2]
            color += str(hex(data).zfill(8)) + ', '
        color += '\n'
    img.close()
    return color

def add(x, y)->int:
    result = x + y
    return result

def lambda_demo():
    task = thread.Thread(target=lambda : print('Hello world, this is a thread task'))
    task.start()

def _main_(arg):
    if len(arg) > 3:
        w = int(arg[2])
        h = int(arg[3])
        print('width:', w, 'height:', h)
        im = Image.new("RGBA",(w, h), 'green')
        im.putpixel((0,0), (0, 0, 0, 0))
        im.save(arg[1])
        im.close()
    elif len(arg) > 1:
        img_file = arg[1]
        color = handle_image(img_file)
        with open('demo.h', 'w') as f:
            print(color, file=f)
    else:
        print('option:')
        print("     python main.py file_name")
        print("     python main.py file_name width height")
# main entry
_main_(sys.argv)
