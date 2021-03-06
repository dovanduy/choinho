# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='bordergraycenter']/table//tr/td/h1[@class='productdetailname']",
    'price' : "//div[@class='bordergraycenter']/table//tr/td/div/div[@class='price']",
    'category' : "//div[@class='titlecenterblue']/a",
    'description' : "//div[@class='bordergraycenter']/div[3]/div",
    'images' : "//td[@class='productimagedetail']/a/@href",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'thethaothientruong.vn'
allowed_domains = ['thethaothientruong.vn']
start_urls = ['http://www.thethaothientruong.vn/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/[a-zA-Z0-9-]+-\d+\.html']), 'parse_item'),
    Rule(LinkExtractor(allow=['/[a-zA-Z0-9-]+/']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
