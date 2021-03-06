# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//h1[@class='proDetail'] | //div[@class='home-content-temp2']/h1[@class='proDetail']",
    'price' : "//div[@class='proDetail-price']",
    'category' : "//div[@class='proDetail-cate']/a",
    'description' : "//div[@class='proDetail-summary']/div",
    'images' : "//div[@class='proDetail-img']/div/a/img/@src",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'vncomputers.net'
allowed_domains = ['vncomputers.net']
start_urls = ['http://vncomputers.net/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/p+\d+\.html']), 'parse_item'),
    Rule(LinkExtractor(allow=['/c+\d+\.html']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
