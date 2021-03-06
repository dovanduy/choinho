# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div/h1[@class='thread-details-title']",
    'price' : "//div/div[@class='gia-ban-int']",
    'category' : "//div[@class='thread-header-title']/a",
    'description' : "//div[@id='uiThreadDetails']/div[@class='thread-border-content']",
    'images' : "//img[@id='img_slideshow']/@src",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'zavado.vn'
allowed_domains = ['zavado.vn']
start_urls = ['http://zavado.vn']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/muachung+-\d+/']), 'parse_item'),
    Rule(LinkExtractor(allow=['/cid+-\d+/']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
