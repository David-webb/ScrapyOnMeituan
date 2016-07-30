# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import scrapy

class MeituanPipeline(object):
    def process_item(self, item, spider):
        return item



# 爬去每个菜单对应网页中的所有商家信息
class MenuPipeline(object):
    def process_item(self, item, MeituancrawlSpider):
        # 进入某一菜单项主页（例如：美食）
        # scrapy.Request(item['murl'], callback=self.item_parse)
        # print "已经调用request\n"
        return item


    def item_parse(self, response):
        mlist = response.xpath('//div[@id="content"]//div[class="poi-tile-nodeal"]/a[class="poi-tile__head"]')
        # 获得主页左侧主菜单
        print "进入二级菜单显示"
        for sel in mlist:
            print 'ops\n'
            # menulist = sel.xpath("//dt//a")
            # for dta in menulist:
            #     print dta, '\n'
                # mitem = MenuItem()
                # mitem['title'] = dta.xpath("text()")[0].extract().encode('utf-8')
                # mitem['murl'] = dta.xpath("@href").extract()
                # yield mitem
        print "二级菜单显示结束！"
        pass
