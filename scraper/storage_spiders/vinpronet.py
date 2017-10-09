# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='breadcrumbs']/ul/li[@class='product']/strong",
    'price' : "//div[@class='col-main']/div/div//span[@class='price']",
    'category' : "//div[@class='breadcrumbs']/ul/li/a",
    'description' : "//div[@class='container']/div[@id='tab-1']",
    'images' : "//div[@id='gallery']/div[@id='menu']/ul/li/a/img/@src | //div[@id='gallery']/div[@id='slides']//img/@src",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'vinpro.net'
allowed_domains = ['vinpro.net']
start_urls = ['http://vinpro.net/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = ['']
rules = [
    #Rule(LinkExtractor(), 'parse_item'),
    #Rule(LinkExtractor(), 'parse'),
    Rule(LinkExtractor(allow=['\.html']), 'parse_item_and_links'),
]
