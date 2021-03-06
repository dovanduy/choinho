# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//span[@class='ProductNameLink']/h1",
    'price' : "//div[@id='Product-Midle']/span[@class='ProductPriceNew']",
    'category' : "//ul[@class='col-xs-12']/li[@class='list-unstyled pull-left']/h2/a",
    'description' : "//div[@id='Product-Midle']/article[@id='Context']",
    'images' : "//img[@id='thumb']/@src",
    'canonical' : "",
    'base_url' : "//base/@href",
    'brand' : ""
}
name = 'mayfax.net'
allowed_domains = ['mayfax.net']
start_urls = ['http://mayfax.net']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['-\d+\.html$']), 'parse_item'),
    Rule(LinkExtractor(allow=['/[a-zA-Z-]+[/a-zA-Z0-9-]*'], deny=['\.html']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
