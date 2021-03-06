# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@id='infoleft']/h1[@class='single-title']",
    'price' : "//ul[@class='detailpro']/li/p",
    'category' : "//main[@class='content']/div[@class='breadcrumb']",
    'description' : "//div[@class='entry-content']/p",
    'images' : "//div[@class='detail-product']/div[@class='img-detail']//a/@href ",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'belo.vn'
allowed_domains = ['belo.vn']
start_urls = ['http://belo.vn']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/pro/']), 'parse_item'),
    Rule(LinkExtractor(allow=['/cat-pro/']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
