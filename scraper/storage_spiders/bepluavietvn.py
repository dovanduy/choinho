# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='col-xs-12 col-sm-12 col-md-12 col-lg-7 body-holder']/div[@class='summary entry-summary body']/div[@class='title']/h1[@class='product_title entry-title']",
    'price' : "//div[@class='summary entry-summary body']/div[@class='prices clearfix']/ins/span[@class='amount']",
    'category' : "//div[@class='breadcrumb-nav-holder minimal']/ul[@class='mc-breadcrumb']/li/span",
    'description' : "//div[@class='container-fluid']/div[@class='tab-holder']/div[@class='tab-content']/div[@id='tab-description']",
    'images' : "//div[@class='col-xs-12 col-sm-8 col-sm-offset-2 col-md-offset-3 col-lg-offset-0 col-md-6 col-lg-5 gallery-holder']/div[@class='images']/a/img/@src",
    'canonical' : "//link[@rel='canonical']/@href",
    'base_url' : "",
    'brand' : ""
}
name = 'bepluaviet.vn'
allowed_domains = ['bepluaviet.vn']
start_urls = ['http://bepluaviet.vn']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/shop/']), 'parse_item'),
    Rule(LinkExtractor(allow=['/sp/[/a-zA-Z0-9-]+$']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
