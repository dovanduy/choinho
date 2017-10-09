# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='main-product']/h1",
    'price' : "//div[@class='main-product']/table//tr[5]/td/div/b/span",
    'category' : "",
    'description' : "",
    'images' : "//div[@class='main-product']/table//tr[1]/th/img/@src",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'binaishop.com'
allowed_domains = ['binaishop.com']
start_urls = ['http://www.binaishop.com/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = ['']
rules = [
    Rule(LinkExtractor(allow=['/\d+/\d+/[a-zA-Z0-9-]+\.html$']), 'parse_item'),
    Rule(LinkExtractor(allow=['/search/label/']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
