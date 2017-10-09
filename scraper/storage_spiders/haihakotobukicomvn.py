# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@id='products']/div/h1",
    'price' : "//div[@id='products']/div/div[@class='price']",
    'category' : "//div[@class='inner']/div/div[@class='main-title']",
    'description' : "//div[@id='products']/div/div[@class='des-pro']",
    'images' : "//ul[@id='thumblist']/li/a/img/@src",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'haiha-kotobuki.com.vn'
allowed_domains = ['haiha-kotobuki.com.vn']
start_urls = ['http://www.haiha-kotobuki.com.vn/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['-\d+-p\d+\.aspx$']), 'parse_item'),
    Rule(LinkExtractor(allow=['-\d+\.aspx$']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
