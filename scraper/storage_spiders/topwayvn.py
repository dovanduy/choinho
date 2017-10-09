# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='product-name']/h1/span",
    'price' : "//div[@class='details-product-price']/span",
    'category' : "//ul[@class='list-inline list-unstyled']/li/a",
    'description' : "//div[@class='product-description']",
    'images' : "//div[@class='single-product-gallery-item']/a/@href",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'topway.vn'
allowed_domains = ['topway.vn']
start_urls = ['http://topway.vn/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(), 'parse_item'),
    Rule(LinkExtractor(), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
