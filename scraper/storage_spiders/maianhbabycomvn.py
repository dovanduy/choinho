# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='list-news']/font",
    'price' : "//div[@id='details']/div[2]/div[2]",
    'category' : "//div[@class='list-news']/a",
    'description' : "//div[@id='moinhat']/div[@class='detail']",
    'images' : "//li/a/img/@src",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'maianhbaby.com.vn'
allowed_domains = ['maianhbaby.com.vn']
start_urls = ['http://maianhbaby.com.vn']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/san-pham+/\d+[a-zA-Z0-9-]+\.html']), 'parse_item'),
    Rule(LinkExtractor(allow=['/danh-muc-san-pham/']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]