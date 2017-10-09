# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='product-name']/h1",
    'price' : "//div[@class='price-box-content']/span[@class='regular-price']/span[@class='price']",
    'category' : "",
    'description' : "//div[@class='main']/div[@class='thong-so-ky-thuat']",
    'images' : "//div[@class='product-img-box']/a/img/@src | //div[@class='product-img-box']/div[@class='more-views']/ul/li/a/img/@src",
    'canonical' : "",
    'base_url' : "",
    'brand' : "",
    'in_stock' : "",
    'guarantee' : "",
    'promotion' : "//div[@class='khuyenmai']/div[@class='khuyenmai-info']"
}
name = 'cellphones.com.vn'
allowed_domains = ['cellphones.com.vn']
start_urls = ['http://cellphones.com.vn/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = ['']
rules = [
    #Rule(LinkExtractor(), 'parse_item'),
    #Rule(LinkExtractor(), 'parse'),
    Rule(LinkExtractor(allow=['\.html']), 'parse_item_and_links'),
]
