# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//title",
    'price' : "//div[@class='prices']/div",
    'category' : "",
    'description' : "//div[@class='fr rel']/div[@id='desProduct']",
    'images' : "//img[@id='imgMainProduct']/@src",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'moriitalia.com'
allowed_domains = ['moriitalia.com']
start_urls = ['http://moriitalia.com/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/san-pham/']), 'parse_item'),
    Rule(LinkExtractor(allow=['/\.*']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
