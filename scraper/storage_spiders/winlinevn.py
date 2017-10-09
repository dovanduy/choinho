# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='pdhme']/div[@class='product-description']/div[@class='pd-name']/h1",
    'price' : "//div[@class='pdhme']/div[@class='product-description']/div[@class='pctemp']/div[@class='sub1 txt_20']",
    'category' : "//div[@id='main_h1']/div[@class='lead_sub2']/div/a",
    'description' : "//div[@class='pdhme']/div[@class='left-bot-detail']/div[@id='tab_info_detail']/div[@class='content_tab']",
    'images' : "//div[@class='thumb-view']/a/@href",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'winline.vn'
allowed_domains = ['winline.vn']
start_urls = ['http://www.winline.vn']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['']), 'parse_item'),
    Rule(LinkExtractor(allow=['']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
