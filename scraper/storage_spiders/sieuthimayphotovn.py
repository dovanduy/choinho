# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//h1",
    'price' : "//div[@class='span6 product-shop']/div[@class='price']/text()",
    'category' : "",
    'description' : "//div[@class='wrap-product']/div[@class='wrap-tabs']/div[@class='tab-content']",
    'images' : "//div[@class='item']/a/@href",
    'canonical' : "//link[@rel='canonical']/@href",
    'base_url' : "//base/@href",
    'brand' : "//div[@class='span6 product-shop']/div[@class='description']/a",
    'in_stock' : "",
    'guarantee' : ""
}
name = 'sieuthimayphoto.vn'
allowed_domains = ['sieuthimayphoto.vn']
start_urls = ['http://sieuthimayphoto.vn/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = ['']
rules = [
    #Rule(LinkExtractor(), 'parse_item'),
    #Rule(LinkExtractor(), 'parse'),
    Rule(LinkExtractor(allow=['/[a-zA-Z0-9-]+($|\?page=\d+$)']), 'parse_item_and_links'),
]