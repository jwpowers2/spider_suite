# python.org spider

import scrapy
from items import PythonItem


class PythonSpider(scrapy.Spider):

    name = "python"
    allowed_domains = ["python.org"]
    start_urls = ["https://www.python.org"]
    custom_settings = {'ITEM_PIPELINES': {'python_pipeline.PythonPipeline':700}}

    def parse(self, response):

        item = PythonItem()
        item['news'] = response.xpath('//ul[@class="menu"]//text()').extract()
        yield item

