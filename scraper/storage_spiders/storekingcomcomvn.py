# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//h1[@id='product-title']",
    'price' : "//ul[@class='list-unstyled']/li/h2",
    'category' : "//ul[@class='breadcrumb']/li/a",
    'description' : "//div[@class='col-sm-7']/div[@class='row']/div[@class='col-sm-5']",
    'images' : "//a[@class='thumbnail']/@href",
    'canonical' : "//link[@rel='canonical']/@href",
    'base_url' : "//base/@href",
    'brand' : ""
}
name = 'store.kingcom.com.vn'
allowed_domains = ['store.kingcom.com.vn']
start_urls = ['https://store.kingcom.com.vn/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/[\w\d-]+-p\d+(c\d+)+\.html$']), 'parse_item'),
    Rule(LinkExtractor(allow=['/[\w\d-]+-(c\d+)+\.html($|\?page=\d+)']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]