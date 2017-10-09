# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@id='content']/div[@class='product-info clearfix']/div[@class='left']/h1[@class='product_name']",
    'price' : "//div[@class='product-info clearfix']/div[@class='right']/div[@class='price']/span | //div[@class='right']/div[@class='price']/span",
    'category' : "//div[@id='body-wrapper']/div[@id='content']/div[@class='breadcrumb']/a",
    'description' : "//body/div[@id='body-wrapper']/div[@id='content']/div[@id='tab-description']",
    'images' : "//div[@id='carousel']/span/img/@src | //div[@id='carousel']//img/@src",
    'canonical' : "//link[@rel='canonical']/@href",
    'base_url' : "//base/@href",
    'brand' : ""
}
name = 'taru.vn'
allowed_domains = ['taru.vn']
start_urls = ['http://taru.vn']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/[a-zA-Z0-9-]+\.html']), 'parse_item'),
    Rule(LinkExtractor(allow=['/\.*']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
