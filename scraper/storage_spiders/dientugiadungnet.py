# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='_p_header']/h3[@class='p-label']",
    'price' : "//div[@class='_p_info']/p[@class='price']/span | //div[@class='_p_info']/p[@class='price-old']/span",
    'category' : "//div[@id='middle']/div[@id='page-name']/ul[@id='sys_pagename']/li/span",
    'description' : "//div[@class='p-longtext']",
    'images' : "//div[@class='_p_image']/ul//img/@src",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'dientugiadung.net'
allowed_domains = ['dientugiadung.net']
start_urls = ['http://dientugiadung.net']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/chi-tiet/']), 'parse_item'),
    Rule(LinkExtractor(allow=['/danh-muc/']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
