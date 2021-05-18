import scrapy
import json
from loguru import logger
import datetime
import pandas as pd
from ..items import MxcMarketTickerDataItem


class MxcSpider(scrapy.Spider):
    name = 'mxc'
    allowed_domains = ['mxc.com']
    url = 'https://www.mxc.com/open/api/v2/market/ticker'

    def start_requests(self):
        self.logger.info(f"start request: {self.url}")
        yield scrapy.Request(
            self.url,
            method='GET',
            callback=self.parse
        )
        self.logger.info(f"end request: {self.url}")

    def parse(self, response):
        body = json.loads(response.body.decode())
        code = body['code']
        data = body['data']
        self.logger.info(f"http status: {code}, data length: {len(data)}")
        assert code == 200
        # pd.DataFrame(data).to_csv(f"{str(int(datetime.datetime.now().timestamp()))}.csv", index=False)
        yield MxcMarketTickerDataItem(data=data)
