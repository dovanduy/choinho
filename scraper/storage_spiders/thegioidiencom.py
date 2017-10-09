# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@id='dvprdthd']/span[3]",
    'price' : "//div[@class='prdtshoprow1left']/span[@class='spangiabanview']",
    'category' : "//div[@id='dvgiuacontent']/div[@id='dvquicknav']/a",
    'description' : "//div[@id='dvtabif']/div[@id='tabchitiet']",
    'images' : "//div[@id='galleria']//img/@src",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'thegioidien.com'
allowed_domains = ['thegioidien.com']
start_urls = ['http://www.thegioidien.com']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = ['']
rules = [
    Rule(LinkExtractor(), 'parse_item'),
    Rule(LinkExtractor(), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
