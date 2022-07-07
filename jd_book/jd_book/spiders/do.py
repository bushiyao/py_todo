# coding=utf-8
# @Time : 2022/7/6 19:09 
# @Author : hh
# @File : do.py 
# @Software: PyCharm

#导包
import scrapy
import os, json
from scrapy_redis.spiders import RedisSpider
from scrapy import Request

#定义抓取类
#class Test(scrapy.Spider):
class Test(RedisSpider):

    #定义爬虫名称，和命令行运行时的名称吻合
    name = "test"

    #定义redis的key
    redis_key = 'test:start_urls'

    #定义头部信息
    haders = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/73.0.3683.86 Chrome/73.0.3683.86 Safari/537.36'
    }

    def start_requests(self):
        task = {
            "url": "https://www.baidu.com",  # 当前任务需要请求的地址。必须
            "callback": "parse1",  # 指定当前任务的处理函数(函数名)。默认 parse
            "page": "1",  # 当前页码
            # "proxy": "http://redis:1087"    # 当前请求否使用代理, 代理地址是：http://proxy_host:proxy_port 这样的
        }
        yield self.make_requests_from_url(task)

    def make_requests_from_url(self, item):
        # item = {"url": "", "task_name": ""}
        # item = json.loads(item)
        if not isinstance(item, dict):
            item = json.loads(item)

        # realUrl = 'http://www.baidu.com'
        print("\nrealUrl: ", item['url'])
        print(item)
        realUrl = item['url']
        return scrapy.Request(url=realUrl,
                              callback=self.parse1,
                              meta={'task_item': item},
                              dont_filter=True
                              )

    # def start_requests(self):
    #     yield Request(
    #         'http://www.baidu.com',
    #         dont_filter=True,
    #         callback=self.parse1
    #     )

    def parse1(self, response):
        print("\n ---------------")
        print(response.url)
        pass