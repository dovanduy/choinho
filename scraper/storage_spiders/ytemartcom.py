# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//h1",
    'price' : "//div[@class='prices-and-button']/p[@class='prices pull-left']/span[@class='price']",
    'category' : "//h1",
    'description' : "//div[@class='product-specification']",
    'images' : "//a[@class='jqzoom']/div/img/@src",
    'canonical' : "",
    'base_url' : "//base/@href",
    'brand' : ""
}
name = 'ytemart.com'
allowed_domains = ['ytemart.com']
start_urls = ['http://ytemart.com/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/vn/[a-zA-Z0-9-]+-\d+\.html$']), 'parse_item'),
    Rule(LinkExtractor(allow=['/vn/san-pham/[a-zA-Z0-9-]+']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
