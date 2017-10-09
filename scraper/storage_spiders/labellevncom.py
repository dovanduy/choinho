# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//h1[@id='title_detail_product']",
    'price' : "//label[@id='lblGiaTien']",
    'category' : "//label[@class='box_your_are_here_lbl']/a",
    'description' : "//div[@class='content_tab']/div[@class='tab_content']",
    'images' : "//li[@id='box_l']/div[@class='multizoom1']/a/@href",
    'canonical' : "",
    'base_url' : "",
    'brand' : "",
    'in_stock' : "",
    'guarantee' : "",
    'promotion' : ""
}
name = 'labellevn.com'
allowed_domains = ['labellevn.com']
start_urls = ['http://labellevn.com/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = ['']
rules = [
    Rule(LinkExtractor(allow=['/sanpham/']), 'parse_item'),
    Rule(LinkExtractor(allow=['/danhmuc/']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
