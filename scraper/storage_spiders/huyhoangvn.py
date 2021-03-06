# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='main-full-content']/div[@class='content-center fl']/div[@class='content-main']/h1",
    'price' : "//div[@class='info-detail']/div[@class='su-pi']/div/span[@class='price-new']|//div[@class='spritespin-stage']//img/@src",
    'category' : "//div[@class='content-center fl']/div[@class='content-main']/div[@class='tree-url']/a",
    'description' : "//div[@class='content-main']/div[@id='tab-content']/div[@class='multi-tab-content']/div[@class='tong-quan block']",
    'images' : "//meta[@property='og:image']/@content",
    'canonical' : "",
    'base_url' : "//base/@href",
    'brand' : ""
}
name = 'huyhoang.vn'
allowed_domains = ['huyhoang.vn']
start_urls = ['http://huyhoang.vn']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = ['']
rules = [
    #Rule(LinkExtractor(), 'parse_item'),
    #Rule(LinkExtractor(), 'parse'),
    Rule(LinkExtractor(allow=['/[a-zA-Z0-9-]+($|\?p=\d+$)']), 'parse_item_and_links'),
]
