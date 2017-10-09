# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//h1[@id='text_name']",
    'price' : "//div[@id='detail_pro']/p[@id='text_price']",
    'category' : "//div[@id='second_menu']/ul/li/a",
    'description' : "//div[@id='detail_pro_tab']/div[@id='panel1']",
    'images' : "//div[@class='ad-thumbs']/ul/li/a/img/@src",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'phukiendientu.vn'
allowed_domains = ['phukiendientu.vn']
start_urls = ['http://phukiendientu.vn']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow = ['/chitiet/']), 'parse_item'),
    Rule(LinkExtractor(allow = ['/sanpham/']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
