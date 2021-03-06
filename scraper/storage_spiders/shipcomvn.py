# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='d-main1right']/div[@class='d-titlepro']/h1/a",
    'price' : "//div[@class='info']/ul/li/span[@class='right gia-ban']",
    'category' : "//div[@class='boun']/div[@class='h-bounmenu']/div[@class='h-menu2']/a",
    'description' : "//div[@class='h-bounmain']/div[@class='d-main4']/div[@class='d-main4lef product-content']/p",
    'images' : "//div[@class='d-imgproduc']/a/img/@src",
    'canonical' : "//link[@rel='canonical']/@href",
    'base_url' : "",
    'brand' : ""
}
name = 'ship.com.vn'
allowed_domains = ['ship.com.vn']
start_urls = ['http://ship.com.vn']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/[a-zA-Z0-9-]+\.html']), 'parse_item'),
    Rule(LinkExtractor(allow=['-s+\d+$']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
