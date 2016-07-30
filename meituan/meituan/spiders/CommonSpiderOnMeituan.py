# -*- coding: utf-8 -*-

import scrapy
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from meituan.items import MenuItem, salersItem
import json, re, chardet, codecs

class MySpiderOnMeituan(CrawlSpider):
    name = 'meituanCspider'
    allowed_domains = ['meituan.com']
    start_urls = ["http://nj.meituan.com/?mtt=1.index%2Fchangecity.0.0.ilktysdu"]

    rules = {
        Rule(LinkExtractor(restrict_xpaths=('//div[@class="J-nav-item"]//dt//a')), callback='salers_parse'),
        # Rule(LinkExtractor(restrict_xpaths=('//div[@id="content"]//div[@class="J-scrollloader cf J-hub"]' +
        #                                     '//a[@class="poi-tile__head"]')), follow=True),
        # Rule(LinkExtractor(), callback=('salers_parse'))

    }

    def salers_parse(self, response):
        mlist = response.xpath('//div[@id="content"]//div[@class="J-scrollloader cf J-hub"]//a[@class="poi-tile__head"]')
        print mlist

        # mitem = salersItem()
        # tmp = response.xpath('//span[@id="map-canvas"]/@data-params').extract()          # extract返回的是Unicode字符串,函数最终进行转换unicode -> ascii
        # if tmp:
        #     mitem['lat_lons'] = self.getPos(self.myencode(tmp[0]))
        # else:
        #     mitem['lat_lons'] = ''
        # tmp = response.xpath('//span[@class="geo"]/text()').extract()
        # if tmp:
        #     mitem['position'] = tmp[0]
        # else:
        #     mitem['position'] = ''
        # tmp = (response.xpath('//span[@class="title"]/text()').extract())
        # if tmp:
        #     mitem['name'] = tmp[0]
        # else:
        #     mitem['name'] = ''
        # tmp = response.xpath('//p[@class="under-title"]/text()').extract()
        # if tmp:
        #     mitem['telephone'] = str(tmp[-1])
        # else:
        #     mitem['telephone'] = ''
        # # mitem['CustomeJudge'] = response.xpath('//li[@class="J-ratelist-item rate-list__item cf"]//p[@class="content"]/text()').extract()
        # tmp = json.dumps(dict(mitem), ensure_ascii=False)   #  ensure_ascii=False 防止序列化将中文变成Unicode编码
        # with codecs.open("salers.json", "a", encoding='utf-8') as wr:
        #     wr.write(tmp)
        #     wr.write('\n')
        # pass

    def getPos(self, buff):
        rem1 = u'"position":\[(.*?)\]'
        r1 = re.compile(rem1, re.M | re.S)
        # buff = self.myencode(buff)
        tmp = eval(r1.findall(buff)[0])
        # print "tmp in getPos:", tmp, '\n'
        return tmp
        pass

    def myencode(self, tmp):
        mychar = chardet.detect(tmp)
        bianma = mychar['encoding']
        print "编码格式：" + bianma + '\n'
        return tmp.decode(bianma.lower(), 'ignore').encode('utf-8')
