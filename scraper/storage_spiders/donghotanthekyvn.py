# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='product-properties']/h1[@class='entry-title']",
    'price' : "//div[@class='product-image']/span[@class='price'] | //div[@id='content']/div/div[@class='product-image']/span",
    'category' : "",
    'description' : "//ul[@class='propertie-list']/li",
    'images' : "//div[@class='product-image']/p/img/@src",
    'canonical' : "//link[@rel='canonical']/@href",
    'base_url' : "",
    'brand' : ""
}
name = 'donghotantheky.vn'
allowed_domains = ['donghotantheky.vn']
start_urls = ['http://donghotantheky.vn']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/[a-zA-Z0-9-]+\.html']), 'parse_item'),
    Rule(LinkExtractor(allow=['/[a-zA-Z0-9-]+/']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]