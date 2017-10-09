# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//td[@class='title']/h1",
    'price' : "//table//tr/td[2]/table[1]//tr/td[@class='title'][2]",
    'category' : "//table//tr/td/div[@class='topic']/a",
    'description' : "//table//tr[9]/td[@class='content']",
    'images' : "//div[@class='zoomPad']/img/@src | //a[@class='jqzoom']/@href",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'beon.com.vn'
allowed_domains = ['beon.com.vn']
start_urls = ['http://beon.com.vn']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/[a-zA-Z0-9-]']), 'parse_item'),
    Rule(LinkExtractor(allow=['/[a-zA-Z0-9-]/']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
