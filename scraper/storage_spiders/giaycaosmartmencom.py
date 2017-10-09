# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='product-name']/h1",
    'price' : "//p[@class='special-price']/span[@class='price2']",
    'category' : "",
    'description' : "//div[@itemprop='description']",
    'images' : "//div[@class='thumb']/li/img/@class",
    'canonical' : "//link[@rel='canonical']/@href",
    'base_url' : "",
    'brand' : "",
    'in_stock' : "",
    'guarantee' : "",
    'promotion' : ""
}
name = 'giaycaosmartmen.com'
allowed_domains = ['giaycaosmartmen.com']
start_urls = ['http://giaycaosmartmen.com/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = ['']
rules = [
    #Rule(LinkExtractor(), 'parse_item'),
    #Rule(LinkExtractor(), 'parse'),
    Rule(LinkExtractor(allow=['/[a-zA-Z0-9-]+$']), 'parse_item_and_links'),
]
