# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='tb-detail-hd']/h1",
    'price' : "//li[@id='J_StrPriceModBox']/strong[@id='J_StrPrice']",
    'category' : "",
    'description' : "",
    'images' : "//ul[@id='J_UlThumb']/li//img/@src",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'dentrungthu.com'
allowed_domains = ['dentrungthu.com']
start_urls = ['http://dentrungthu.com/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/[a-zA-Z0-9-]+\.html$']), 'parse_item'),
    Rule(LinkExtractor(allow=['/[a-zA-Z-]+/$']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
