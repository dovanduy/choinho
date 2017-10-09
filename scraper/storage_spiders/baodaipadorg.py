# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='header_layer_2']/h1/span/label",
    'price' : "//span[@class='giavnd'] | //span[@class='gia_tt']",
    'category' : "//div[@class='boxgiua_lop2']/p[1]/strong/a",
    'description' : "//div[@class='boxgiua_lop2']/p",
    'images' : "//img[@id='anh_chitiet_sanpham']/@src",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'baodaipad.org'
allowed_domains = ['baodaipad.org']
start_urls = ['http://baodaipad.org']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/[a-zA-Z0-9-_]+-id+\d+\.html']), 'parse_item'),
    Rule(LinkExtractor(allow=['/[a-zA-Z0-9-_]+-d+\d+\.html']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
