# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='infoProduct']/h1",
    'price' : "//div[@class='abc']/div[@class='txPro ui-mark'][2]/span[@class='color-red font-bigger']",
    'category' : "//ul[@class='bc-menu']/li/a",
    'description' : "//div[@class='list-news']",
    'images' : "//div[@class='thumnailProduct']//ul/li/a/@data-image",
    'canonical' : "//link[@rel='canonical']/@href",
    'base_url' : "",
    'brand' : ""
}
name = 'baothymobile.com.vn'
allowed_domains = ['baothymobile.com.vn']
start_urls = ['http://baothymobile.com.vn/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['']), 'parse_item'),
    Rule(LinkExtractor(allow=['']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
