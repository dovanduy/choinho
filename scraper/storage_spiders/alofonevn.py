# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='infoProduct']/h1",
    'price' : "//span[@class='color-red font-bigger']",
    'category' : "",
    'description' : "//div[@id='detail_product']/div/div[@class='_mota']",
    'images' : "//ul[@id='mycarousel']/li/a/img/@src",
    'canonical' : "//link[@rel='canonical']/@href",
    'base_url' : "",
    'brand' : ""
}
name = 'alofone.vn'
allowed_domains = ['alofone.vn']
start_urls = ['http://alofone.vn/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/[a-zA-Z0-9-]+-1-1-\d+\.html']), 'parse_item'),
    Rule(LinkExtractor(allow=['/[a-zA-Z0-9-]+-2-1-\d+\.html']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]