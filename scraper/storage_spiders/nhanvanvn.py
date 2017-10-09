# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='detail']/h1/font/b",
    'price' : "//div[@class='detail']/h1/font[4]",
    'category' : "//div[@class='menuheaders selected']/a",
    'description' : "//div[@class='news'][2]",
    'images' : "//div[@class='detailimages']/img/@src",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'nhanvan.vn'
allowed_domains = ['nhanvan.vn']
start_urls = ['http://www.nhanvan.vn/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(), 'parse_item'),
    Rule(LinkExtractor(), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
