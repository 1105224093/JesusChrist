#! /usr/bin/python
#! -*- encoding:utf-8 -*-
from bs4 import BeautifulSoup
from urllib import request
import codecs
import csv
import os



def get_responses():

    url_list = []
    ana_results_all = []
    for i in range(int(get_pages(url_base))):
        url_list.append(url_base+str(i+1))
    # print(url_list)
    for i in range(len(url_list)):
        req = request.Request(url_list[i], headers=headers)
        # print(url_list[i])
        response = request.urlopen(req).read()
        soup = BeautifulSoup(response, 'html5lib')
        att = {
            "class": "pic"
        }
        ana_results = soup.find_all("a", attrs=att)
        print(ana_results)

        ana_results_all += ana_results
    tran_csv("books.csv", ana_results_all)


# 获取页码数
def get_pages(url):
    req = request.Request(url+"1", headers=headers)
    resp = request.urlopen(req).read()
    soup = BeautifulSoup(resp, "html5lib")
    att1 = {
        "name": "Fy"
    }
    ul1 = soup.find("ul", attrs=att1)
    att2 = {
        "class": "null"
    }
    lis = ul1.find_all("a", attrs=att2)
    return lis[len(lis)-1].text


#分析http响应
def analysis(content):
    pass
    #返回tag列表


#转成表格
def tran_csv(filename, books):

    with codecs.open(filename, 'a', 'utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=['书名', '网页地址'])
        writer.writeheader()
        for book in books:
            # print(book.img.attrs)
            book_name = book['title']
            book_url = book['href']
            if len(book.img.attrs) == 2:
                pic_url = book.img['src']
            else:
                pic_url = book.img['data-original']
            try:
                os.mkdir('pictures')
            except FileExistsError:
                pass
            # 去文件名中除特殊字符
            book_name_fixed = book_name.replace('"', "").replace(":", '').replace("/", '').replace("?", '')
            book_name_fixed = book_name_fixed.replace("*", '').replace("|", '').replace("<", '').replace(">", '')
            with open("./pictures/%s.png" % book_name_fixed, 'wb') as f1:
                # print(type(pic_url))
                f1.write(request.urlopen(pic_url).read())
            bookdit = {
                "书名": book_name,
                "网页地址": book_url,
            }
            writer.writerow(bookdit)


if __name__ == "__main__":
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, "
                      "like Gecko) Chrome/71.0.3578.80 Safari/537.36",

    }
    url_base = "http://search.dangdang.com/?key=python&act=input&page_index="
    get_responses()

