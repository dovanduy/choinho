# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//h1[@class='header-1']",
    'price' : "//div[@class='r']/div[@class='price']",
    'category' : "//div[@class='breadcrumb']/a",
    'description' : "//div[@class='tab-content']/div/div",
    'images' : "//ul[@class='image-additional']/li/a/@href",
    'canonical' : "//link[@rel='canonical']/@href",
    'base_url' : "//base/@href",
    'brand' : ""
}
name = 'itgirl.vn'
allowed_domains = ['itgirl.vn']
start_urls = ['http://itgirl.vn/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/[a-zA-Z-]+/[a-zA-Z-]+/[a-zA-Z0-9-]+$']), 'parse_item'),
    Rule(LinkExtractor(allow=['/[a-zA-Z-]+/[a-zA-Z-]+$']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
