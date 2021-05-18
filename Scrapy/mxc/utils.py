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
PROD_ENV = 'PROD_ENV'
DB_NAME = 'mxc'
TB_MARKET_TICKERS = 'market_tickers'

# conf
if os.environ.get(PROD_ENV):
    u = parse.quote_plus(os.environ.get(USER_ENV))
    p = parse.quote_plus(os.environ.get(PW_ENV))
    host = parse.quote_plus(os.environ.get(HOST_ENV))
    db_url = f'mongodb://{u}:{p}@{host}:27017/'
else:
    u = parse.quote_plus(DB_NAME)
    p = parse.quote_plus(DB_NAME)
    db_url = f'mongodb://{u}:{p}@localhost:27018/'


# initialize
client = pymongo.MongoClient(db_url)
db = client[DB_NAME]


def insert_mxc_market_tickers(data):
    tb = db[TB_MARKET_TICKERS]
    result_insert = tb.insert_many(data)
    logger.info(f"insert {len(data)} records")
    return result_insert