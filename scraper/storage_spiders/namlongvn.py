# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//span[@class='ProductNameLink']/h1",
    'price' : "//span[@class='ProductPriceNew']",
    'category' : "//ul[@class='col-xs-12']/li[@class='list-unstyled pull-left']/h2/a",
    'description' : "//div[@class='row']/div[@id='Product-Midle']/article[@id='Context']/span[@class='Context']",
    'images' : "//img[@id='thumb']/@src",
    'canonical' : "",
    'base_url' : "//base/@href",
    'brand' : ""
}
name = 'namlong.vn'
allowed_domains = ['namlong.vn']
start_urls = ['http://namlong.vn']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow = ['/[a-zA-Z0-9-]+\d+.html']), 'parse_item'),
    Rule(LinkExtractor(allow = ['\.html']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
