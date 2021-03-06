# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='product-info model']",
    'price' : "//span[@class='uc-price-product uc-price-sell uc-price']",
    'category' : "//div[@class='breadcrumb']/a",
    'description' : "//div[@class='product-body']/p",
    'images' : "//div[@class='product-image']/div/a/@href",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'vnsupermark.com'
allowed_domains = ['vnsupermark.com']
start_urls = ['http://www.vnsupermark.com']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(), 'parse_item'),
    Rule(LinkExtractor(), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
