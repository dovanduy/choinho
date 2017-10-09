# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='detail-product-content-name']",
    'price' : "//div[@class='detail-product-content-price']",
    'category' : "//span[@class='title-link-item']/a",
    'description' : "//div[@class='detail-product-content']",
    'images' : "//div[@class='l-i-b-item-image']/img/@src",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'tonymolyvn.com.vn'
allowed_domains = ['tonymolyvn.com.vn']
start_urls = ['http://tonymolyvn.com.vn']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/chi-tietsp/']), 'parse_item'),
    Rule(LinkExtractor(allow=['/loaisanpham/']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]