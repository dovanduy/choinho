# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='main-content']/div[@class='row product-detai']/div[@class='product-meta']/h1",
    'price' : "//div[@class='product-meta']/div[@class='meta meta-price']/span[@class='price']/span|//div[@class='product-meta']/span[@class='bl price']/span[@itemprop='price']",
    'category' : "",
    'description' : "//div[@class='main-content']/div[@class='row product-content']",
    'images' : "//div[@class='row product-detai']/div[@class='product-image']/img/@src",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'dongtay.vn'
allowed_domains = ['dongtay.vn']
start_urls = ['http://dongtay.vn']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/san-pham/\d+/']), 'parse_item'),
    Rule(LinkExtractor(allow=['/danh-muc/\d+']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
