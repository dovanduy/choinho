# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//h2[@class='name-product-detail']",
    'price' : "//div[@class='wrapP_Content']/div[@class='curren-price']",
    'category' : "//ul/li[@class='cat']/a[@itemprop='url']",
    'description' : "",
    'images' : "//div[@class='slider owl-carousel owl-theme']/div[@class='item']/a[@class='changemedia swipebox']/@href",
    'canonical' : "//link[@rel='canonical']/@href",
    'base_url' : "",
    'brand' : "",
    'in_stock' : "",
    'guarantee' : "",
    'promotion' : ""
}
name = 'lemino.vn'
allowed_domains = ['lemino.vn']
start_urls = ['http://lemino.vn/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = ['']
rules = [
    #Rule(LinkExtractor(), 'parse_item'),
    #Rule(LinkExtractor(), 'parse'),
    Rule(LinkExtractor(allow=['http://lemino.vn/[a-zA-Z0-9-]+(/pageindex-\d+)?\.html$']), 'parse_item_and_links'),
]