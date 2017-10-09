# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='product-detail clearfix']/div[@class='product-item']/div[@class='property']/h1[@class='product-name']",
    'price' : "//div[@class='property']/ul[@class='meta']/li[@class='promo-price']/div[@class='dp-info']",
    'category' : "//div[@class='breadcrumb clearfix']/ul/li/a/span[@itemprop='title']",
    'description' : "//div[@id='product-info']/div[@class='col-main']/div[@class='main-wrap clearfix']/div[@id='attributes']",
    'images' : "//a[@class='cloud-zoom']/@href|//ul[@class='thumb-images clearfix']/li/div[@class='pic s40']/a/img/@src",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'ever.vn'
allowed_domains = ['ever.vn']
start_urls = ['http://ever.vn']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['-dpxi\d+\.html']), 'parse_item'),
    Rule(LinkExtractor(allow=['/[a-zA-Z-]+/']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
