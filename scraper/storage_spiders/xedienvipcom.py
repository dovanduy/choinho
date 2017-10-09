# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@id='info_product']/h4",
    'price' : "//strong[@class='price']",
    'category' : "",
    'description' : "//div[@id='content_product']/div",
    'images' : "//ul[@class='amazingcarousel-list']/li/div/div/a/@href",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'xedienvip.com'
allowed_domains = ['xedienvip.com']
start_urls = ['http://xedienvip.com/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/p\d+\.html$']), 'parse_item'),
    Rule(LinkExtractor(allow=['/c\d+\.html']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]