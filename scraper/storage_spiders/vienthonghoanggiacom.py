# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='box_mid add_detail']/div[@class='mid-title']/div[@class='titleL']/h1",
    'price' : "//tr/td[@class='colInfo2']/span[@class='price_old']/span",
    'category' : "//div[@id='vnt-container']/div[@class='navigation']/span/a",
    'description' : "//tr/td[@class='content_tab']/div[@class='tab']/div[@class='tab_1']",
    'images' : "//div[@class='ad-image']/a/img/@src",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'vienthonghoanggia.com'
allowed_domains = ['vienthonghoanggia.com']
start_urls = ['http://vienthonghoanggia.com']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['']), 'parse_item'),
    Rule(LinkExtractor(allow=['']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
