# -*- coding: utf-8 -*-
import scrapy


class SpecialOfferSpider(scrapy.Spider):
    name = 'special_offer'
    allowed_domains = ['www.cigabuy.com/consumer-electronics-c-56_75-pg-1.html']
    start_urls = ['http://www.cigabuy.com/consumer-electronics-c-56_75-pg-1.html/']

    def parse(self, response):
        pass
