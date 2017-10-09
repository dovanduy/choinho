# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='detail']/h1[@class='name']",
    'price' : "//div[@class='l-price']/p[@id='box_price_available']/span[2]",
    'category' : "/ul[@class='breadcrumb-nav clearfix']/li/a/span",
    'description' : "//div[@class='left']/div[@id='tab1']",
    'images' : "//li[@class='image-nav-item']/span/@id",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'dambao123mua.vn'
allowed_domains = ['dambao.123mua.vn']
start_urls = ['http://dambao.123mua.vn']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/u+\d+/.*']), 'parse_item'),
    Rule(LinkExtractor(allow=['/\d+/\d+/.*']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
