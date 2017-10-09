# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='name_product']/h1",
    'price' : "//table//tr[3]/td[2]/strong[@class='price pink']",
    'category' : "//div[@id='location']/a",
    'description' : "//div[@class='detail']/div[@class='content_tab']",
    'images' : "//div[@id='img_large']/div[@class='zoomp']/a/@href",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'mbcarehanoi.com'
allowed_domains = ['mbcarehanoi.com']
start_urls = ['http://mbcarehanoi.com']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/p+\d+\.html']), 'parse_item'),
    Rule(LinkExtractor(allow=['/c+\d+\.html']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]