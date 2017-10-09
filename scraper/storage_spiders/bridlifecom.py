# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//h1[@class='header  headline']/span/label",
    'price' : "//div[@class='div_gia']/span[@class='giavnd ']",
    'category' : "//div[@class='bang_chi_tiet_san_pham']/p/strong/a",
    'description' : "//div[@class='bang_chi_tiet_san_pham']/div[@class='mo_ta_sanpham'] | //div[@class='tabDetails']/div[@id='tab0']/p",
    'images' : "//div[@class='div_anh']/div[@class='div_anh_chi_tiet']//img/@src",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'bridlife.com'
allowed_domains = ['bridlife.com']
start_urls = ['http://bridlife.com']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/[a-zA-Z0-9-]+-id+\d+\.html']), 'parse_item'),
    Rule(LinkExtractor(allow=['/[a-zA-Z0-9-]+-d+\d+\.html']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
