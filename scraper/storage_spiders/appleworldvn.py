# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='tensp']/a",
    'price' : "//span[@class='gia']",
    'category' : "//table//tr/td/div[@class='header']/a",
    'description' : "//table//tr/td/div[@id='tabs']/div[@id='tabs-1']",
    'images' : "//a[@id='thumb1']/img/@src",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'appleworld.vn'
allowed_domains = ['appleworld.vn']
start_urls = ['http://appleworld.vn']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/vi/spct/']), 'parse_item'),
    Rule(LinkExtractor(allow=['/vi/spds/']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
