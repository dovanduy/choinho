# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div/div/div/div[@class='namesp']/text()",
    'price' : "//div/div/div/div[@class='giaspchitiet']",
    'category' : "//div/div/a[@class='achu']/span[@class='achu']",
    'description' : "//div[@class='divchinh']/div[@class='divchinh']/div/div[@id='thongtinchitiet']",
    'images' : "//div/div[@id='content']/a[@class='jqzoom']/@href",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'thegioicamtay.vn'
allowed_domains = ['thegioicamtay.vn']
start_urls = ['http://thegioicamtay.vn']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/sanphamdetails/']), 'parse_item'),
    Rule(LinkExtractor(allow=['/san-pham/']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]