# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='tensp_ct']/h1",
    'price' : "//td/div[@class='gia_ct']",
    'category' : "//span[@id='Lbtenloai']/a",
    'description' : "//div[@class='chudenthuong']/table[@class='product-compare']",
    'images' : "//div[@class='main_content_1']/div[1]/table//a/@href",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'mykim.vn'
allowed_domains = ['mykim.vn']
start_urls = ['http://mykim.vn/san-pham-dien-may/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/chi-tiet/']), 'parse_item'),
    Rule(LinkExtractor(allow=['/san-pham/']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
