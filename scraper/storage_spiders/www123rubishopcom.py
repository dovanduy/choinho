# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//h1[@itemprop='name']",
    'price' : "//div[@class='cart']/div[@class='price']/span[@itemprop='price']",
    'category' : "",
    'description' : "//div[@class='tab-content']",
    'images' : "//ul[@class='image_carousel']/li/a/@href",
    'canonical' : "//link[@rel='canonical']/@href",
    'base_url' : "//base/@href",
    'brand' : "//div[@class='right']/div[@class='description']/a",
    'in_stock' : "",
    'guarantee' : ""
}
name = '123rubishop.com'
allowed_domains = ['123rubishop.com']
start_urls = ['http://123rubishop.com/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = ['']
rules = [
    #Rule(LinkExtractor(), 'parse_item'),
    #Rule(LinkExtractor(), 'parse'),
    Rule(LinkExtractor(allow=['/[\w-]+($|/page/\d+$)']), 'parse_item_and_links'),
]
