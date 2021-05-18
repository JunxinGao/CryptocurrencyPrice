'''
File: utils.py
Project: Scrapy
Created Date: Friday 14th May 2021
Author: Junxin Gao
Copyright (c) 2021 Junxin Gao
'''
import os
import pymongo
from loguru import logger
from urllib import parse

# const
USER_ENV = 'MONGO_INITDB_ROOT_USERNAME'
PW_ENV = 'MONGO_INITDB_ROOT_PASSWORD'
HOST_ENV = 'MONGO_INITDB_ROOT_HOST'
PORT_ENV = 'MONGO_INITDB_ROOT_PORT'
PROD_ENV = 'PROD_ENV'
DB_NAME = 'mxc'
TB_MARKET_TICKERS = 'market_tickers'

# conf
u = parse.quote_plus(os.environ.get(USER_ENV))
p = parse.quote_plus(os.environ.get(PW_ENV))
host = parse.quote_plus(os.environ.get(HOST_ENV))
port = parse.quote_plus(os.environ.get(PORT_ENV))
db_url = f'mongodb://{u}:{p}@{host}:{port}/'


# initialize
client = pymongo.MongoClient(db_url)
db = client[DB_NAME]


def insert_mxc_market_tickers(data):
    tb = db[TB_MARKET_TICKERS]
    result_insert = tb.insert_many(data)
    logger.info(f"insert {len(data)} records")
    return result_insert