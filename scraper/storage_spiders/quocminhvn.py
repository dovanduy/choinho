# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='header_layer_2']/h1[@class='header  headline']",
    'price' : "//div[@class='div_gia']/span[@class='giavnd ']/span",
    'category' : "",
    'description' : "//div[@class='tabContents']/p",
    'images' : "//img[@id='anh_chitiet_sanpham']/@src",
    'canonical' : "",
    'base_url' : "//base/@href",
    'brand' : ""
}
name = 'quocminh.vn'
allowed_domains = ['quocminh.vn']
start_urls = ['http://www.quocminh.vn/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['']), 'parse_item'),
    Rule(LinkExtractor(allow=['']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
