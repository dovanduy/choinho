# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//table[2]/tbody/tr[1]/td/b",
    'price' : "//p[@class='price']/font",
    'category' : "",
    'description' : "",
    'images' : "//div/img/@src",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'thegioihoaviet.com'
allowed_domains = ['thegioihoaviet.com']
start_urls = ['http://thegioihoaviet.com/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(), 'parse_item'),
    Rule(LinkExtractor(), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
