# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from .utils import insert_mxc_market_tickers


class ScrapyPipeline:
    def process_item(self, item, spider):
        return item

class MxcPipeline:
    def process_item(self, item, spider):
        results = insert_mxc_market_tickers(item['data'])
        return item