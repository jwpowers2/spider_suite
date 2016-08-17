
# scientificlinux.org spider

import scrapy
from items import ScientificLinuxItem


class ScientificLinuxSpider(scrapy.Spider):

    name = "scientificlinux"
    allowed_domains = ["scientificlinux.org"]
    start_urls = ["https://www.scientificlinux.org"]
    custom_settings = {'ITEM_PIPELINES': {'scientificlinux_pipeline.ScientificLinuxPipeline':700}}

    def parse(self, response):

        item = ScientificLinuxItem()
        item['news'] = response.xpath('//div[@class="entry-content"]/p/text()').extract()
        yield item
