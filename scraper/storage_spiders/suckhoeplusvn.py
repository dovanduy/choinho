# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//h1",
    'price' : "//div[@class='top-right-detail']/div[@class='top1right']",
    'category' : "//div[@class='right-beccm']/ul/li/a",
    'description' : "//div[@class='content-detail']/div[@class='content1top article readmore-js-section readmore-js-collapsed']",
    'images' : "//div[@class='title-left-img-fixed']/div/img/@src",
    'canonical' : "//link[@rel='canonical']/@href",
    'base_url' : "",
    'brand' : ""
}
name = 'suckhoeplus.vn'
allowed_domains = ['suckhoeplus.vn']
start_urls = ['http://suckhoeplus.vn/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/\d+\.htm']), 'parse_item'),
    Rule(LinkExtractor(allow=['/cat-\d+\.htm']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]