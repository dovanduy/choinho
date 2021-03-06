# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='right']/h1",
    'price' : "//div[@class='price-new']/span[@class='amount contrast_font']",
    'category' : "//ul[@class='breadcrumb']/li/a",
    'description' : "//div[@class='col-sm-12 product']/div[@class='tab-content']/div[@id='tab-description']",
    'images' : "//img[@itemprop='image']/@src",
    'canonical' : "//link[@rel='canonical']/@href",
    'base_url' : "//base/@href",
    'brand' : ""
}
name = 'outlet.euplaza.vn'
allowed_domains = ['outlet.euplaza.vn']
start_urls = ['http://outlet.euplaza.vn/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/[a-zA-Z0-9-]+\?product_id=\d+$']), 'parse_item'),
    Rule(LinkExtractor(allow=['/[a-zA-Z0-9-]+($|\?page=\d+$)']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
