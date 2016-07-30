# -*- coding: utf-8 -*-

import json
import urllib
# from StringIO import StringIO
from scrapy.selector import Selector
import httplib


class AjaxSimulate():
    def getAjaxData(self, refer, poiidList, poiData, mcookie):

        data = {
            'poiidList': json.dumps(poiidList[32:80]),       # json.dumps(poiidList[:])!!!!!!
            'bigImageMode': "true",
            'poiData': json.dumps(poiData[32:80])
        }
        data_encode = urllib.urlencode(data)  #　请求数据的格式不太一致
        aurl = "http://nj.meituan.com/index/poilist"
        headers = {
            'Host': 'nj.meituan.com',
            'User-Agent': 'Mozilla/5.0 (X11; Linux i586; rv:31.0) Gecko/20100101 Firefox/31.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Connection': 'keep-alive',
            'X-Requested-With': 'XMLHttpRequest',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Referer': 'http://nj.meituan.com/category/meishi?mtt=1.index%2Ffloornew.nc.1.ilvprxya',
            'Content-Length': len(data_encode),
            'Cookie': mcookie
        }

        httpClient = None
        page = ''
        try:
            httpClient = httplib.HTTPConnection("nj.meituan.com", 80, timeout=10)
            httpClient.request(method="POST", url=aurl, body=data_encode, headers=headers)
            response = httpClient.getresponse()
            page = json.loads(response.read())['data']
            # print response.status
            # print response.reason
            # print response.version
            # print response.read()
            # print response.getheaders() # 获取头信息
        except Exception, e:
            print e
        finally:
            if httpClient:
                httpClient.close()
        page = Selector(text=page)
        mlist = page.xpath('//a[@class="poi-tile__head"]/@href').extract()
        return mlist
        pass


    def getUrlAfterAjax(self, param, refer, mcookie):
        tmpparam = param.encode('utf-8')
        tmpparam = json.loads(tmpparam)
        data = json.loads(tmpparam['data'])
        poiidList = data['poiidList']
        poiData = data['poiData']
        urlList = self.getAjaxData(refer, poiidList, poiData, mcookie)
        return urlList


if __name__ == '__main__':

    # tmp = AjaxSimulate()
    # tmp.getAjaxData('','','','')


    # with open('../postonlineresp.txt','r') as rd:
    #     tmp = rd.read()
    # buf = StringIO(tmp)
    # tmp = gzip.GzipFile(fileobj=buf)
    # print tmp.read()


    # 测试迭代器
    mygenerator = (x*x for x in range(3))
    for i in mygenerator:
        print(i)
    for i in mygenerator:
        print(i)
    pass