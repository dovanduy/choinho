# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='product-name']/h1",
    'price' : "//div[@class='price-box']/span[@class='regular-price']/span[@class='price']",
    'category' : "//div[@class='breadcrumbs']/ul/li/a/span",
    'description' : "//div[@class='product-view']/div[@class='product-collateral']",
    'images' : "//div[@class='more-views']/ul/li/a/@href",
    'canonical' : "//link[@rel='canonical']/@href",
    'base_url' : "",
    'brand' : ""
}
name = 'eropi.com'
allowed_domains = ['eropi.com']
start_urls = ['http://eropi.com/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/[a-zA-Z0-9-]+\.html$']), 'parse_item'),
    Rule(LinkExtractor(allow=['/[a-zA-Z-]+\.html$']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
