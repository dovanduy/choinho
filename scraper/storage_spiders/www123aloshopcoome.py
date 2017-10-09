# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//h1[@class='np_pdtitle']",
    'price' : "//div[@class='np_pdprice']",
    'category' : "",
    'description' : "",
    'images' : "//div[@class='np_pdimg']/img/@src",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = '123aloshop.coo.me'
allowed_domains = ['123aloshop.coo.me']
start_urls = ['http://www.123aloshop.coo.me/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/[a-zA-Z0-9-]+-i5-\d+\.html$']), 'parse_item'),
    Rule(LinkExtractor(allow=['/[a-zA-Z0-9-]+-i1-\d+\.html']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]