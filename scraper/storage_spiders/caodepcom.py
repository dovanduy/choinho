# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='center breadcrumb']/h1",
    'price' : "//div[@class='product-info']/div[@class='right']/div[@class='price']/span[@class='price-old'] | //div[@class='product-info']/div[@class='right']/div[@class='price']/span[@class='price-new']",
    'category' : "//div[@class='center breadcrumb']/div/a",
    'description' : "//div[@class='column']/div[@id='tab-description']/p",
    'images' : "//div[@class='image']/a/img/@src | //div[@class='image-additional']/a/img/@src",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'caodep.com'
allowed_domains = ['caodep.com']
start_urls = ['http://caodep.com']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/product']), 'parse_item'),
    Rule(LinkExtractor(allow=['route=product//category']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
