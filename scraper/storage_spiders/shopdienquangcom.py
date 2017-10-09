# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//h1[@class='mainbox-title']",
    'price' : "//span[@class='price']/span[@class='price-num']",
    'category' : "//div[@class='breadcrumbs clearfix']/a",
    'description' : "//div[@class='product-main-info']/div[@class='cm-tabs-content tabs-content clearfix']",
    'images' : "//img[@class='   pict']/@src",
    'canonical' : "//link[@rel='canonical']/@href",
    'base_url' : "//base/@href",
    'brand' : ""
}
name = 'shop.dienquang.com'
allowed_domains = ['shop.dienquang.com']
start_urls = ['http://shop.dienquang.com/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    #Rule(LinkExtractor(), 'parse_item'),
    #Rule(LinkExtractor(), 'parse'),
    Rule(LinkExtractor(allow=['/product/']), 'parse_item_and_links'),
]