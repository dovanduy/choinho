# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='header_layer_2']/h1",
    'price' : "//input[@name='price']/@value",
    'category' : "//div[@class='thanh_dinh_huong']/a",
    'description' : "",
    'images' : "//img[@id='anh_chitiet_sanpham']/@src",
    'canonical' : "",
    'base_url' : "//base/@href",
    'brand' : ""
}
name = 'songvu.net'
allowed_domains = ['songvu.net']
start_urls = ['http://songvu.net/ao-so-mi-nam-d37v3.html']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/[a-zA-Z0-9-]+-id\d+\.html$']), 'parse_item'),
    Rule(LinkExtractor(allow=['/[a-zA-Z0-9-]+-d\d+(v3)?(p\d+)?\.html$']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
