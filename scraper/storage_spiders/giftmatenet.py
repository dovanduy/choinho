# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//h1[@itemprop='name']",
    'price' : "//div[@class='prices detail']/ul[@class='list-unstyled']/li/span[@itemprop='price']",
    'category' : "//a[@itemprop='item']/span[@itemprop='name']",
    'description' : "",
    'images' : "//ul[@id='thumblist']/li[@class='thumb_item  ']/a/@data-image",
    'canonical' : "//link[@rel='canonical']/@href",
    'base_url' : "",
    'brand' : "",
    'in_stock' : "//div[@class='product-info-bg']/div[@class='product-center-column col-xs-12 col-sm-7 col-md-7 col-lg-7']/ul[@class='list-unstyled']/li",
    'guarantee' : "",
    'promotion' : ""
}
name = 'giftmate.net'
allowed_domains = ['giftmate.net']
start_urls = ['http://giftmate.net/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = ['']
rules = [
    Rule(LinkExtractor(allow=['/collections/[a-zA-Z0-9-]+/products/']), 'parse_item'),
    Rule(LinkExtractor(allow=['/collections/[a-zA-Z0-9-]+$']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]