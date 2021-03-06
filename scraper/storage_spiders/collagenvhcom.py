# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='single']/div[@class='ct spshow']/h1",
    'price' : "//div[@class='tab_container khung']/div[@id='bc']/p[6]/span/strong",
    'category' : "//div[@class='main']/div[@class='bre']/a",
    'description' : "//div[@class='entry']/div/div[@class='tab_container khung']",
    'images' : "//div[@class='entry']/div[@class='mtbl showsp']/ul/li/a/img/@src",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'collagenvh.com'
allowed_domains = ['collagenvh.com']
start_urls = ['http://collagenvh.com']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(), 'parse_item'),
    Rule(LinkExtractor(), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
