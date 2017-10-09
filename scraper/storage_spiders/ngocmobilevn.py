# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='product-detail-info']/div[@class='product-avata']/h1",
    'price' : "//div[@class='product-price']/div[@class='col-1']/span",
    'category' : "",
    'description' : "//div[@id='tabc2']/div[@id='product-info-text']",
    'images' : "//div[@class='product-detail-image']/div/img/@data-zoom-image | //div[@id='product-info-text']/p/img/@src",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'ngocmobile.vn'
allowed_domains = ['ngocmobile.vn']
start_urls = ['http://ngocmobile.vn']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/product+/\d+/']), 'parse_item'),
    Rule(LinkExtractor(allow=['/category+/\d+/']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
