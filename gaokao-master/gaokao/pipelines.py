# -*- coding: utf-8 -*-
import pymysql
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
class GaokaoPipeline(object):
    def __init__(self):
        # 连接数据库
        self.connect = pymysql.connect(
            host='127.0.0.1',  # 数据库地址
            port=3306,  # 数据库端口
            db='gaokao',  # 数据库名
            user='root',  # 数据库用户名
            passwd='',  # 数据库密码
            charset='utf8',  # 编码方式
            use_unicode=True)
        # 通过cursor执行增删查改
        self.cursor = self.connect.cursor()
    def process_item(self, item, spider):

        if item['province'] == "" or item['province'] == "[]":
            item['province'] = "无"
        if item['schooltype'] == "" or item['schooltype'] == "[]":
            item['schooltype'] = "无"
        if item['schoolproperty'] == "" or item['schoolproperty'] == "[]":
            item['schoolproperty'] = "无"

        if item['level'] == "" or item['level'] == "[]":
            item['level'] = "无"
        if item['membership'] == "" or item['membership'] == "[]":
            item['membership'] = "无"

        if item['schoolnature'] == "" or item['schoolnature'] == "[]":
            item['schoolnature'] = "无"
        if item['shoufei'] == "" or item['shoufei'] == "[]":
            item['shoufei'] = "无"
        if item['jianjie'] == "" or item['jianjie'] == "[]":
            item['jianjie'] = "无"

        if item['oldname'] == "" or item['oldname'] == "[]":
            item['oldname'] = "无"

        if item['num'] == "--":
            item['num'] = -1

        sq = "insert into `school` (`schoolid`,`schoolname`,`province`,`schooltype`,`schoolproperty`,`f985`,`f211`,`s_level`,`membership`," \
             "`schoolnature`,`shoufei`,`jianjie`,`schoolcode`,`ranking`,`rankingCollegetype`,`guanwang`,`oldname`,`num`) " \
             "values('%s','%s','%s','%s','%s','%d','%d','%s','%s','%s','%s','%s','%s','%d','%d','%s','%s','%d')" \
             % (item['schoolid'], item['schoolname'], item['province'], item['schooltype'], item['schoolproperty']
                , int(item['f985']), int(item['f211']), item['level'], ''.join(item['membership']),
                ''.join(item['schoolnature'])
                , ''.join(item['shoufei']), ''.join(item['jianjie']), item['schoolcode'], int(item['ranking']),
                int(item['rankingCollegetype'])
                , item['guanwang'], item['oldname'], int(item['num']))

        self.cursor.execute(sq)
        self.connect.commit()
        return item
