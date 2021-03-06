# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//td[@class='title16']/strong",
    'price' : "//td[@class='brd_bott'][2]/span[@class='fontred']",
    'category' : "//td[@class='title']/a",
    'description' : "//div[@id='dog1']",
    'images' : "//img[@width='180']/@src",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'congnghesovn.net'
allowed_domains = ['congnghesovn.net']
start_urls = ['http://congnghesovn.net']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['prodetail-']), 'parse_item'),
    Rule(LinkExtractor(allow=['/\d+-\d+']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
