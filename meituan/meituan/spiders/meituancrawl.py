# -*- coding: utf-8 -*-
import chardet
import json
import re
import scrapy
from meituan.ajaxSimulate import AjaxSimulate
from meituan.items import salersItem


class MeituancrawlSpider(scrapy.Spider):
    name = "meituancrawl"
    allowed_domains = ["meituan.com"]
    start_urls = [
        "http://nj.meituan.com/?mtt=1.index%2Fchangecity.0.0.ilktysdu",
    ]

    def parse(self, response):
        mlist = response.xpath('//div[@class="J-nav-item"]')
        # 获得主页左侧主菜单
        for sel in mlist:
            menulist = sel.xpath("//dt//a")
            for dta in menulist:
                mitem = {}
                mitem['title'] = dta.xpath("text()")[0].extract()   # 若print 则encode('utf-8')
                mitem['murl'] = dta.xpath("@href")[0].extract()
                request = scrapy.Request(mitem['murl'], callback=self.item_parse, method='GET', meta={'title': mitem['title']})
                yield request
                break
        pass

    def item_parse(self, response):

        # 获得当前页面(Ajax刷新前)中所有商铺的urls
        mlist = response.selector.xpath('//div[@id="content"]//div[@class="J-scrollloader cf J-hub"]//a[@class="poi-tile__head"]/@href')
        # print "获得商铺url：", len(mlist)

        # 获取当前网页ajax请求后的商户url
        ajaxparam = response.xpath('//div[@id="content"]//div[@class="J-scrollloader cf J-hub"]/@data-async-params')[0].extract()
        AjaxS = AjaxSimulate()
        mcookie = response.headers['Set-Cookie']
        AjaxSList = AjaxS.getUrlAfterAjax(ajaxparam, response.url, mcookie)
        for i in mlist:
            if i.extract() not in AjaxSList:
                AjaxSList.append(i.extract())

        # 合并AjaxSList和mlist
        for j in AjaxSList:
            yield scrapy.Request(j, callback=self.salers_parse, meta={'url': j})

        # 获取当前页面下一页的url,并递归调用本函数
        pageList = response.xpath('//div[@class="paginator-wrapper"]//li[contains(@class,"next")]/a/@href')
        if pageList:       # 还有下一页
            yield scrapy.Request('http://nj.meituan.com' + pageList[0].extract(), callback=self.item_parse, meta={'title':response.meta['title']})
        else:
            print '\n\n\n\n', response.meta['title'], "结束！\n\n\n\n\n\n\n"

    def salers_parse(self, response):
        mitem = salersItem()

        # 获得坐标
        tmp = response.xpath('//span[@id="map-canvas"]/@data-params').extract()          # extract返回的是Unicode字符串,函数最终进行转换unicode -> ascii
        if tmp:
            mitem['lat_lons'] = self.getPos(self.myencode(tmp[0]))
        else:
            mitem['lat_lons'] = u''

        # 获得地址
        tmp = response.xpath('//span[@class="geo"]/text()').extract()
        if tmp:
            mitem['position'] = tmp[0]
        else:
            mitem['position'] = response.meta['url']

        # 获得店名
        tmp = (response.xpath('//span[@class="title"]/text()').extract())
        if tmp:
            mitem['name'] = tmp[0]
        else:
            mitem['name'] = u''

        # 获得电话
        tmp = response.xpath('//p[@class="under-title"]/text()').extract()
        if tmp:
            mitem['telephone'] = str(tmp[-1])
        else:
            mitem['telephone'] = u''

        # 获得用户评论
        # mitem['CustomeJudge'] = response.xpath('//li[@class=" J-ratelist-item rate-list__item cf"]//p[@class="content"]/text()').extract()

        tmp = json.dumps(dict(mitem), ensure_ascii=False)
        # print mitem['position'],'\n', mitem
        import codecs
        with codecs.open("salerstest.json", "a", encoding='utf-8') as wr:
            wr.write(tmp)
            wr.write('\n')
            # pass

    def getPos(self, buff):
        rem1 = u'"position":\[(.*?)\]'
        r1 = re.compile(rem1, re.M | re.S)
        tmp = eval(r1.findall(buff)[0])
        return tmp
        pass

    def myencode(self, tmp):
        mychar = chardet.detect(tmp)
        bianma = mychar['encoding']  # AttributeError: 'NoneType' object has no attribute 'lower'
        # print "编码格式：" + bianma + '\n'
        return tmp.decode(bianma.lower(), 'ignore').encode('utf-8')

