# coding=utf-8
# from scrapy.selector import Selector
# from selenium import webdriver
# from meituancrawl import myencode
# import HTMLParser
# driver = webdriver.PhantomJS()  # webdriver.Firefox()
# from lxml import html
#
# # driver.execute_script(
# #     '''
# #         window.document.body.scrollTop = document.body.scrollHeight;
# #         window.setTimeout(
# #         function ()
# #         {
# #             phantom.exit();
# #         }, 6000+500);
# #
# #         '''
# # )
# driver.set_window_size(744, 1366)
# driver.get('http://nj.meituan.com/category/meishi?mtt=1.index%2Ffloornew.nc.1.ilvprxya')
# # driver.execute_async_script()
# # print driver.page_source, '\n'
# html_parse = HTMLParser.HTMLParser()
# page = html.fromstring(html_parse.unescape(driver.page_source))
# # print page
# mlist = page.xpath('//a[@class="poi-tile__head"]')
# # mlist = driver.find_elements_by_xpath('//a[@class="poi-tile__head"]')
# # mlist = driver.find_elements_by_xpath('//div[@id="content"]//div[@class="J-scrollloader cf J-hub"]//a[@class="poi-tile__head"]')
# print len(mlist)
# driver.quit()

from lxml import html
import urllib
import urllib2
import json
# from meituancrawl import myencode
from StringIO import StringIO
import gzip
from scrapy.selector import Selector
from lxml import html
import HTMLParser
# import requests

# def salers_parse(response):
#         html_parse = HTMLParser.HTMLParser()
#         response = html.fromstring(response)
#         # response = Selector(response.encode('utf-8'))
#         mitem = {}
#         tmp = response.xpath('//span[@id="map-canvas"]/@data-params')      # extract返回的是Unicode字符串,函数最终进行转换unicode -> ascii
#         # print 'lat_lon', tmp, '\n'
#         if tmp:
#             mitem['lat_lons'] = getPos(myencode(tmp[0]))
#         else:
#             mitem['lat_lons'] = ''
#         tmp = response.xpath('//span[@class="geo"]/text()')
#         if tmp:
#             mitem['position'] = tmp[0]
#         else:
#             mitem['position'] = "not Found"
#         tmp = (response.xpath('//span[@class="title"]/text()'))
#         if tmp:
#             mitem['name'] = tmp[0]
#         else:
#             mitem['name'] = response.xpath("/html/text()")
#         tmp = response.xpath('//p[@class="under-title"]/text()')
#         if tmp:
#             mitem['telephone'] = str(tmp[-1])
#         else:
#             mitem['telephone'] = ''
#         with open('dataajax1.txt', 'a') as wr:
#             wr.write(json.dumps(dict(mitem), ensure_ascii=False))
#             wr.write('\n')
#         # return mitem
#
#
# import re
# def getPos( buff):
#         rem1 = u'"position":\[(.*?)\]'
#         r1 = re.compile(rem1, re.M | re.S)
#         # buff = self.myencode(buff)
#         tmp = eval(r1.findall(buff)[0])
#         # print "tmp in getPos:", tmp, '\n'
#         return tmp
#
if __name__ == "__main__":
    #     # d = '{"pageIndex":0,"pageSize":30,"title":""}'
    #     ajax_url = 'http://nj.meituan.com/index/poilist'
    ajax_url = 'http://nj.meituan.com/category/meishi'
    #     data = {
    #         'poiidList':"[42931715,4935526,5249646,5277401,42132051,5676128,5898129,40643993,6097441,40063484,6660963,6882249,51900465,40013263,40691775,41166727,41278178,41809805,41579428,3292746,50571500,42355449,5325634,5137206,4438997,42399220,40440361,6231135,41337403,51034379,40578179,6736715]",
    #         'bigImageMode':"true",
    #         'poiData': '[{"dealid":"30404633","acm":"AcategoryC4681791065322908775.42931715.33","dealacm":"AcategoryC4681791065322908775.42931715.33.30404633.1"},{"dealid":"27447577","acm":"AcategoryC4681791065322908775.4935526.34","dealacm":"AcategoryC4681791065322908775.4935526.34.27447577.1"},{"dealid":"27376235,28407335","acm":"AcategoryC4681791065322908775.5249646.35","dealacm":"AcategoryC4681791065322908775.5249646.35.27376235.1,AcategoryC4681791065322908775.5249646.35.28407335.2"},{"dealid":"26359978","acm":"AcategoryC4681791065322908775.5277401.36","dealacm":"AcategoryC4681791065322908775.5277401.36.26359978.1"},{"dealid":"29454047,29456921","acm":"AcategoryC4681791065322908775.42132051.37","dealacm":"AcategoryC4681791065322908775.42132051.37.29454047.1,AcategoryC4681791065322908775.42132051.37.29456921.2"},{"dealid":"25759031","acm":"AcategoryC4681791065322908775.5676128.38","dealacm":"AcategoryC4681791065322908775.5676128.38.25759031.1"},{"dealid":"26955143","acm":"AcategoryC4681791065322908775.5898129.39","dealacm":"AcategoryC4681791065322908775.5898129.39.26955143.1"},{"dealid":"27201014,29052021,29052029,27268712","acm":"AcategoryC4681791065322908775.40643993.40","dealacm":"AcategoryC4681791065322908775.40643993.40.27201014.1,AcategoryC4681791065322908775.40643993.40.29052021.2,AcategoryC4681791065322908775.40643993.40.29052029.3,AcategoryC4681791065322908775.40643993.40.27268712.4"},{"dealid":"24987788,29843978,25708067,31226682","acm":"AcategoryC4681791065322908775.6097441.41","dealacm":"AcategoryC4681791065322908775.6097441.41.24987788.1,AcategoryC4681791065322908775.6097441.41.29843978.2,AcategoryC4681791065322908775.6097441.41.25708067.3,AcategoryC4681791065322908775.6097441.41.31226682.4"},{"dealid":"30018732,30023667,31375497,31375519,31375545,31375510,31375536","acm":"AcategoryC4681791065322908775.40063484.42","dealacm":"AcategoryC4681791065322908775.40063484.42.30018732.1,AcategoryC4681791065322908775.40063484.42.30023667.2,AcategoryC4681791065322908775.40063484.42.31375497.3,AcategoryC4681791065322908775.40063484.42.31375519.4,AcategoryC4681791065322908775.40063484.42.31375545.5,AcategoryC4681791065322908775.40063484.42.31375510.6,AcategoryC4681791065322908775.40063484.42.31375536.7"},{"dealid":"26250713,26249576,28367511,26250705,28367523,26623219,26623228,26623223,26623240,31398091,26250697,31397963","acm":"AcategoryC4681791065322908775.6660963.43","dealacm":"AcategoryC4681791065322908775.6660963.43.26250713.1,AcategoryC4681791065322908775.6660963.43.26249576.2,AcategoryC4681791065322908775.6660963.43.28367511.3,AcategoryC4681791065322908775.6660963.43.26250705.4,AcategoryC4681791065322908775.6660963.43.28367523.5,AcategoryC4681791065322908775.6660963.43.26623219.6,AcategoryC4681791065322908775.6660963.43.26623228.7,AcategoryC4681791065322908775.6660963.43.26623223.8,AcategoryC4681791065322908775.6660963.43.26623240.9,AcategoryC4681791065322908775.6660963.43.31398091.10,AcategoryC4681791065322908775.6660963.43.26250697.11,AcategoryC4681791065322908775.6660963.43.31397963.12"},{"dealid":"8709594,9204142","acm":"AcategoryC4681791065322908775.6882249.44","dealacm":"AcategoryC4681791065322908775.6882249.44.8709594.1,AcategoryC4681791065322908775.6882249.44.9204142.2"},{"dealid":"31095101,31095089,31095097","acm":"AcategoryC4681791065322908775.51900465.45","dealacm":"AcategoryC4681791065322908775.51900465.45.31095101.1,AcategoryC4681791065322908775.51900465.45.31095089.2,AcategoryC4681791065322908775.51900465.45.31095097.3"},{"dealid":"28250453,28251032,28251017","acm":"AcategoryC4681791065322908775.40013263.46","dealacm":"AcategoryC4681791065322908775.40013263.46.28250453.1,AcategoryC4681791065322908775.40013263.46.28251032.2,AcategoryC4681791065322908775.40013263.46.28251017.3"},{"dealid":"29601457","acm":"AcategoryC4681791065322908775.40691775.47","dealacm":"AcategoryC4681791065322908775.40691775.47.29601457.1"},{"dealid":"31257476","acm":"AcategoryC4681791065322908775.41166727.48","dealacm":"AcategoryC4681791065322908775.41166727.48.31257476.1"},{"dealid":"30269951","acm":"AcategoryC4681791065322908775.41278178.49","dealacm":"AcategoryC4681791065322908775.41278178.49.30269951.1"},{"dealid":"27408489,27766049,27765802","acm":"AcategoryC4681791065322908775.41809805.50","dealacm":"AcategoryC4681791065322908775.41809805.50.27408489.1,AcategoryC4681791065322908775.41809805.50.27766049.2,AcategoryC4681791065322908775.41809805.50.27765802.3"},{"dealid":"26851507","acm":"AcategoryC4681791065322908775.41579428.51","dealacm":"AcategoryC4681791065322908775.41579428.51.26851507.1"},{"dealid":"26736921,26736745","acm":"AcategoryC4681791065322908775.3292746.52","dealacm":"AcategoryC4681791065322908775.3292746.52.26736921.1,AcategoryC4681791065322908775.3292746.52.26736745.2"},{"dealid":"30654352","acm":"AcategoryC4681791065322908775.50571500.53","dealacm":"AcategoryC4681791065322908775.50571500.53.30654352.1"},{"dealid":"28146106,31175553","acm":"AcategoryC4681791065322908775.42355449.54","dealacm":"AcategoryC4681791065322908775.42355449.54.28146106.1,AcategoryC4681791065322908775.42355449.54.31175553.2"},{"dealid":"27130075","acm":"AcategoryC4681791065322908775.5325634.55","dealacm":"AcategoryC4681791065322908775.5325634.55.27130075.1"},{"dealid":"6231076,30839016","acm":"AcategoryC4681791065322908775.5137206.56","dealacm":"AcategoryC4681791065322908775.5137206.56.6231076.1,AcategoryC4681791065322908775.5137206.56.30839016.2"},{"dealid":"25456954,30842348,30842160","acm":"AcategoryC4681791065322908775.4438997.57","dealacm":"AcategoryC4681791065322908775.4438997.57.25456954.1,AcategoryC4681791065322908775.4438997.57.30842348.2,AcategoryC4681791065322908775.4438997.57.30842160.3"},{"dealid":"25023503,25097392,29577640","acm":"AcategoryC4681791065322908775.42399220.58","dealacm":"AcategoryC4681791065322908775.42399220.58.25023503.1,AcategoryC4681791065322908775.42399220.58.25097392.2,AcategoryC4681791065322908775.42399220.58.29577640.3"},{"dealid":"30068448,30070347","acm":"AcategoryC4681791065322908775.40440361.59","dealacm":"AcategoryC4681791065322908775.40440361.59.30068448.1,AcategoryC4681791065322908775.40440361.59.30070347.2"},{"dealid":"27788792,30001973","acm":"AcategoryC4681791065322908775.6231135.60","dealacm":"AcategoryC4681791065322908775.6231135.60.27788792.1,AcategoryC4681791065322908775.6231135.60.30001973.2"},{"dealid":"29696740","acm":"AcategoryC4681791065322908775.41337403.61","dealacm":"AcategoryC4681791065322908775.41337403.61.29696740.1"},{"dealid":"30372513,30372305,30372511","acm":"AcategoryC4681791065322908775.51034379.62","dealacm":"AcategoryC4681791065322908775.51034379.62.30372513.1,AcategoryC4681791065322908775.51034379.62.30372305.2,AcategoryC4681791065322908775.51034379.62.30372511.3"},{"dealid":"27609116,27609353","acm":"AcategoryC4681791065322908775.40578179.63","dealacm":"AcategoryC4681791065322908775.40578179.63.27609116.1,AcategoryC4681791065322908775.40578179.63.27609353.2"},{"dealid":"26078838,26081007","acm":"AcategoryC4681791065322908775.6736715.64","dealacm":"AcategoryC4681791065322908775.6736715.64.26078838.1,AcategoryC4681791065322908775.6736715.64.26081007.2"}]'
    #     }
    #     # data = {
    #     #     'poiidList':"[51761811,1749997,4371945,52608208,1574101,1751787,4963021,6918059,6631370,721685,5293139,40970291,42154494,6722443,40160880,1749095]",
    #     #     'bigImageMode':"true",
    #     #     'poiData': '[{"dealid":"30577019","acm":"AcategoryC4681791065322908775.51761811.65","dealacm":"AcategoryC4681791065322908775.51761811.65.30577019.1"},{"dealid":"30404555","acm":"AcategoryC4681791065322908775.1749997.66","dealacm":"AcategoryC4681791065322908775.1749997.66.30404555.1"},{"dealid":"25145111","acm":"AcategoryC4681791065322908775.4371945.67","dealacm":"AcategoryC4681791065322908775.4371945.67.25145111.1"},{"dealid":"30862973","acm":"AcategoryC4681791065322908775.52608208.68","dealacm":"AcategoryC4681791065322908775.52608208.68.30862973.1"},{"dealid":"28023378,28023628,28023679,28023651,28857549","acm":"AcategoryC4681791065322908775.1574101.69","dealacm":"AcategoryC4681791065322908775.1574101.69.28023378.1,AcategoryC4681791065322908775.1574101.69.28023628.2,AcategoryC4681791065322908775.1574101.69.28023679.3,AcategoryC4681791065322908775.1574101.69.28023651.4,AcategoryC4681791065322908775.1574101.69.28857549.5"},{"dealid":"29979152,29979162,29968287","acm":"AcategoryC4681791065322908775.1751787.70","dealacm":"AcategoryC4681791065322908775.1751787.70.29979152.1,AcategoryC4681791065322908775.1751787.70.29979162.2,AcategoryC4681791065322908775.1751787.70.29968287.3"},{"dealid":"25013404","acm":"AcategoryC4681791065322908775.4963021.71","dealacm":"AcategoryC4681791065322908775.4963021.71.25013404.1"},{"dealid":"25145113","acm":"AcategoryC4681791065322908775.6918059.72","dealacm":"AcategoryC4681791065322908775.6918059.72.25145113.1"},{"dealid":"7468690","acm":"AcategoryC4681791065322908775.6631370.73","dealacm":"AcategoryC4681791065322908775.6631370.73.7468690.1"},{"dealid":"26938988,30845842","acm":"AcategoryC4681791065322908775.721685.74","dealacm":"AcategoryC4681791065322908775.721685.74.26938988.1,AcategoryC4681791065322908775.721685.74.30845842.2"},{"dealid":"30968373,30709034","acm":"AcategoryC4681791065322908775.5293139.75","dealacm":"AcategoryC4681791065322908775.5293139.75.30968373.1,AcategoryC4681791065322908775.5293139.75.30709034.2"},{"dealid":"28450896","acm":"AcategoryC4681791065322908775.40970291.76","dealacm":"AcategoryC4681791065322908775.40970291.76.28450896.1"},{"dealid":"27792565,27792571,27895399,27915147,28035646","acm":"AcategoryC4681791065322908775.42154494.77","dealacm":"AcategoryC4681791065322908775.42154494.77.27792565.1,AcategoryC4681791065322908775.42154494.77.27792571.2,AcategoryC4681791065322908775.42154494.77.27895399.3,AcategoryC4681791065322908775.42154494.77.27915147.4,AcategoryC4681791065322908775.42154494.77.28035646.5"},{"dealid":"29238196","acm":"AcategoryC4681791065322908775.6722443.78","dealacm":"AcategoryC4681791065322908775.6722443.78.29238196.1"},{"dealid":"29401277","acm":"AcategoryC4681791065322908775.40160880.79","dealacm":"AcategoryC4681791065322908775.40160880.79.29401277.1"},{"dealid":"29768826","acm":"AcategoryC4681791065322908775.1749095.80","dealacm":"AcategoryC4681791065322908775.1749095.80.29768826.1"}]'
    #     # }
    data = "poiidList=%5B2562728%2C41166727%2C6970061%2C5592284%2C6580346%2C41510157%2C6631370%2C4935526%2C50955292%2C5676128%2C40013263%2C42931715%2C6097441%2C5898129%2C5277401%2C41579428%2C41809805%2C41278178%2C3292746%2C50571500%2C42355449%2C5325634%2C5137206%2C4438997%2C42399220%2C40440361%2C6231135%2C41337403%2C51034379%2C40578179%2C6736715%2C51761811%5D&bigImageMode=true&poiData=%5B%7B%22dealid%22%3A%2229481902%22%2C%22acm%22%3A%22AcategoryC15484869372451100728.2562728.33%22%2C%22dealacm%22%3A%22AcategoryC15484869372451100728.2562728.33.29481902.1%22%7D%2C%7B%22dealid%22%3A%2231257476%22%2C%22acm%22%3A%22AcategoryC15484869372451100728.41166727.34%22%2C%22dealacm%22%3A%22AcategoryC15484869372451100728.41166727.34.31257476.1%22%7D%2C%7B%22dealid%22%3A%2227570297%2C27570418%22%2C%22acm%22%3A%22AcategoryC15484869372451100728.6970061.35%22%2C%22dealacm%22%3A%22AcategoryC15484869372451100728.6970061.35.27570297.1%2CAcategoryC15484869372451100728.6970061.35.27570418.2%22%7D%2C%7B%22dealid%22%3A%2227910937%22%2C%22acm%22%3A%22AcategoryC15484869372451100728.5592284.36%22%2C%22dealacm%22%3A%22AcategoryC15484869372451100728.5592284.36.27910937.1%22%7D%2C%7B%22dealid%22%3A%2226003443%22%2C%22acm%22%3A%22AcategoryC15484869372451100728.6580346.37%22%2C%22dealacm%22%3A%22AcategoryC15484869372451100728.6580346.37.26003443.1%22%7D%2C%7B%22dealid%22%3A%2227376235%22%2C%22acm%22%3A%22AcategoryC15484869372451100728.41510157.38%22%2C%22dealacm%22%3A%22AcategoryC15484869372451100728.41510157.38.27376235.1%22%7D%2C%7B%22dealid%22%3A%222359713%2C7468690%22%2C%22acm%22%3A%22AcategoryC15484869372451100728.6631370.39%22%2C%22dealacm%22%3A%22AcategoryC15484869372451100728.6631370.39.2359713.1%2CAcategoryC15484869372451100728.6631370.39.7468690.2%22%7D%2C%7B%22dealid%22%3A%2227447577%22%2C%22acm%22%3A%22AcategoryC15484869372451100728.4935526.40%22%2C%22dealacm%22%3A%22AcategoryC15484869372451100728.4935526.40.27447577.1%22%7D%2C%7B%22dealid%22%3A%2231064064%2C31064047%22%2C%22acm%22%3A%22AcategoryC15484869372451100728.50955292.41%22%2C%22dealacm%22%3A%22AcategoryC15484869372451100728.50955292.41.31064064.1%2CAcategoryC15484869372451100728.50955292.41.31064047.2%22%7D%2C%7B%22dealid%22%3A%2225759031%22%2C%22acm%22%3A%22AcategoryC15484869372451100728.5676128.42%22%2C%22dealacm%22%3A%22AcategoryC15484869372451100728.5676128.42.25759031.1%22%7D%2C%7B%22dealid%22%3A%2228250453%2C28251032%2C28251017%22%2C%22acm%22%3A%22AcategoryC15484869372451100728.40013263.43%22%2C%22dealacm%22%3A%22AcategoryC15484869372451100728.40013263.43.28250453.1%2CAcategoryC15484869372451100728.40013263.43.28251032.2%2CAcategoryC15484869372451100728.40013263.43.28251017.3%22%7D%2C%7B%22dealid%22%3A%2230404633%22%2C%22acm%22%3A%22AcategoryC15484869372451100728.42931715.44%22%2C%22dealacm%22%3A%22AcategoryC15484869372451100728.42931715.44.30404633.1%22%7D%2C%7B%22dealid%22%3A%2224987788%2C29843978%2C25708067%2C31226682%22%2C%22acm%22%3A%22AcategoryC15484869372451100728.6097441.45%22%2C%22dealacm%22%3A%22AcategoryC15484869372451100728.6097441.45.24987788.1%2CAcategoryC15484869372451100728.6097441.45.29843978.2%2CAcategoryC15484869372451100728.6097441.45.25708067.3%2CAcategoryC15484869372451100728.6097441.45.31226682.4%22%7D%2C%7B%22dealid%22%3A%2226955143%22%2C%22acm%22%3A%22AcategoryC15484869372451100728.5898129.46%22%2C%22dealacm%22%3A%22AcategoryC15484869372451100728.5898129.46.26955143.1%22%7D%2C%7B%22dealid%22%3A%2226359978%22%2C%22acm%22%3A%22AcategoryC15484869372451100728.5277401.47%22%2C%22dealacm%22%3A%22AcategoryC15484869372451100728.5277401.47.26359978.1%22%7D%2C%7B%22dealid%22%3A%2226851507%22%2C%22acm%22%3A%22AcategoryC15484869372451100728.41579428.48%22%2C%22dealacm%22%3A%22AcategoryC15484869372451100728.41579428.48.26851507.1%22%7D%2C%7B%22dealid%22%3A%2227408489%2C27766049%2C27765802%22%2C%22acm%22%3A%22AcategoryC15484869372451100728.41809805.49%22%2C%22dealacm%22%3A%22AcategoryC15484869372451100728.41809805.49.27408489.1%2CAcategoryC15484869372451100728.41809805.49.27766049.2%2CAcategoryC15484869372451100728.41809805.49.27765802.3%22%7D%2C%7B%22dealid%22%3A%2230269951%22%2C%22acm%22%3A%22AcategoryC15484869372451100728.41278178.50%22%2C%22dealacm%22%3A%22AcategoryC15484869372451100728.41278178.50.30269951.1%22%7D%2C%7B%22dealid%22%3A%2226736921%2C26736745%22%2C%22acm%22%3A%22AcategoryC15484869372451100728.3292746.51%22%2C%22dealacm%22%3A%22AcategoryC15484869372451100728.3292746.51.26736921.1%2CAcategoryC15484869372451100728.3292746.51.26736745.2%22%7D%2C%7B%22dealid%22%3A%2230654352%22%2C%22acm%22%3A%22AcategoryC15484869372451100728.50571500.52%22%2C%22dealacm%22%3A%22AcategoryC15484869372451100728.50571500.52.30654352.1%22%7D%2C%7B%22dealid%22%3A%2228146106%2C31175553%22%2C%22acm%22%3A%22AcategoryC15484869372451100728.42355449.53%22%2C%22dealacm%22%3A%22AcategoryC15484869372451100728.42355449.53.28146106.1%2CAcategoryC15484869372451100728.42355449.53.31175553.2%22%7D%2C%7B%22dealid%22%3A%2227130075%22%2C%22acm%22%3A%22AcategoryC15484869372451100728.5325634.54%22%2C%22dealacm%22%3A%22AcategoryC15484869372451100728.5325634.54.27130075.1%22%7D%2C%7B%22dealid%22%3A%226231076%2C30839016%22%2C%22acm%22%3A%22AcategoryC15484869372451100728.5137206.55%22%2C%22dealacm%22%3A%22AcategoryC15484869372451100728.5137206.55.6231076.1%2CAcategoryC15484869372451100728.5137206.55.30839016.2%22%7D%2C%7B%22dealid%22%3A%2225456954%22%2C%22acm%22%3A%22AcategoryC15484869372451100728.4438997.56%22%2C%22dealacm%22%3A%22AcategoryC15484869372451100728.4438997.56.25456954.1%22%7D%2C%7B%22dealid%22%3A%2225023503%2C25097392%2C29577640%22%2C%22acm%22%3A%22AcategoryC15484869372451100728.42399220.57%22%2C%22dealacm%22%3A%22AcategoryC15484869372451100728.42399220.57.25023503.1%2CAcategoryC15484869372451100728.42399220.57.25097392.2%2CAcategoryC15484869372451100728.42399220.57.29577640.3%22%7D%2C%7B%22dealid%22%3A%2230068448%2C30070347%22%2C%22acm%22%3A%22AcategoryC15484869372451100728.40440361.58%22%2C%22dealacm%22%3A%22AcategoryC15484869372451100728.40440361.58.30068448.1%2CAcategoryC15484869372451100728.40440361.58.30070347.2%22%7D%2C%7B%22dealid%22%3A%2227788792%2C30001973%22%2C%22acm%22%3A%22AcategoryC15484869372451100728.6231135.59%22%2C%22dealacm%22%3A%22AcategoryC15484869372451100728.6231135.59.27788792.1%2CAcategoryC15484869372451100728.6231135.59.30001973.2%22%7D%2C%7B%22dealid%22%3A%2229696740%22%2C%22acm%22%3A%22AcategoryC15484869372451100728.41337403.60%22%2C%22dealacm%22%3A%22AcategoryC15484869372451100728.41337403.60.29696740.1%22%7D%2C%7B%22dealid%22%3A%2230372513%2C30372305%2C30372511%22%2C%22acm%22%3A%22AcategoryC15484869372451100728.51034379.61%22%2C%22dealacm%22%3A%22AcategoryC15484869372451100728.51034379.61.30372513.1%2CAcategoryC15484869372451100728.51034379.61.30372305.2%2CAcategoryC15484869372451100728.51034379.61.30372511.3%22%7D%2C%7B%22dealid%22%3A%2227609116%2C27609353%22%2C%22acm%22%3A%22AcategoryC15484869372451100728.40578179.62%22%2C%22dealacm%22%3A%22AcategoryC15484869372451100728.40578179.62.27609116.1%2CAcategoryC15484869372451100728.40578179.62.27609353.2%22%7D%2C%7B%22dealid%22%3A%2226078838%2C26081007%22%2C%22acm%22%3A%22AcategoryC15484869372451100728.6736715.63%22%2C%22dealacm%22%3A%22AcategoryC15484869372451100728.6736715.63.26078838.1%2CAcategoryC15484869372451100728.6736715.63.26081007.2%22%7D%2C%7B%22dealid%22%3A%2230577019%22%2C%22acm%22%3A%22AcategoryC15484869372451100728.51761811.64%22%2C%22dealacm%22%3A%22AcategoryC15484869372451100728.51761811.64.30577019.1%22%7D%5D"
    # data_encode = urllib.urlencode(data)
    request = urllib2.Request(url=ajax_url, data=data)
    request.add_header("Host", "nj.meituan.com")
    request.add_header("User-Agent","Mozilla/5.0 (X11; Linux i586; rv:31.0) Gecko/20100101 Firefox/31.0")
    request.add_header("Accept","text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8")
    request.add_header("Accept-Language", "en-US,en;q=0.5")
    request.add_header("Accept-Encoding", "gzip, deflate")
    request.add_header("X-Request-With", "XMLHttpRequest")
    request.add_header("Content-Type", "application/x-www-form-urlencoded; charset=UTF-8")
    request.add_header("Referer","http://nj.meituan.com/category/meishi?mtt=1.index%2Ffloornew.nc.1.ilvprxya")
    request.add_header("Content-Length", "7467")
    request.add_header("Cookie", "uuid=5b737188f407f80ff402.1458747457.1.0.1; oc=Q7i8N7-FkttutAWbwPFexBkX4j-K1WnImPSucnYbe-GHZ9XkWfMEYaPguXmTHI2cLjeSEZz4lhyak_SCcDCejGzhECSjEjzeGcUGOX5-mzr_jF2m4gDxKxEnYdWqL2VaIijdx8uugpPRQlKmcjgK2yY8D9JFTYlQ6jvU51IU0b4; ci=55; abt=1458950159.0%7CACE; __mta=151911942.1458747461922.1458950160368.1458950163134.37; __utma=211559370.310281063.1458747462.1458915735.1458950160.9; __utmz=211559370.1458881460.4.2.utmcsr=baidu|utmccn=baidu|utmcmd=organic|utmctr=post%20content-length%20%E5%BF%85%E9%A1%BB%E8%AE%BE%E7%BD%AE%EF%BC%9F|utmcct=homepage; __utmv=211559370.|1=city=nj=1; _lx_utm=utm_source%3Dbaiduutm_medium%3Dorganicutm_term%3Dpost%2520content-length%2520%25E5%25BF%2585%25E9%25A1%25BB%25E8%25AE%25BE%25E7%25BD%25AE%25EF%25BC%259Futm_content%3Dhomepageutm_campaign%3Dbaidu; stick-qrcode=1; lsu=; ignore-zoom=true; __utmc=211559370; SID=2ekst2gpj11ebkm509vjg7a3l0; __utmb=211559370.2.10.1458950160")



    # print request.headers
    f = urllib2.urlopen(request)
    tmp1 = f.read()
    buf = StringIO(tmp1)
    tmp = gzip.GzipFile(fileobj=buf)
    with open("result.txt", 'w') as wr:
        wr.write(tmp.read())
    # print f, "shuchuraw\n"
    # content = myencode(tmp.read())
    print tmp.read()
    #     html_parse = HTMLParser.HTMLParser()
    #     page = html.fromstring(html_parse.unescape(content))
    #
    #     mlist = page.xpath('//div[@id="content"]//div[@class="J-scrollloader cf J-hub"]//a[@class="poi-tile__head"]/@href')
    #     tmp = []
    #     for sel in mlist:
    #         # print 'url', sel, '\n'
    #         ttmp = requests.get(sel)
    #         tmp.append(salers_parse(ttmp.text))
    #         # break
    #     # print content
    #     # content = json.dumps(tmp, ensure_ascii=False)
    #
    #     # content = json.loads(content)
    #     # print content
    #


    # 用来查重的
    # import json
    # content = []
    # with open("../../salers.json",'r') as rd:
    #     for line in rd.readlines():
    #         content.append(json.loads(line))
    #
    #
    # with open("dataajax1.json", 'r') as rd:
    #     with open("answer.json", 'a') as wr:
    #         count = 1
    #         for line in rd.readlines():
    #             tmp = json.loads(line)
    #             if tmp not in content:
    #                 # wr.write('num:'+str(count)+'\t')
    #                 print line
    #                 wr.write(line)
    #                 # wr.write('\n')
    #             count += 1


    # import re
    #
    # def finddealid(buff, file):
    #     rem1 = u'\{.*?\}'  # \\"dealid\\"::????
    #     # print buff
    #     r1 = re.compile(rem1, re.M | re.S)
    #     # buff = self.myencode(buff)
    #     # tmp = eval(r1.findall(buff))
    #     tmp = r1.findall(buff)
    #     count = 0
    #     with open(file, 'a') as wr:
    #         for i in tmp:
    #             if "dealid" in i:
    #                 count += 1
    #                 wr.write(i)
    #                 wr.write('\n')


    # with open("../../meituanpost.txt",'r') as rd:
    #     finddealid(myencode(rd.read()), "source.txt")
    # with open("../../head.txt",'r') as rd:
    #     finddealid(myencode(rd.read()), "source2.txt")
    # with open("head2.txt",'r') as rd:
    #     finddealid(myencode(rd.read()), "sourcehead2.txt")

























# -*- coding: utf-8 -*-

# from lxml import html
# import urllib
# import urllib2
import json
# from meituan.spiders.meituancrawl import myencode
# from StringIO import StringIO
import gzip, chardet
# from scrapy.selector import Selector
# from lxml import html
# import HTMLParser
# import requests
# import re
import httplib
def myencode(tmp):
    mychar = chardet.detect(tmp)
    bianma = mychar['encoding']
    print "编码格式：" + bianma + '\n'
    return tmp.decode(bianma, 'ignore').encode('utf-8')


class AjaxSimulate():
    def getAjaxData(self, time, refer, poiidList, poiData, mcookie):
        data = {}
        mcookie = 'uuid=5b737188f407f80ff402.1458747457.1.0.1; oc=Q7i8N7-FkttutAWbwPFexBkX4j-K1WnImPSucnYbe-GHZ9XkWfMEYaPguXmTHI2cLjeSEZz4lhyak_SCcDCejGzhECSjEjzeGcUGOX5-mzr_jF2m4gDxKxEnYdWqL2VaIijdx8uugpPRQlKmcjgK2yY8D9JFTYlQ6jvU51IU0b4; ci=55; abt=1458950159.0%7CACE; __mta=151911942.1458747461922.1458950160368.1458950163134.37; __utma=211559370.310281063.1458747462.1458915735.1458950160.9; __utmz=211559370.1458881460.4.2.utmcsr=baidu|utmccn=baidu|utmcmd=organic|utmctr=post%20content-length%20%E5%BF%85%E9%A1%BB%E8%AE%BE%E7%BD%AE%EF%BC%9F|utmcct=homepage; __utmv=211559370.|1=city=nj=1; _lx_utm=utm_source%3Dbaiduutm_medium%3Dorganicutm_term%3Dpost%2520content-length%2520%25E5%25BF%2585%25E9%25A1%25BB%25E8%25AE%25BE%25E7%25BD%25AE%25EF%25BC%259Futm_content%3Dhomepageutm_campaign%3Dbaidu; stick-qrcode=1; lsu=; ignore-zoom=true; __utmc=211559370; SID=2ekst2gpj11ebkm509vjg7a3l0; __utmb=211559370.2.10.1458950160'
        # if time == 1:
        #     data = {
        #         'poiidList': json.dumps(poiidList[32:64]),       # json.dumps(poiidList[:])!!!!!!
        #         'bigImageMode': "true",
        #         'poiData': json.dumps(poiData[32:64])
        #     }
        # elif time == 2:
        #     data = {
        #         'poiidList': json.dumps(poiidList[64:80]),         # json.dumps(poiidList[:])!!!!!!
        #         'bigImageMode': "true",
        #         'poiData': json.dumps(poiData[64:80])
        #     }
        # else:
        #     print "param is error!"

        aurl = "http://nj.meituan.com/index/poilist"

        # data_encode = urllib.urlencode(data)  #　请求数据的格式不太一致
        # print data_encode,'\nmydata:', len(data_encode)
        data = 'poiidList=%5B2562728%2C41166727%2C6970061%2C5592284%2C6580346%2C41510157%2C6631370%2C4935526%2C50955292%2C5676128%2C40013263%2C42931715%2C6097441%2C5898129%2C5277401%2C41579428%2C41809805%2C41278178%2C3292746%2C50571500%2C42355449%2C5325634%2C5137206%2C4438997%2C42399220%2C40440361%2C6231135%2C41337403%2C51034379%2C40578179%2C6736715%2C51761811%5D&bigImageMode=true&poiData=%5B%7B%22dealid%22%3A%2229481902%22%2C%22acm%22%3A%22AcategoryC5164586507100027312.2562728.33%22%2C%22dealacm%22%3A%22AcategoryC5164586507100027312.2562728.33.29481902.1%22%7D%2C%7B%22dealid%22%3A%2231257476%22%2C%22acm%22%3A%22AcategoryC5164586507100027312.41166727.34%22%2C%22dealacm%22%3A%22AcategoryC5164586507100027312.41166727.34.31257476.1%22%7D%2C%7B%22dealid%22%3A%2227570297%2C27570418%22%2C%22acm%22%3A%22AcategoryC5164586507100027312.6970061.35%22%2C%22dealacm%22%3A%22AcategoryC5164586507100027312.6970061.35.27570297.1%2CAcategoryC5164586507100027312.6970061.35.27570418.2%22%7D%2C%7B%22dealid%22%3A%2227910937%22%2C%22acm%22%3A%22AcategoryC5164586507100027312.5592284.36%22%2C%22dealacm%22%3A%22AcategoryC5164586507100027312.5592284.36.27910937.1%22%7D%2C%7B%22dealid%22%3A%2226003443%22%2C%22acm%22%3A%22AcategoryC5164586507100027312.6580346.37%22%2C%22dealacm%22%3A%22AcategoryC5164586507100027312.6580346.37.26003443.1%22%7D%2C%7B%22dealid%22%3A%2227376235%22%2C%22acm%22%3A%22AcategoryC5164586507100027312.41510157.38%22%2C%22dealacm%22%3A%22AcategoryC5164586507100027312.41510157.38.27376235.1%22%7D%2C%7B%22dealid%22%3A%222359713%2C7468690%22%2C%22acm%22%3A%22AcategoryC5164586507100027312.6631370.39%22%2C%22dealacm%22%3A%22AcategoryC5164586507100027312.6631370.39.2359713.1%2CAcategoryC5164586507100027312.6631370.39.7468690.2%22%7D%2C%7B%22dealid%22%3A%2227447577%22%2C%22acm%22%3A%22AcategoryC5164586507100027312.4935526.40%22%2C%22dealacm%22%3A%22AcategoryC5164586507100027312.4935526.40.27447577.1%22%7D%2C%7B%22dealid%22%3A%2231064064%2C31064047%22%2C%22acm%22%3A%22AcategoryC5164586507100027312.50955292.41%22%2C%22dealacm%22%3A%22AcategoryC5164586507100027312.50955292.41.31064064.1%2CAcategoryC5164586507100027312.50955292.41.31064047.2%22%7D%2C%7B%22dealid%22%3A%2225759031%22%2C%22acm%22%3A%22AcategoryC5164586507100027312.5676128.42%22%2C%22dealacm%22%3A%22AcategoryC5164586507100027312.5676128.42.25759031.1%22%7D%2C%7B%22dealid%22%3A%2228250453%2C28251032%2C28251017%22%2C%22acm%22%3A%22AcategoryC5164586507100027312.40013263.43%22%2C%22dealacm%22%3A%22AcategoryC5164586507100027312.40013263.43.28250453.1%2CAcategoryC5164586507100027312.40013263.43.28251032.2%2CAcategoryC5164586507100027312.40013263.43.28251017.3%22%7D%2C%7B%22dealid%22%3A%2230404633%22%2C%22acm%22%3A%22AcategoryC5164586507100027312.42931715.44%22%2C%22dealacm%22%3A%22AcategoryC5164586507100027312.42931715.44.30404633.1%22%7D%2C%7B%22dealid%22%3A%2224987788%2C29843978%2C25708067%2C31226682%22%2C%22acm%22%3A%22AcategoryC5164586507100027312.6097441.45%22%2C%22dealacm%22%3A%22AcategoryC5164586507100027312.6097441.45.24987788.1%2CAcategoryC5164586507100027312.6097441.45.29843978.2%2CAcategoryC5164586507100027312.6097441.45.25708067.3%2CAcategoryC5164586507100027312.6097441.45.31226682.4%22%7D%2C%7B%22dealid%22%3A%2226955143%22%2C%22acm%22%3A%22AcategoryC5164586507100027312.5898129.46%22%2C%22dealacm%22%3A%22AcategoryC5164586507100027312.5898129.46.26955143.1%22%7D%2C%7B%22dealid%22%3A%2226359978%22%2C%22acm%22%3A%22AcategoryC5164586507100027312.5277401.47%22%2C%22dealacm%22%3A%22AcategoryC5164586507100027312.5277401.47.26359978.1%22%7D%2C%7B%22dealid%22%3A%2226851507%22%2C%22acm%22%3A%22AcategoryC5164586507100027312.41579428.48%22%2C%22dealacm%22%3A%22AcategoryC5164586507100027312.41579428.48.26851507.1%22%7D%2C%7B%22dealid%22%3A%2227408489%2C27766049%2C27765802%22%2C%22acm%22%3A%22AcategoryC5164586507100027312.41809805.49%22%2C%22dealacm%22%3A%22AcategoryC5164586507100027312.41809805.49.27408489.1%2CAcategoryC5164586507100027312.41809805.49.27766049.2%2CAcategoryC5164586507100027312.41809805.49.27765802.3%22%7D%2C%7B%22dealid%22%3A%2230269951%22%2C%22acm%22%3A%22AcategoryC5164586507100027312.41278178.50%22%2C%22dealacm%22%3A%22AcategoryC5164586507100027312.41278178.50.30269951.1%22%7D%2C%7B%22dealid%22%3A%2226736921%2C26736745%22%2C%22acm%22%3A%22AcategoryC5164586507100027312.3292746.51%22%2C%22dealacm%22%3A%22AcategoryC5164586507100027312.3292746.51.26736921.1%2CAcategoryC5164586507100027312.3292746.51.26736745.2%22%7D%2C%7B%22dealid%22%3A%2230654352%22%2C%22acm%22%3A%22AcategoryC5164586507100027312.50571500.52%22%2C%22dealacm%22%3A%22AcategoryC5164586507100027312.50571500.52.30654352.1%22%7D%2C%7B%22dealid%22%3A%2228146106%2C31175553%22%2C%22acm%22%3A%22AcategoryC5164586507100027312.42355449.53%22%2C%22dealacm%22%3A%22AcategoryC5164586507100027312.42355449.53.28146106.1%2CAcategoryC5164586507100027312.42355449.53.31175553.2%22%7D%2C%7B%22dealid%22%3A%2227130075%22%2C%22acm%22%3A%22AcategoryC5164586507100027312.5325634.54%22%2C%22dealacm%22%3A%22AcategoryC5164586507100027312.5325634.54.27130075.1%22%7D%2C%7B%22dealid%22%3A%226231076%2C30839016%22%2C%22acm%22%3A%22AcategoryC5164586507100027312.5137206.55%22%2C%22dealacm%22%3A%22AcategoryC5164586507100027312.5137206.55.6231076.1%2CAcategoryC5164586507100027312.5137206.55.30839016.2%22%7D%2C%7B%22dealid%22%3A%2225456954%22%2C%22acm%22%3A%22AcategoryC5164586507100027312.4438997.56%22%2C%22dealacm%22%3A%22AcategoryC5164586507100027312.4438997.56.25456954.1%22%7D%2C%7B%22dealid%22%3A%2225023503%2C25097392%2C29577640%22%2C%22acm%22%3A%22AcategoryC5164586507100027312.42399220.57%22%2C%22dealacm%22%3A%22AcategoryC5164586507100027312.42399220.57.25023503.1%2CAcategoryC5164586507100027312.42399220.57.25097392.2%2CAcategoryC5164586507100027312.42399220.57.29577640.3%22%7D%2C%7B%22dealid%22%3A%2230068448%2C30070347%22%2C%22acm%22%3A%22AcategoryC5164586507100027312.40440361.58%22%2C%22dealacm%22%3A%22AcategoryC5164586507100027312.40440361.58.30068448.1%2CAcategoryC5164586507100027312.40440361.58.30070347.2%22%7D%2C%7B%22dealid%22%3A%2227788792%2C30001973%22%2C%22acm%22%3A%22AcategoryC5164586507100027312.6231135.59%22%2C%22dealacm%22%3A%22AcategoryC5164586507100027312.6231135.59.27788792.1%2CAcategoryC5164586507100027312.6231135.59.30001973.2%22%7D%2C%7B%22dealid%22%3A%2229696740%22%2C%22acm%22%3A%22AcategoryC5164586507100027312.41337403.60%22%2C%22dealacm%22%3A%22AcategoryC5164586507100027312.41337403.60.29696740.1%22%7D%2C%7B%22dealid%22%3A%2230372513%2C30372305%2C30372511%22%2C%22acm%22%3A%22AcategoryC5164586507100027312.51034379.61%22%2C%22dealacm%22%3A%22AcategoryC5164586507100027312.51034379.61.30372513.1%2CAcategoryC5164586507100027312.51034379.61.30372305.2%2CAcategoryC5164586507100027312.51034379.61.30372511.3%22%7D%2C%7B%22dealid%22%3A%2227609116%2C27609353%22%2C%22acm%22%3A%22AcategoryC5164586507100027312.40578179.62%22%2C%22dealacm%22%3A%22AcategoryC5164586507100027312.40578179.62.27609116.1%2CAcategoryC5164586507100027312.40578179.62.27609353.2%22%7D%2C%7B%22dealid%22%3A%2226078838%2C26081007%22%2C%22acm%22%3A%22AcategoryC5164586507100027312.6736715.63%22%2C%22dealacm%22%3A%22AcategoryC5164586507100027312.6736715.63.26078838.1%2CAcategoryC5164586507100027312.6736715.63.26081007.2%22%7D%2C%7B%22dealid%22%3A%2230577019%22%2C%22acm%22%3A%22AcategoryC5164586507100027312.51761811.64%22%2C%22dealacm%22%3A%22AcategoryC5164586507100027312.51761811.64.30577019.1%22%7D%5D'
        headers = {
            'Host': 'nj.meituan.com',
            'User-Agent': 'Mozilla/5.0 (X11; Linux i586; rv:31.0) Gecko/20100101 Firefox/31.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Connection': 'keep-alive',
            'X-Requested-With': 'XMLHttpRequest',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Referer': 'http://nj.meituan.com/category/meishi?mtt=1.index%2Ffloornew.nc.1.ilvprxya',
            'Content-Length': len(data),
            'Cookie': 'uuid=5b737188f407f80ff402.1458747457.1.0.1; oc=Q7i8N7-FkttutAWbwPFexBkX4j-K1WnImPSucnYbe-GHZ9XkWfMEYaPguXmTHI2cLjeSEZz4lhyak_SCcDCejGzhECSjEjzeGcUGOX5-mzr_jF2m4gDxKxEnYdWqL2VaIijdx8uugpPRQlKmcjgK2yY8D9JFTYlQ6jvU51IU0b4; ci=55; abt=1458950159.0%7CACE; __mta=151911942.1458747461922.1458973229358.1458976966058.47; __utma=211559370.310281063.1458747462.1458973230.1458976966.12; __utmz=211559370.1458881460.4.2.utmcsr=baidu|utmccn=baidu|utmcmd=organic|utmctr=post%20content-length%20%E5%BF%85%E9%A1%BB%E8%AE%BE%E7%BD%AE%EF%BC%9F|utmcct=homepage; __utmv=211559370.|1=city=nj=1; _lx_utm=utm_source%3Dbaiduutm_medium%3Dorganicutm_term%3Dpost%2520content-length%2520%25E5%25BF%2585%25E9%25A1%25BB%25E8%25AE%25BE%25E7%25BD%25AE%25EF%25BC%259Futm_content%3Dhomepageutm_campaign%3Dbaidu; lsu=; ignore-zoom=true; __utmc=211559370; SID=2ekst2gpj11ebkm509vjg7a3l0; IJSESSIONID=4q67h19mp1bjajmi1irf041w; iuuid=FF8DC3A76A5CF86481933637D2A6A7C30F54502B1A72CEF9D9FA1C48E349C6C8; a2h=1; __utmb=211559370.1.10.1458976966'
        }
        #         """
        # Host: nj.meituan.com
        # User-Agent: Mozilla/5.0 (X11; Linux i586; rv:31.0) Gecko/20100101 Firefox/31.0
        # Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
        # Accept-Language: en-US,en;q=0.5
        # Accept-Encoding: gzip, deflate
        # X-Requested-With: XMLHttpRequest
        # Content-Type: application/x-www-form-urlencoded; charset=UTF-8
        # Referer: http://nj.meituan.com/category/meishi
        # Content-Length: 3990
        # Cookie: uuid=5b737188f407f80ff402.1458747457.1.0.1; oc=Q7i8N7-FkttutAWbwPFexBkX4j-K1WnImPSucnYbe-GHZ9XkWfMEYaPguXmTHI2cLjeSEZz4lhyak_SCcDCejGzhECSjEjzeGcUGOX5-mzr_jF2m4gDxKxEnYdWqL2VaIijdx8uugpPRQlKmcjgK2yY8D9JFTYlQ6jvU51IU0b4; ci=55; abt=1458950159.0%7CACE; __mta=151911942.1458747461922.1458979516585.1458979557040.51; __utma=211559370.310281063.1458747462.1458976966.1458979460.13; __utmz=211559370.1458881460.4.2.utmcsr=baidu|utmccn=baidu|utmcmd=organic|utmctr=post%20content-length%20%E5%BF%85%E9%A1%BB%E8%AE%BE%E7%BD%AE%EF%BC%9F|utmcct=homepage; __utmv=211559370.|1=city=nj=1; _lx_utm=utm_source%3Dbaiduutm_medium%3Dorganicutm_term%3Dpost%2520content-length%2520%25E5%25BF%2585%25E9%25A1%25BB%25E8%25AE%25BE%25E7%25BD%25AE%25EF%25BC%259Futm_content%3Dhomepageutm_campaign%3Dbaidu; lsu=; ignore-zoom=true; __utmc=211559370; SID=2ekst2gpj11ebkm509vjg7a3l0; IJSESSIONID=4q67h19mp1bjajmi1irf041w; iuuid=FF8DC3A76A5CF86481933637D2A6A7C30F54502B1A72CEF9D9FA1C48E349C6C8; a2h=1; __utmb=211559370.4.10.1458979460
        # Connection: keep-alive
        # """
        print "content-length", len(data)
        httpClient = None
        try:
            httpClient = httplib.HTTPConnection("nj.meituan.com", 80, timeout=10)
            httpClient.request("POST", aurl, data, headers)
            response = httpClient.getresponse()
            print response.status
            print response.reason
            print response.version
            print response.read()
            print response.getheaders() #获取头信息
            if response.status == 302:
                # headers["Cookie"] = response.getheader('set-cookie')
                httpClient.close()
                httpClient = httplib.HTTPConnection("nj.meituan.com", 80, timeout=30)
                response = httpClient.request('POST',response.getheader('location'), data, headers)
                print response.status
                print response.reason
                print response.version
                print response.read()
                print response.getheaders() #获取头信息
        except Exception, e:
            print e
        finally:
            if httpClient:
                httpClient.close()
        # res1 = requests.post(ajax_url, data=data, headers=headers)
        # print "history", res1.history,'\n'
        # if res1.history:
        #     for sel in res1.history:
        #         print sel.status_code,'\t', sel.url, '\n'
        #     print res1.content
        # # buf = StringIO(res1.content)
        # tmp = gzip.GzipFile(fileobj=buf)
        # print tmp.read()
        # with open("pagetmp.txt",'w') as wr:
        #     wr.write(res1.content)

        # request = urllib2.Request(url=ajax_url, data=data_encode)
        # request.add_header("Host", "nj.meituan.com")
        # request.add_header("User-Agent", "Mozilla/5.0 (X11; Linux i586; rv:31.0) Gecko/20100101 Firefox/31.0")
        # request.add_header("Accept", "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8")
        # request.add_header("Accept-Language", "en-US,en;q=0.5")
        # request.add_header("Connection", "keep-alive")
        # request.add_header("Accept-Encoding", "gzip, deflate")
        # request.add_header("X-Request-With", "XMLHttpRequest")
        # request.add_header("Content-Type", "application/x-www-form-urlencoded; charset=UTF-8")
        # request.add_header("Referer", refer)
        # request.add_header("Content-Length", len(data_encode))
        # request.add_header("Cookie", mcookie)
        #
        # f = urllib2.urlopen(request)
        # buf = StringIO(f.read())
        # tmp = gzip.GzipFile(fileobj=buf)
        # content = myencode(tmp.read())
        # html_parse = HTMLParser.HTMLParser()
        # page = html.fromstring(html_parse.unescape(content))
        # mlist = page.xpath('//div[@id="content"]//div[@class="J-scrollloader cf J-hub"]//a[@class="poi-tile__head"]/@href')
        # return mlist


        pass

    def getUrlAfterAjax(self, param, refer, mcookie):
        tmpparam = param.encode('utf-8')
        # tmpparam = tmpparam.replace('/','')
        # tmpparam = tmpparam.replace('\\', '')
        tmpparam = json.loads(tmpparam)
        data = json.loads(tmpparam['data'])
        poiidList = data['poiidList']
        poiData = data['poiData']

        self.getAjaxData(1, refer, poiidList, poiData, mcookie)
        # urlList = self.getAjaxData(1, refer, poiidList, poiData, mcookie)
        # tmplit = self.getAjaxData(2, refer, poiidList, poiData, mcookie)
        # for i in tmplit:
        #     if i not in urlList:
        #         urlList.append(i)
        # print len(urlList)
        # return urlList


if __name__ == '__main__':
    with open('../../salersFull.json','r') as rd:
        lines = rd.readlines()

    finalist = []
    for line in lines:
        if line not in finalist:
            finalist.append(line)
    print "个数：",len(finalist)
    # mlist = [1, 2, 3, 4]
    # print mlist[2:4]
    # tmp = AjaxSimulate()
    # tmp.getAjaxData('','','','','')
    # with open('../postonlineresp.txt','r') as rd:
    #     tmp = rd.read()
    # buf = StringIO(tmp)
    # tmp = gzip.GzipFile(fileobj=buf)
    # print tmp.read()

    pass



    # FIREBUG提取的数据
    # data = {
    #         'poiidLidt':"[2562728,41166727,6970061,5592284,6580346,41510157,6631370,4935526,50955292,5676128,40013263,42931715,6097441,5898129,5277401,41579428,41809805,41278178,3292746,50571500,42355449,5325634,5137206,4438997,42399220,40440361,6231135,41337403,51034379,40578179,6736715,51761811]",
    #         'bigImageMode':"true",
    #         'poiData': '[{"dealid":"29481902","acm":"AcategoryC2309194822229530182.2562728.33","dealacm":"AcategoryC2309194822229530182.2562728.33.29481902.1"},{"dealid":"31257476","acm":"AcategoryC2309194822229530182.41166727.34","dealacm":"AcategoryC2309194822229530182.41166727.34.31257476.1"},{"dealid":"27570297,27570418","acm":"AcategoryC2309194822229530182.6970061.35","dealacm":"AcategoryC2309194822229530182.6970061.35.27570297.1,AcategoryC2309194822229530182.6970061.35.27570418.2"},{"dealid":"27910937","acm":"AcategoryC2309194822229530182.5592284.36","dealacm":"AcategoryC2309194822229530182.5592284.36.27910937.1"},{"dealid":"26003443","acm":"AcategoryC2309194822229530182.6580346.37","dealacm":"AcategoryC2309194822229530182.6580346.37.26003443.1"},{"dealid":"27376235","acm":"AcategoryC2309194822229530182.41510157.38","dealacm":"AcategoryC2309194822229530182.41510157.38.27376235.1"},{"dealid":"2359713,7468690","acm":"AcategoryC2309194822229530182.6631370.39","dealacm":"AcategoryC2309194822229530182.6631370.39.2359713.1,AcategoryC2309194822229530182.6631370.39.7468690.2"},{"dealid":"27447577","acm":"AcategoryC2309194822229530182.4935526.40","dealacm":"AcategoryC2309194822229530182.4935526.40.27447577.1"},{"dealid":"31064064,31064047","acm":"AcategoryC2309194822229530182.50955292.41","dealacm":"AcategoryC2309194822229530182.50955292.41.31064064.1,AcategoryC2309194822229530182.50955292.41.31064047.2"},{"dealid":"25759031","acm":"AcategoryC2309194822229530182.5676128.42","dealacm":"AcategoryC2309194822229530182.5676128.42.25759031.1"},{"dealid":"28250453,28251032,28251017","acm":"AcategoryC2309194822229530182.40013263.43","dealacm":"AcategoryC2309194822229530182.40013263.43.28250453.1,AcategoryC2309194822229530182.40013263.43.28251032.2,AcategoryC2309194822229530182.40013263.43.28251017.3"},{"dealid":"30404633","acm":"AcategoryC2309194822229530182.42931715.44","dealacm":"AcategoryC2309194822229530182.42931715.44.30404633.1"},{"dealid":"24987788,29843978,25708067,31226682","acm":"AcategoryC2309194822229530182.6097441.45","dealacm":"AcategoryC2309194822229530182.6097441.45.24987788.1,AcategoryC2309194822229530182.6097441.45.29843978.2,AcategoryC2309194822229530182.6097441.45.25708067.3,AcategoryC2309194822229530182.6097441.45.31226682.4"},{"dealid":"26955143","acm":"AcategoryC2309194822229530182.5898129.46","dealacm":"AcategoryC2309194822229530182.5898129.46.26955143.1"},{"dealid":"26359978","acm":"AcategoryC2309194822229530182.5277401.47","dealacm":"AcategoryC2309194822229530182.5277401.47.26359978.1"},{"dealid":"26851507","acm":"AcategoryC2309194822229530182.41579428.48","dealacm":"AcategoryC2309194822229530182.41579428.48.26851507.1"},{"dealid":"27408489,27766049,27765802","acm":"AcategoryC2309194822229530182.41809805.49","dealacm":"AcategoryC2309194822229530182.41809805.49.27408489.1,AcategoryC2309194822229530182.41809805.49.27766049.2,AcategoryC2309194822229530182.41809805.49.27765802.3"},{"dealid":"30269951","acm":"AcategoryC2309194822229530182.41278178.50","dealacm":"AcategoryC2309194822229530182.41278178.50.30269951.1"},{"dealid":"26736921,26736745","acm":"AcategoryC2309194822229530182.3292746.51","dealacm":"AcategoryC2309194822229530182.3292746.51.26736921.1,AcategoryC2309194822229530182.3292746.51.26736745.2"},{"dealid":"30654352","acm":"AcategoryC2309194822229530182.50571500.52","dealacm":"AcategoryC2309194822229530182.50571500.52.30654352.1"},{"dealid":"28146106,31175553","acm":"AcategoryC2309194822229530182.42355449.53","dealacm":"AcategoryC2309194822229530182.42355449.53.28146106.1,AcategoryC2309194822229530182.42355449.53.31175553.2"},{"dealid":"27130075","acm":"AcategoryC2309194822229530182.5325634.54","dealacm":"AcategoryC2309194822229530182.5325634.54.27130075.1"},{"dealid":"6231076,30839016","acm":"AcategoryC2309194822229530182.5137206.55","dealacm":"AcategoryC2309194822229530182.5137206.55.6231076.1,AcategoryC2309194822229530182.5137206.55.30839016.2"},{"dealid":"25456954","acm":"AcategoryC2309194822229530182.4438997.56","dealacm":"AcategoryC2309194822229530182.4438997.56.25456954.1"},{"dealid":"25023503,25097392,29577640","acm":"AcategoryC2309194822229530182.42399220.57","dealacm":"AcategoryC2309194822229530182.42399220.57.25023503.1,AcategoryC2309194822229530182.42399220.57.25097392.2,AcategoryC2309194822229530182.42399220.57.29577640.3"},{"dealid":"30068448,30070347","acm":"AcategoryC2309194822229530182.40440361.58","dealacm":"AcategoryC2309194822229530182.40440361.58.30068448.1,AcategoryC2309194822229530182.40440361.58.30070347.2"},{"dealid":"27788792,30001973","acm":"AcategoryC2309194822229530182.6231135.59","dealacm":"AcategoryC2309194822229530182.6231135.59.27788792.1,AcategoryC2309194822229530182.6231135.59.30001973.2"},{"dealid":"29696740","acm":"AcategoryC2309194822229530182.41337403.60","dealacm":"AcategoryC2309194822229530182.41337403.60.29696740.1"},{"dealid":"30372513,30372305,30372511","acm":"AcategoryC2309194822229530182.51034379.61","dealacm":"AcategoryC2309194822229530182.51034379.61.30372513.1,AcategoryC2309194822229530182.51034379.61.30372305.2,AcategoryC2309194822229530182.51034379.61.30372511.3"},{"dealid":"27609116,27609353","acm":"AcategoryC2309194822229530182.40578179.62","dealacm":"AcategoryC2309194822229530182.40578179.62.27609116.1,AcategoryC2309194822229530182.40578179.62.27609353.2"},{"dealid":"26078838,26081007","acm":"AcategoryC2309194822229530182.6736715.63","dealacm":"AcategoryC2309194822229530182.6736715.63.26078838.1,AcategoryC2309194822229530182.6736715.63.26081007.2"},{"dealid":"30577019","acm":"AcategoryC2309194822229530182.51761811.64","dealacm":"AcategoryC2309194822229530182.51761811.64.30577019.1"}]'
    # }
    # print "data_len:" , len(urllib.urlencode(data))
    # mcookie = 'uuid=5b737188f407f80ff402.1458747457.1.0.1; oc=Q7i8N7-FkttutAWbwPFexBkX4j-K1WnImPSucnYbe-GHZ9XkWfMEYaPguXmTHI2cLjeSEZz4lhyak_SCcDCejGzhECSjEjzeGcUGOX5-mzr_jF2m4gDxKxEnYdWqL2VaIijdx8uugpPRQlKmcjgK2yY8D9JFTYlQ6jvU51IU0b4; ci=55; abt=1458950159.0%7CACE; __mta=151911942.1458747461922.1458950160368.1458950163134.37; __utma=211559370.310281063.1458747462.1458915735.1458950160.9; __utmz=211559370.1458881460.4.2.utmcsr=baidu|utmccn=baidu|utmcmd=organic|utmctr=post%20content-length%20%E5%BF%85%E9%A1%BB%E8%AE%BE%E7%BD%AE%EF%BC%9F|utmcct=homepage; __utmv=211559370.|1=city=nj=1; _lx_utm=utm_source%3Dbaiduutm_medium%3Dorganicutm_term%3Dpost%2520content-length%2520%25E5%25BF%2585%25E9%25A1%25BB%25E8%25AE%25BE%25E7%25BD%25AE%25EF%25BC%259Futm_content%3Dhomepageutm_campaign%3Dbaidu; stick-qrcode=1; lsu=; ignore-zoom=true; __utmc=211559370; SID=2ekst2gpj11ebkm509vjg7a3l0; __utmb=211559370.2.10.1458950160'