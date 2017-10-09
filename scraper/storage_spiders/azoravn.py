# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='product-name']/h1",
    'price' : "//p[@class='special-price']/span[@class='price']|//span[@class='regular-price']/span[@class='price']",
    'category' : "//div[@class='breadcrumbs']/ul/li/a",
    'description' : "//div[@class='box-collateral box-description']/div[@id='details-area']",
    'images' : "//p[@class='product-image']/a/@href",
    'canonical' : "",
    'base_url' : "",
    'brand' : "",
    'in_stock' : "",
    'guarantee' : "",
    'promotion' : ""
}
name = 'azora.vn'
allowed_domains = ['azora.vn']
start_urls = ['http://azora.vn/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = ['']
rules = [
    #Rule(LinkExtractor(), 'parse_item'),
    #Rule(LinkExtractor(), 'parse'),
    Rule(LinkExtractor(allow=['/[a-zA-Z0-9-]+\.html($|\?p=\d+$)']), 'parse_item_and_links'),
]
