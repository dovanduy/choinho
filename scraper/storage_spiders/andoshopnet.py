# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='product-title defaultTitle']/h1",
    'price' : "//div[@class='Value']/em[@class='ProductPrice VariationProductPrice']",
    'category' : "",
    'description' : "",
    'images' : "//div[@class='zoomPad']/img/@src | //img[@id='TinyImage_0']/@src",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'andoshop.net'
allowed_domains = ['andoshop.net']
start_urls = ['http://andoshop.net']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/[a-zA-Z0-9-]+\d+\.html']), 'parse_item'),
    Rule(LinkExtractor(allow=['/\d+\.html']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
