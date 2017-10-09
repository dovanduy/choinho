# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='product-info']/h1",
    'price' : "//div[@class='product-info']/p[@class='info-item']/span[@class='price']",
    'category' : "",
    'description' : "//div[@class='products']/div[@class='product-description'][1]",
    'images' : "//img[@class='featured-image']/@src",
    'canonical' : "//link[@rel='canonical']/@href",
    'base_url' : "",
    'brand' : "//div[@class='product-info']/p[@class='info-item']/span[@class='vendor']",
    'in_stock' : "",
    'guarantee' : ""
}
name = 'thefaceshop.com.vn'
allowed_domains = ['thefaceshop.com.vn']
start_urls = ['http://www.thefaceshop.com.vn/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = ['']
rules = [
    Rule(LinkExtractor(allow=['/products/[\w-]+$']), 'parse_item'),
    Rule(LinkExtractor(allow=['/collections/[\w-]+($|\?page=\d+$)']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]