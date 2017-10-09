# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='col-lg-7 col-md-7 col-sm-12 col-xs-12 product-view']/h1",
    'price' : "//div[@class='price']/div[@class='price-gruop']",
    'category' : "//ol[@class='breadcrumb container']/li",
    'description' : "//div[@id='tab-description']/div[@class='sidebar2']",
    'images' : "//div[@class='image col-lg-10 col-md-12']/a/@href",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'trangsucbac.vn'
allowed_domains = ['trangsucbac.vn']
start_urls = ['http://trangsucbac.vn']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = ['']
rules = [
    Rule(LinkExtractor(allow=['/[a-zA-Z0-9-]+\.html']), 'parse_item'),
    Rule(LinkExtractor(allow=['/[a-zA-Z0-9-]+($|\?page=\d+)']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
