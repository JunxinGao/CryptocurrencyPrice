#!/bin/bash
cp -rf ../Scrapy scrapyd/
docker-compose build
rm -rf scrapyd/Scrapy
