# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='product-title']/h1",
    'price' : "//div[@class='product-price']/span",
    'category' : "",
    'description' : "//div[@id='mota']",
    'images' : "//div[@class='img-product']/img/@src",
    'canonical' : "//link[@rel='canonical']/@href",
    'base_url' : "",
    'brand' : ""
}
name = 'gheluoi.com'
allowed_domains = ['gheluoi.com']
start_urls = ['http://gheluoi.com/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = ['']
rules = [
    Rule(LinkExtractor(allow=['/products/']), 'parse_item'),
    Rule(LinkExtractor(allow=['/collections/[a-zA-Z0-9-]+($|\?page=\d+$)']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]