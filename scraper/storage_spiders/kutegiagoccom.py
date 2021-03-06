# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='detail_content']/h1[@id='detail_name']",
    'price' : "//div[@id='detail']/ul[@class='info_panel']/li/p[@id='price']",
    'category' : "//ul[@id='breadcrumb']/li/a",
    'description' : "//div[@id='detail_content']/div",
    'images' : "//div[@id='detail_content']/div//img/@src",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'kutegiagoc.com'
allowed_domains = ['kutegiagoc.com']
start_urls = ['http://kutegiagoc.com']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(), 'parse_item'),
    Rule(LinkExtractor(), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
