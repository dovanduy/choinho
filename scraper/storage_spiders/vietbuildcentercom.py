# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='center']/h1",
    'price' : "//div[@class='price-default']",
    'category' : "//div[@class='center']/a",
    'description' : "//div[@id='tab-description']",
    'images' : "//section[@class='product-info']//div/a/@href",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'vietbuildcenter.com'
allowed_domains = ['vietbuildcenter.com']
start_urls = ['http://vietbuildcenter.com/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(), 'parse_item'),
    Rule(LinkExtractor(), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
