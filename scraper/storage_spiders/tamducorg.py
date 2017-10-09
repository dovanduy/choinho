# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//title",
    'price' : "//tr[2]/td/font/strong | //font[@color='#FF0000']/strong",
    'category' : "",
    'description' : "//tr[2]/td/p/span",
    'images' : "//table//tr[1]/td/a/img/@src",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'tamduc.org'
allowed_domains = ['tamduc.org']
start_urls = ['http://tamduc.org']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/Product/']), 'parse_item'),
    Rule(LinkExtractor(allow=['/listProduct/']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]