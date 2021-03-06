# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='detailsptitle']",
    'price' : "//div[@class='spsummery']/li[@class='gachdaudong'][2]/span[@class='thongtin']",
    'category' : "//font[@class='navMenu']",
    'description' : "//div[@class='spsummery']/li[@class='gachdaudong']/span",
    'images' : "//div[@class='detailimages']/a/img/@src",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'sieuthicongnghe.com.vn'
allowed_domains = ['sieuthicongnghe.com.vn']
start_urls = ['http://www.sieuthicongnghe.com.vn/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/detailProduct+/']), 'parse_item'),
    Rule(LinkExtractor(allow=['/viewcatalogcat/']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
