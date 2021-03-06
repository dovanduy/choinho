# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@id='ctl00_cpMainpage_Main1_ctl00_pnBox']/h1",
    'price' : "//div[@class='contentbox']/div[@class='productprice']",
    'category' : "//div[@class='path'][2]/a/span",
    'description' : "//div[@class='content']/p",
    'images' : "//div[@class='common']/a/img/@src",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'deptunhien.com.vn'
allowed_domains = ['deptunhien.com.vn']
start_urls = ['http://www.deptunhien.com.vn/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow = ['/p/[a-zA-Z0-9-]+.htm']), 'parse_item'),
    Rule(LinkExtractor(), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
