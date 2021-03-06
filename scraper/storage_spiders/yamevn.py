# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='col-md-6']/div[@class='ditem']/h4",
    'price' : "//div[@class='ditem']/h5[@class='price']",
    'category' : "//ol[@class='breadcrumb']/li/a",
    'description' : "",
    'images' : "//div[@class='col-md-4']/img[@class='img-responsive']/@src",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'yame.vn'
allowed_domains = ['yame.vn']
start_urls = ['http://yame.vn']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/shop/[a-zA-Z0-9-]+/[a-zA-Z0-9-]+-\d+\?']), 'parse_item'),
    Rule(LinkExtractor(allow=['/shop/[a-zA-Z-]+($|\?page)']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
