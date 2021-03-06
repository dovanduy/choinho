# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@id='san-pham']/h1[@class='title']/a",
    'price' : "//div[@class='info']/div[@class='price-info']",
    'category' : "",
    'description' : "",
    'images' : "//div[@id='san-pham']/div[@class='img']/img/@src",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'cauvong.net'
allowed_domains = ['cauvong.net']
start_urls = ['http://cauvong.net']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/san-pham/']), 'parse_item'),
    Rule(LinkExtractor(allow=['/danh-muc/']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
