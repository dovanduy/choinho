# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//td[@class='spm-text']//td[@class='font-name-product1']",
    'price' : "//td[@class='spm-ten']/span[@class='price']/b",
    'category' : "//td[@class='top-menu1'][2]/div/span[@class='title-sao']",
    'description' : "//tr[6]/td[@class='spm-text'] ",
    'images' : "//td[@class='spm-text']//tr[3]/td/div/img/@src",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'bizo.vn'
allowed_domains = ['bizo.vn']
start_urls = ['http://bizo.vn/home/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow = ['/detail.asp.*']), 'parse_item'),
    Rule(LinkExtractor(allow = ['/type.asp.*']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]