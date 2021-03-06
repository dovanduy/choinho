# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//h1",
    'price' : "//div[@class='col-md-4']/p/span[@class='price-original']|//div[@class='col-md-4 col-xs-12']/p/span[@class='price']",
    'category' : "//div[@class='container-fluid']/ul/li/a",
    'description' : "//div[@class='col-md-12 prd-desc tskt']",
    'images' : "//ul[@class='overview']/li/a/@href",
    'canonical' : "",
    'base_url' : "",
    'brand' : "",
    'in_stock' : "",
    'guarantee' : "",
    'promotion' : ""
}
name = 'phankhang.vn'
allowed_domains = ['phankhang.vn']
start_urls = ['http://phankhang.vn/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = ['']
rules = [
    Rule(LinkExtractor(allow=['/[a-zA-Z0-9-]+-d+\.html']), 'parse_item'),
    Rule(LinkExtractor(allow=['/[a-zA-Z0-9-]+$'], deny=['/tin-tuc/']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
