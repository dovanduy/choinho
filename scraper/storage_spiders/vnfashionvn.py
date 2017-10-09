# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//h1[@itemprop='name']",
    'price' : "//div[@itemprop='offers']/span[@id='ctl00_ContentPlaceHolder1_ListView1_ctrl0_lblPrice']/strong",
    'category' : "//ul[@id='site']/li/a[@itemprop='url']/span[@itemprop='title']",
    'description' : "",
    'images' : "//meta[@property='og:image']/@content",
    'canonical' : "//link[@rel='canonical']/@href",
    'base_url' : "",
    'brand' : "",
    'in_stock' : "",
    'guarantee' : "",
    'promotion' : ""
}
name = 'vnfashion.vn'
allowed_domains = ['vnfashion.vn']
start_urls = ['http://www.vnfashion.vn/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = ['']
rules = [
    Rule(LinkExtractor(allow=['pi\d+']), 'parse_item'),
    Rule(LinkExtractor(allow=['pr\d+','ps\d+','pc\d+']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
