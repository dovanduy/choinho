# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='header-for-light']/h3",
    'price' : "//div[@class='clearfix text-center']/p[@class='product-price']/text()",
    'category' : "",
    'description' : "//div[@class='panel-collapse collapse in']/div[@class='panel-body']",
    'images' : "//div[@class='product-image']/img[@id='product-zoom']/@src",
    'canonical' : "//link[@rel='canonical']/@href",
    'base_url' : "",
    'brand' : "",
    'in_stock' : "",
    'guarantee' : "",
    'promotion' : ""
}
name = 'reginashop.vn'
allowed_domains = ['reginashop.vn']
start_urls = ['http://reginashop.vn/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = ['']
rules = [
    #Rule(LinkExtractor(), 'parse_item'),
    #Rule(LinkExtractor(), 'parse'),
    Rule(LinkExtractor(allow=['/[a-zA-Z0-9-]+($|\?page=\d+$)']), 'parse_item_and_links'),
]
