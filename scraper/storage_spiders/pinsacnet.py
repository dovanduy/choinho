# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//table//tr[1]/td[@colspan='2']",
    'price' : "(//td/span[@class='price'])[1]",
    'category' : "//div[@class='text_product']/a",
    'description' : "//table//tr[2]/td/div[@class='bosung']",
    'images' : "//div[@id='content2']/div/div/table//tr/td/div/a[@class='screenshot']/img/@src",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'pinsac.net'
allowed_domains = ['pinsac.net']
start_urls = ['http://pinsac.net/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow = ['-p$','-a$']), 'parse_item'),
    Rule(LinkExtractor(allow = ['-h$','-b$','curPg=']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
