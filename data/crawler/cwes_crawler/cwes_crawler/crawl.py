import scrapy
from scrapy.crawler import CrawlerProcess
from spiders.cwe_spider import *

process = CrawlerProcess()
process.crawl(CWESpider)

process.start()
