import re
import json
import scrapy
import pymysql
from scrapy.conf import settings
from gaokao.items import GaokaoItem


class gaokao(scrapy.Spider):
    name = "gaokao"
    def start_requests(self):
        headers = {
             'Referer': 'https://gkcx.eol.cn/soudaxue/queryschool.html?&page=1',
        }
        urls=[
            'https://data-gkcx.eol.cn/soudaxue/queryschool.html?messtype=jsonp&callback=&province=&schooltype=&page=1&size=30&keyWord1=&schoolprop=&schoolflag=&schoolsort=&schoolid=&_=1543499182148'#.format(i) for i in range(1,2)
        #'https://data-gkcx.eol.cn/soudaxue/queryschool.html?messtype=jsonp&callback=&size=2843'
        ]
        for url in urls:
            yield scrapy.Request(url=url,callback=self.parse,headers=headers)

    def parse(self, response):
        headers = {
            'Referer': 'https://gkcx.eol.cn/soudaxue/queryschool.html?&page=1',
        }
        text = response.text.rstrip(';')
        text = eval(text)
        schools = text["school"]
        a = int(text['totalRecord']['num'])
        str = response.url.split("&")
        page = int(str[4].split("=")[1])
        print("-----------------》%d" % page)
        item = GaokaoItem()
        for school in schools:
            item['schoolid'] = school['schoolid']
            item['schoolname'] = school['schoolname']
            if school['province'] == "" or school['province'] == "[]":
                item['province'] = "无"
            else:
                item['province'] = school['province']
            if school['schooltype'] == "" or school['schooltype'] == "[]":
                item['schooltype'] = "无"
            else:
                item['schooltype'] = school['schooltype']
            if school['schoolproperty'] == ""or school['schoolproperty'] == "[]":
                item['schoolproperty'] = "无"
            else:
                item['schoolproperty'] = school['schoolproperty']
            item['f985'] = school['f985']
            item['f211'] = school['f211']
            if school['level'] == "" or school['level'] == "[]":
                item['level'] = "无"
            else:
                item['level'] = school['level']
            if school['membership'] == "" or school['membership'] == "[]":
                item['membership'] = "无"
            else:
                item['membership'] = school['membership']
            if school['schoolnature'] == "" or school['schoolnature'] == "[]":
                item['schoolnature'] = "无"
            else:
                item['schoolnature'] = school['schoolnature']
            if school['shoufei'] == "" or school['shoufei'] == "[]":
                item['shoufei'] = "无"
            else:
                item['shoufei'] = school['shoufei']
            if school['jianjie'] == "" or school['jianjie'] == "[]":
                item['jianjie'] = "无"
            else:
                item['jianjie'] = school['jianjie']
            item['schoolcode'] = school['schoolcode']
            item['ranking'] = school['ranking']
            item['rankingCollegetype'] = school['rankingCollegetype']
            item['guanwang'] = school['guanwang']
            if school['oldname'] == "" or school['oldname'] == "[]":
                item['oldname'] = "无"
            else:
                item['oldname'] = school['oldname']
            if school['num'] == "--":
                item['num'] = -1
            else:
                item['num'] = school['num']
            yield item
        #for i in range (2,100):
        #    next_page = response.urljoin('https://data-gkcx.eol.cn/soudaxue/queryschool.html?messtype=jsonp&callback=&province=&schooltype=&page=%s&size=30&keyWord1=&schoolprop=&schoolflag=&schoolsort=&schoolid=&_=1543499182148' % i)
        #    yield scrapy.Request(next_page, callback=self.parse)


        if (page == 1):
            b = 30
            c = a // b + 1
            for i in range(c):
                page = i + 1
                res = "page=%d" % page
                newurl = str[0]+"&"+str[1]+"&"+str[2]+"&"+str[3] + "&" + res + "&" + str[5]+"&"+str[6]+"&"+str[7]+"&"+str[8]+"&"+str[9]+"&schoolid=&_=1543499182148"
                print(newurl)
                print("----------+++++++++++++》%s" % newurl)
                yield scrapy.Request(url=newurl, callback=self.parse, headers=headers)
        self.log("总共有%s条数据" % a)
