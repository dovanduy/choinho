# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//h1",
    'price' : "//div[@id='detail_product']//b[@class='red']",
    'category' : "//div[@id='location']/a",
    'description' : "//div[@id='tab_detail_product']/div[@class='content_tab']",
    'images' : "//div[@id='img_large']/a/@href",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'japanvip.vn'
allowed_domains = ['japanvip.vn']
start_urls = ['http://www.japanvip.vn/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/[\w\d-]+/p\d+\.html$']), 'parse_item'),
    Rule(LinkExtractor(allow=['/[\w\d-]+/c\d+\.html$']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
