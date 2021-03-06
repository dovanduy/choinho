# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='spct']/div[@class='product-info']/h1",
    'price' : "//div[@class='product-info']/div[@class='product-price']/p",
    'category' : "//div[@class='rdfa-breadcrumb']/div/p/span/a",
    'description' : "//div[@id='mContent']/div[@class='San_pham_chi_tiet'][2] | //div[@id='mContent']/div[@class='San_pham_chi_tiet'][2]/p/img[@class='aligncenter']/@src",
    'images' : "//div[@class='view-big']/img/@src",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'baodaipad.vn'
allowed_domains = ['baodaipad.vn']
start_urls = ['http://baodaipad.vn']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/\d+-[a-zA-Z0-9-_]+$']), 'parse_item'),
    Rule(LinkExtractor(allow=['/[a-zA-Z0-9-]+$']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
