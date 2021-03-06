# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div/div[@class='bodyProductDetail first']/h1",
    'price' : "//div[@class='priceProductDetail']/div[@class='wPrice']/p",
    'category' : "//ul[@class='breadcrumb hidden-sm hidden-xs']/li/a",
    'description' : "//div[@id='realDetail']/div",
    'images' : "//ul[@class='bxslider']/li/img/@src",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'mox.vn'
allowed_domains = ['mox.vn']
start_urls = ['http://www.mox.vn/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/[a-zA-Z0-9-]+-\d+\.html']), 'parse_item'),
    Rule(LinkExtractor(allow=['/[a-zA-Z0-9-]+/']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
