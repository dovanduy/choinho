# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@id='content']/div[@class='row product-info split-50-50']/div[@class='right']/h1[@class='heading-title']",
    'price' : "//div[@class='right']/div[@id='product']/ul[@class='list-unstyled price']/li[@class='product-price']",
    'category' : "//ul[@class='breadcrumb']/li/a/span",
    'description' : "//div[@class='product-tabs']/div[@class='tabs-content']",
    'images' : "//body/div[@class='zm-viewer ']/img/@src|//div[@class='left']/div[@class='image']/a/@href",
    'canonical' : "//link[@rel='canonical']/@href",
    'base_url' : "",
    'brand' : ""
}
name = 'halomobile.vn'
allowed_domains = ['halomobile.vn']
start_urls = ['http://halomobile.vn']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = ['']
rules = [
    #Rule(LinkExtractor(), 'parse_item'),
    #Rule(LinkExtractor(), 'parse'),
    Rule(LinkExtractor(allow=['/[a-zA-Z0-9-]+\.html($|\?page=\d+$)'], deny=['tim-kiem\.html','tag=']), 'parse_item_and_links'),
]
