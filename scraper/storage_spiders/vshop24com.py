# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='product-detail-wrap clearfix']/h1",
    'price' : "//div[@class='product-detail']/div[@class='prod_price']/span",
    'category' : "",
    'description' : "",
    'images' : "//div[@class='product-image']/a/@href",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'vshop24.com'
allowed_domains = ['vshop24.com']
start_urls = ['http://vshop24.com']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/product/']), 'parse_item'),
    Rule(LinkExtractor(allow=['/category/']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
