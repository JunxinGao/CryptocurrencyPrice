# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import copy
from .utils import insert_mxc_market_tickers


class MxcPipeline:
    def process_item(self, item, spider):
        spider.logger.info(f"start insert {len(item['data'])} to mongodb")
        results = insert_mxc_market_tickers(copy.deepcopy(item['data']))
        spider.logger.info(f"insert end")
        return item