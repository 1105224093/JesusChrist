#! /usr/bin/python
#! -*- encoding:utf-8 -*-
from bs4 import BeautifulSoup
from urllib import request
import time
import codecs, csv



def get_responses():
    for i in range(5):
        url_list.append(url_base+str(i+1))
    for i in range(len(url_list)):
        req = request.Request(url_list[i], headers=headers)
        response = request.urlopen(req).read()
        ana_result = analysis(response)
        for i in ana_result:
            print(type(i))
        time.sleep(1)
        # with open(str(i+1)+".txt", 'wb') as f:
            # f.write(response)


def get_pages(url):
    pass


def analysis(content):
    soup = BeautifulSoup(content, features='lxml')
    att = {
        "class": "pic"
    }
    book = soup.find_all("a", attrs=att)
    #返回tag列表
    return book


def tran_csv(filename, books):
    with codecs.open(filename, 'w', 'utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=['书名', '网页地址', '图片地址'])
        writer.writeheader()
        writer.writerow()



if __name__ == "__main__":
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, "
                      "like Gecko) Chrome/71.0.3578.80 Safari/537.36",

    }

    url_base = "http://search.dangdang.com/?key=python&act=input&page_index="
    url_list = []
    get_responses()

