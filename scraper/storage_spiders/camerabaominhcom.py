# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='product-detail']/div[@class='product-detail-right']/h1",
    'price' : "//div[@class='product-price-pomotion']/p[@class='price']",
    'category' : "//div[@class='product-category-path']/ul/li/a",
    'description' : "",
    'images' : "//div[@class='extra_details']/div[@id='gallery']/img/@src",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'camerabaominh.com'
allowed_domains = ['camerabaominh.com']
start_urls = ['http://camerabaominh.com']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(), 'parse_item'),
    Rule(LinkExtractor(), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
