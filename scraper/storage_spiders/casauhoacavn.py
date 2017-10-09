# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//h1[@class='heading-title']/span",
    'price' : "//span[@class='new_price']",
    'category' : "//div[@class='breadcrumb']/a",
    'description' : "//div[@class='box'][1]",
    'images' : "//div[@class='image']//a/@href",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'casauhoaca.vn'
allowed_domains = ['casauhoaca.vn']
start_urls = ['http://www.casauhoaca.vn']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(), 'parse_item'),
    Rule(LinkExtractor(), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
