# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='product-name']/h1",
    'price' : "//div[@class='product-shop']/div[@class='price-box']/span[@class='regular-price']/span[@class='price']",
    'category' : "//div[@class='breadcrumbs container']/ul/li/a",
    'description' : "//div[@class='short-description']/div[@class='std']",
    'images' : "//img[@id='product-image']/@src",
    'canonical' : "//link[@rel='canonical']/@href",
    'base_url' : "",
    'brand' : ""
}
name = 'beautyzone.vn'
allowed_domains = ['beautyzone.vn']
start_urls = ['http://beautyzone.vn/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/[a-zA-Z0-9-]+-\d+\.html$']), 'parse_item'),
    Rule(LinkExtractor(allow=['/[a-zA-Z0-9-]+\.html$']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
